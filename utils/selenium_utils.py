from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from config.config import HEADLESS, PAGE_LOAD_TIMEOUT, ERROR_MESSAGES

class SeleniumUtils:
    @staticmethod
    def get_driver():
        """
        Inicializa e retorna uma instância do WebDriver do Chrome
        Configura as opções do navegador e define o timeout de carregamento de página
        """
        chrome_options = Options()
        if HEADLESS:
            chrome_options.add_argument('--headless=new')  # Novo modo headless
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')  # Necessário para Windows
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-software-rasterizer')
        
        try:
            # Configuração específica para Windows
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
            return driver
        except Exception as e:
            print(f"Erro ao inicializar o WebDriver: {str(e)}")
            raise

    @staticmethod
    def wait_for_element(driver, locator, timeout=10):
        """
        Aguarda até que um elemento esteja presente e visível na página
        Args:
            driver: Instância do WebDriver
            locator: Tupla com o método de localização e o valor (ex: (By.ID, "elemento"))
            timeout: Tempo máximo de espera em segundos
        Returns:
            O elemento encontrado
        Raises:
            TimeoutException: Se o elemento não for encontrado no tempo especificado
        """
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise TimeoutException(f"{ERROR_MESSAGES['element_not_found']}: {locator}")

    @staticmethod
    def wait_for_clickable(driver, locator, timeout=10):
        """
        Aguarda até que um elemento esteja clicável na página
        Args:
            driver: Instância do WebDriver
            locator: Tupla com o método de localização e o valor
            timeout: Tempo máximo de espera em segundos
        Returns:
            O elemento clicável
        Raises:
            TimeoutException: Se o elemento não ficar clicável no tempo especificado
        """
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            raise TimeoutException(f"{ERROR_MESSAGES['element_not_clickable']}: {locator}")

    @staticmethod
    def take_screenshot(driver, name):
        """
        Captura uma screenshot da página atual
        Args:
            driver: Instância do WebDriver
            name: Nome do arquivo para salvar a screenshot
        """
        try:
            driver.save_screenshot(f"reports/screenshots/{name}.png")
        except Exception as e:
            print(f"Erro ao capturar screenshot: {str(e)}")
            raise 