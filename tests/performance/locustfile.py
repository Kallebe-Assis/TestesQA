from locust import HttpUser, task, between
from config.config import BASE_URL

class SteamUser(HttpUser):
    wait_time = between(1, 3)
    host = BASE_URL

    @task(3)
    def browse_store(self):
        """Simulate browsing the store"""
        self.client.get("/")
        self.client.get("/search/")
        self.client.get("/explore/")

    @task(2)
    def search_games(self):
        """Simulate searching for games"""
        self.client.get("/search/results?term=action")
        self.client.get("/search/results?term=rpg")

    @task(1)
    def view_game_details(self):
        """Simulate viewing game details"""
        self.client.get("/app/570/")  # Dota 2
        self.client.get("/app/730/")  # CS:GO

    @task(1)
    def browse_categories(self):
        """Simulate browsing game categories"""
        self.client.get("/category/action/")
        self.client.get("/category/rpg/")
        self.client.get("/category/strategy/") 