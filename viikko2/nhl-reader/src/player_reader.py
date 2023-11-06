import requests
from player import Player


class PlayerReader:

    def __init__(self, url):
        self.players = [Player(pla) for pla in requests.get(url).json()]
