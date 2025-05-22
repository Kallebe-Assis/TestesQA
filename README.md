# Testes Automatizados - Site da Steam

Projeto de testes automatizados no site da Steam usando Python e Selenium.

## 📁 Estrutura do Projeto

```
steam_tests/
├── tests/         # Testes (performance, funcional, UI, API)
├── utils/         # Funções e utilitários
├── config/        # Configurações
└── reports/       # Relatórios
```

## ⚙️ Como Usar

1. Criar ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

2. Instalar dependências:
```bash
pip install -r requirements.txt
```

3. Configurar `.env`:
```
STEAM_URL=https://store.steampowered.com
```

## ▶️ Executar Testes

### Performance
```bash
locust -f tests/performance/locustfile.py  
pytest tests/performance/test_stress.py
```

### Funcionais
```bash
pytest tests/functional/
```

### UI
```bash
pytest tests/ui/
```

### API
```bash
pytest tests/api/
```

## 📊 Relatórios

Relatórios de testes são gerados na pasta `reports` após a execução.
