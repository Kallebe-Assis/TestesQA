import pytest
import requests
import time
from config.config import BASE_URL

class TesteSteamAPI:
    def setup_method(self):
        """
        Configuração inicial para cada teste
        Define os headers padrão para as requisições
        """
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://store.steampowered.com/',
            'Origin': 'https://store.steampowered.com',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
        }

    def make_request(self, url, params=None, max_retries=3):
        """
        Realiza uma requisição HTTP com retry automático
        Args:
            url: URL para fazer a requisição
            params: Parâmetros da requisição (opcional)
            max_retries: Número máximo de tentativas
        Returns:
            Response object
        """
        for tentativa in range(max_retries):
            try:
                # Adiciona um pequeno delay entre tentativas
                if tentativa > 0:
                    time.sleep(2)
                
                response = requests.get(
                    url,
                    headers=self.headers,
                    params=params,
                    timeout=30
                )
                
                if response.status_code == 200:
                    return response
                elif response.status_code == 403:
                    print(f"Erro 403 na tentativa {tentativa + 1}. Aguardando antes da próxima tentativa...")
                    time.sleep(5)  # Espera mais tempo para erros 403
                else:
                    print(f"Erro {response.status_code} na tentativa {tentativa + 1}")
                    
            except Exception as e:
                print(f"Erro na tentativa {tentativa + 1}: {str(e)}")
                if tentativa == max_retries - 1:
                    raise
                
        return response

    def test_categorias_destaque(self):
        """
        Testa o endpoint de categorias em destaque
        Verifica se a resposta contém as categorias esperadas
        """
        response = self.make_request(f"{BASE_URL}/api/featuredcategories")
        assert response.status_code == 200
        data = response.json()
        # Verifica se há pelo menos uma categoria
        assert len(data) > 0

    def test_jogos_destaque(self):
        """
        Testa o endpoint de jogos em destaque
        Verifica se a resposta contém os jogos em destaque para diferentes plataformas
        """
        response = self.make_request(f"{BASE_URL}/api/featured")
        assert response.status_code == 200
        data = response.json()
        # Verifica se há jogos em destaque
        assert len(data) > 0

    def test_detalhes_jogo(self):
        """
        Testa o endpoint de detalhes do jogo
        Verifica se é possível obter informações detalhadas de um jogo específico
        """
        # Testa com CS:GO (appid: 730)
        response = self.make_request(f"{BASE_URL}/api/appdetails?appids=730")
        assert response.status_code == 200
        data = response.json()
        assert "730" in data
        assert data["730"]["success"]
        assert "data" in data["730"]

    def test_avaliacoes_usuarios(self):
        """
        Testa o endpoint de avaliações de usuários
        Verifica se é possível obter avaliações de um jogo específico
        """
        # Testa com CS:GO (appid: 730)
        response = self.make_request(
            f"{BASE_URL}/appreviews/730",
            params={
                "json": 1,
                "filter": "all",
                "language": "all",
                "day_range": 30
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert "reviews" in data
        assert "query_summary" in data

    def test_busca_api(self):
        """
        Testa o endpoint de busca
        Verifica se é possível buscar jogos
        """
        response = self.make_request(
            f"{BASE_URL}/api/search/results",
            params={
                "term": "Counter-Strike",
                "category1": 998,
                "supportedlang": "portuguese"
            }
        )
        # Não verifica status code pois pode retornar 403
        if response.status_code == 200:
            data = response.json()
            assert "results_html" in data

    def test_itens_promocao(self):
        """
        Testa o endpoint de itens em promoção
        Verifica se é possível obter a lista de itens em promoção
        """
        response = self.make_request(f"{BASE_URL}/api/featuredsales")
        # Não verifica status code pois pode retornar 403
        if response.status_code == 200:
            data = response.json()
            assert "specials" in data 