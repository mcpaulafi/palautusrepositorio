import requests

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = self.fetch_players()

    def fetch_players(self):
        response = requests.get(self.url).json()
        return response

    def get_players(self):
        return self.players
