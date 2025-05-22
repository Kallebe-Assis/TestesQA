# Testes Automatizados - Site da Steam

Projeto de testes automatizados no site da Steam usando Python e Selenium.

## Estrutura do Projeto

steam_tests/
├── tests/ # Testes (performance, funcional, UI, API)
├── utils/ # Funções e utilitários
├── config/ # Configurações
└── reports/ # Relatórios

bash
Copiar
Editar

## Como Usar

1. Criar ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instalar dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Configurar .env:

ini
Copiar
Editar
STEAM_URL=https://store.steampowered.com
Executar Testes
Performance:

bash
Copiar
Editar
locust -f tests/performance/locustfile.py  
pytest tests/performance/test_stress.py
Funcionais:

bash
Copiar
Editar
pytest tests/functional/
UI:

bash
Copiar
Editar
pytest tests/ui/
API:

bash
Copiar
Editar
pytest tests/api/
Relatórios
Relatórios de testes são gerados na pasta reports após a execução.

perl
Copiar
Editar

Se quiser que já venha com a formatação de Markdown visível no preview do GitHub, posso ajustar também.
