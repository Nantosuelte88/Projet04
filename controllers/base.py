from typing import List

from models.player import Player
from models.tournament import Tournament
from models.match import Match
from models.round import Round

from data import PlAYERS

import random

ROUND_NUMBER = 4
MATCH_SCORE = [(1, 0), (0.5, 0.5), (0, 1)]
MATCHS = 4
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
#        print(self.id_with_score)
        # verifier si il est mieux de ne prendre que l'id et le score ou garder les autres infos du joueur en stock içi ???
        return info_tournament, self.id_with_score


    def update_score(self):
        pass

    def sorted_players(self):
        sorted_players_scores = sorted(self.id_with_score, key= lambda x: x[1], reverse=True)
 #       print("Select players for match : ", sorted_players_scores)
        return sorted_players_scores


    def new_round(self):
        init_round = Round("Round")
        print("ROUND : Liste des Matchs = ", init_round.list_matchs)
        players = self.sorted_players()
        #    print("Print system_matchs:", players)
        for i in range(0, len(players), 2):
            player1 = players[i][0]
            score1 = players[i][1]
            player2 = players[i + 1][0]
            score2 = players[i + 1][1]
            print("player1 :", player1, "score1: ", score1, "player2", player2, "score2 :", score2)
            matchs = Match(player1, score1, player2, score2)
            #      print(matchs)
            init_round.list_matchs.append(matchs)

        print(init_round)
        result_match = []
        for p in init_round.list_matchs:
            random.shuffle(MATCH_SCORE)
            score1 = MATCH_SCORE[0][0]
            score2 = MATCH_SCORE[0][1]
            print("tututu", score1, score2)
        return init_round


    def result_matchs(self, matchs):
        for match in matchs:
            print(match)




    def run(self):
        self.get_players()
        print("Run")

        self.new_tournament()

        self.new_round()

        self.update_score()
        self.sorted_players()




    #    print(new_round)







