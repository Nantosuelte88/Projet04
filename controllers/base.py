from typing import List

from models.player import Player
from models.tournament import Tournament
from models.match import Match
from models.round import Round

from dataplayers import PlAYERS

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
        self.player_with_score = []


    def get_players(self):
        player_info = PlAYERS
        for i in player_info:
            player = Player(i[0], i[1], i[2], i[3])
            self.players.append(player)
            self.list_players.append([player.name, player.first_name, player.date_birth, player.id_chess])
#        print("Print - get_player dans Controller - Len list_player :", len(self.list_players))


    def __str__(self):
        return f"test info du joueur dans controlleur {self.list_players}"



    def new_tournament(self):
        info_tournament = Tournament("Tournoi des Sorciers", "15 juillet", "Poudlard")
        info_tournament.list_players = self.list_players
#        print(info_tournament)
        score = 0
        for player in self.list_players:
            self.player_with_score.append([player, score])
 #       print(self.player_with_score)
        # verifier si il est mieux de ne prendre que l'id et le score ou garder les autres infos du joueur en stock içi ???
        return info_tournament, self.player_with_score


    def update_score(self):
        pass


    def new_round(self):
        for round in range(ROUND_NUMBER):
            init_round = Round("Round " + str(round +1))
            print(init_round.name_round)
            if init_round.name_round == "Round 1":
                players = self.player_with_score
                random.shuffle(players)
            #    print("PREMIER ROUND", players)
            else:
                # Trouver comment faire en sorte que les joueurs ne rejouent pas direct entre eux
                players = sorted(self.player_with_score, key= lambda x: x[1], reverse=True)
            #    print("PAS LE PREMIER ROUND", init_round.name_round, players)

            for i in range(0, len(players), 2):
                random.shuffle(MATCH_SCORE)
                score1_match = MATCH_SCORE[0][0]
                score2_match = MATCH_SCORE[0][1]
                player1 = players[i][0]
                score1 = players[i][1] + (score1_match)
                player2 = players[i + 1][0]
                score2 = players[i + 1][1] + (score2_match)
                matchs = Match(player1, score1, player2, score2)
                #      print(matchs)
                init_round.list_matchs.append(matchs)
   #             print(matchs)
      #      print("PRINT liste des maths dans init_round", init_round.list_matchs)
            print("Résultat du", init_round.name_round)
            self.result_round(init_round.list_matchs)
 #           self.update_score_round(init_round)
        return init_round #ne retourne que le PREMIER ROUND !!! ATTENTION !!


    def result_round(self, round):
   #     player_score_tournament = [list(player) for player in self.player_with_score] # pour créer un liste à part
        for match in round:
            print("\nMatch = ", match.result_match)
            if match.score1 == 1:
                print("Le gagnant est p1", match.player1[0], match.player1[1])
                for i, player in enumerate(self.player_with_score):
                    if player[0] == match.player1:
                        self.player_with_score[i] = (player[0], player[1] + 1)
           #             player_score_tournament[i] = (player[0], player[1] + 1)
                        print("Test nouvelle boucle", "\nPlayer with score = ", self.player_with_score[i], "\n")
                       # test_choix_du_joueur = self.player_with_score[] # comment lui indiquer de chercher dans les infos de ce joeur
         #               print("TCHUUUK correspondance PLAYER 1", match.player1,"TEST 1 :", test_choix_du_joueur, "TEEEEST :", test)
            elif match.score2 == 1:
                print("Le gagnant est p2", match.player2[0], match.player2[1])
                for i, player in enumerate(self.player_with_score):
                    if player[0] == match.player2:
                        self.player_with_score[i] = (player[0], player[1] + 1)
                        print("!!!! corresponcance PLAYER 2", match.player2,"TEST 2 :", self.player_with_score[i], "\n")

            else:
                if match.player1 or match.player2 == self.player_with_score:
                    print("LEs DEUX correspondent !!!", match.score1)
                print("Match nul pour ", match.player1[0], match.player1[1], "et ", match.player2[0], match.player2[1], "MAtch nul score = ", self.player_with_score)


            #       print("§§§§§§§§", result_round_scores,self.player_with_score)

      #      print(self.player_with_score)
      #          print("Le Gagnant est :", )
       #     elif match.score2 == 1:
         #       print("Bravo", match.player2)


    def update_score_round(self, round):
        pass



    def run(self):
        self.get_players()
        print("Run")

        self.new_tournament()

        self.new_round()








    #    print(new_round)







