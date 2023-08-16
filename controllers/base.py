from typing import List

from models.player import Player
from models.tournament import Tournament
from models.match import Match

from data import PlAYERS


class Controller:
    """ Le Contrôleur """

    def __init__(self):
        # mettre la vue içi
        self.players: List[Player] = []
        self.list_players = []
        self.id_with_score = []


    def get_players(self):
        player_info = PlAYERS
        for i in player_info:
            player = Player(i[0], i[1], i[2], i[3])
            self.players.append(player)
            self.list_players.append([player.name, player.first_name, player.date_birth, player.id_chess])
        print("Print - get_player dans Controller - Len list_player :", len(self.list_players))


    def __str__(self):
        return f"test info du joueur dans controlleur {self.list_players}"



    def new_tournament(self):
        info_tournament = Tournament("Tournoi des Sorciers", "15 juillet", "Poudlard")
        info_tournament.list_players = self.list_players
#        print(info_tournament)
        # verifier si il est mieux de ne prendre que l'id et le score ou garder les autres infos du joueur en stock içi ???
        return info_tournament,


    def update_score(self):
        number_round = 1
        match_result = Match("Joueur01", 1, "Joueur02", 0)
        if number_round == 1:
            score = 0
        else:
            score = match_result
        for player in self.list_players:
            id_player = player[3]

            self.id_with_score.append([id_player, score])
        print(self.id_with_score)
        return self.id_with_score



    def sorted_players(self, players_with_score):
        sorted_players_scores = sorted(players_with_score, key= lambda x: x[1], reverse=True)
        print("Select players for match : ", sorted_players_scores)
        return sorted_players_scores



    def select_player_for_match(self):
        pass



    def run(self):
        self.get_players()
        print("Run")





