from typing import List

from models.player import Player
from models.tournament import Tournament
from models.match import Match
from models.round import Round

from data import PlAYERS


ROUND_NUMBER = 4
MATCH_SCORE = [(1, 0), (0.5, 0.5), (0, 1)]

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
        score = 0
        for player in self.list_players:
            id_player = player[3]
            self.id_with_score.append([id_player, score])
        print(self.id_with_score)
        # verifier si il est mieux de ne prendre que l'id et le score ou garder les autres infos du joueur en stock içi ???
        return info_tournament, self.id_with_score


    def update_score(self):
        pass

    def sorted_players(self):
        sorted_players_scores = sorted(self.id_with_score, key= lambda x: x[1], reverse=True)
 #       print("Select players for match : ", sorted_players_scores)
        return sorted_players_scores


    def run(self):
        self.get_players()
        print("Run")

        for number in range(ROUND_NUMBER):
           print("number :", number)
           round = Round("Round" + str(number +1))
           print("round : ", round)
           matchs = 4
           o = 0

           """ Trouver comment créer automatiquement les matchs en leurs donnant 2 joueurs et leurs score en entrée de la classe Match"""
           for match in range(matchs):
               print("TTTEST", o, self.sorted_players())
               round.list_matchs.append(match)
               #print("Liste matchs :", round.list_matchs)

               o += 1







