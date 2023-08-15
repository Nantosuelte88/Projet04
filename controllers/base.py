from typing import List

from models.player import Player
from models.match import Match
from models.round import Round
from  models.tournament import Tournament
from data import PlAYERS


class Controller:
    """ Le Contrôleur """

    def __init__(self):
        # mettre la vue içi
        self.players: List[Player] = []
        self.list_players = []


    def get_players(self):
        player_info = PlAYERS
        for i in player_info:
            player = Player(i[0], i[1], i[2], i[3])
            self.players.append(player)
            self.list_players.append([player.name, player.first_name, player.date_birth, player.id_chess])

    def __str__(self):
        return f"test info du joueur dans controlleur {self.list_players}"


