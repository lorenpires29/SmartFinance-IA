# SmartFinance AI 🚀

Uma plataforma premium de gestão financeira pessoal e familiar impulsionada por Inteligência Artificial (LLaMA 3.1). 

## ✨ Funcionalidades
- **Dashboard Interativo:** Acompanhamento de Saldo, Receitas e Despesas com gráficos de Fluxo de Caixa (linhas) e Distribuição (rosca).
- **Gestão de Contas da Família:** Tabela detalhada de transações com sistema de badges para Receitas (Verde) e Despesas (Vermelho).
- **Agente Financeiro IA:** Um assistente embutido conectado à **Groq API (LLaMA 3.1)**. Ele entende linguagem natural! Basta digitar *"Gastei 150 no ifood"* e o agente classificará, extrairá o valor e registrará a despesa automaticamente.
- **Insight Dinâmico:** Análises e alertas automáticos gerados a partir do seu comportamento financeiro.
- **Interface Premium:** Design moderno utilizando *Dark Mode* profundo e elementos *Glassmorphism*.

## 🛠️ Tecnologias Utilizadas
- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, Vanilla JS, Chart.js
- **Inteligência Artificial:** Groq API (LLaMA-3.1-8b-instant)
- **Banco de Dados:** SQLite (default Django)

## 🚀 Como Executar Localmente

1. Clone o repositório para sua máquina local.
2. No terminal, instale as dependências:
   ```bash
   pip install django groq
   ```
3. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da Groq API:
   ```
   GROQ_API_KEY='sua_chave_api_aqui'
   ```
   Você pode obter sua chave API em Groq Console.

3. Crie e aplique as migrações do banco de dados:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```
5. Acesse `http://127.0.0.1:8000/` no navegador.

---
Desenvolvido com 💜 para automação e saúde financeira.

Como recriar o projeto passo a passo: https://chemical-radiator-0ea.notion.site/Smart-Finance-AI-38a3f6ca33b78069bee8c75e907cf087
