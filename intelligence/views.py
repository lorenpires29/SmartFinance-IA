import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from groq import Groq
from finance.models import Transaction
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv() # Carrega as variáveis do .env
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

@login_required(login_url='/users/login/')
def chat_view(request):
    return render(request, 'chat.html')

@login_required(login_url='/users/login/')
def chat_api(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        today = datetime.now().strftime("%Y-%m-%d")
        
        system_prompt = f"""
Você é o SmartFinance AI, um Assistente Financeiro integrado a um painel. O usuário fala com você.
Se a mensagem contiver o registro de um gasto ou ganho financeiro, você DEVE retornar APENAS um JSON válido com a seguinte estrutura estrita:
{{"is_transaction": true, "amount": 100.50, "date": "{today}", "category": "Alimentação", "type": "despesa", "description": "Comida"}}
- amount: float.
- date: YYYY-MM-DD. Hoje é {today}. Ajuste se ele disser "ontem" ou "semana passada".
- category: escolha entre "Alimentação", "Transporte", "Lazer", "Moradia", "Salário" ou "Outros".
- type: "receita" ou "despesa".

Se NÃO for um registro de transação, responda amigavelmente também em JSON:
{{"is_transaction": false, "reply": "sua resposta aqui"}}
"""
        
        try:
            client = Groq(api_key=GROQ_API_KEY)
            response = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                model="llama-3.1-8b-instant",
                response_format={"type": "json_object"}
            )
            
            result = json.loads(response.choices[0].message.content)
            
            if result.get('is_transaction'):
                Transaction.objects.create(
                    user=request.user,
                    description=result.get('description', 'Transação Automática'),
                    amount=result.get('amount'),
                    date=result.get('date'),
                    category=result.get('category'),
                    type=result.get('type')
                )
                ai_reply = f"Lançamento feito! Salvei uma {result['type']} de R$ {result['amount']:.2f} em {result['category']}."
            else:
                ai_reply = result.get('reply', 'Não entendi.')
                
            return JsonResponse({'reply': ai_reply})
        except Exception as e:
            return JsonResponse({'reply': f"Erro na IA: {str(e)}"})
            
    return JsonResponse({'error': 'Invalid request'}, status=400)
