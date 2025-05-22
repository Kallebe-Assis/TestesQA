import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# URL base do site da Steam
BASE_URL = os.getenv('STEAM_URL', 'https://store.steampowered.com')

# Configurações do navegador
BROWSER = os.getenv('BROWSER', 'chrome')
HEADLESS = os.getenv('HEADLESS', 'False').lower() == 'true'

# Tempos de espera (em segundos)
DEFAULT_TIMEOUT = 10  # Tempo padrão de espera para elementos
PAGE_LOAD_TIMEOUT = 30  # Tempo máximo para carregar uma página

# Dados de teste do usuário
TEST_USER = {
    'username': os.getenv('TEST_USERNAME', ''),
    'password': os.getenv('TEST_PASSWORD', '')
}

# Configurações dos testes de performance
LOAD_TEST_USERS = 100  # Número de usuários virtuais para teste de carga
LOAD_TEST_SPAWN_RATE = 10  # Taxa de criação de usuários por segundo
STRESS_TEST_DURATION = 300  # Duração do teste de stress em segundos (5 minutos)

# Mensagens de erro
ERROR_MESSAGES = {
    'timeout': 'Tempo limite excedido ao aguardar elemento',
    'element_not_found': 'Elemento não encontrado na página',
    'invalid_response': 'Resposta inválida da API',
    'connection_error': 'Erro de conexão com o servidor',
    'invalid_credentials': 'Credenciais inválidas',
    'element_not_clickable': 'Elemento não está clicável'
}

# Configurações de relatório
REPORT_CONFIG = {
    'screenshot_dir': 'reports/screenshots',
    'log_dir': 'reports/logs',
    'report_dir': 'reports/html'
} 