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
        self.players: List[Player] = []  # !!! demander si le List[Player] change vraiment quelque chose ??!!!
 #       self.list_players = [] # le joueur + le score du tournoi
  #      self.player_with_score = [] # le joueur + le score du match


    def get_players(self):
        player_info = PlAYERS
        for i in player_info:
            player = Player(i[0], i[1], i[2], i[3])
            self.players.append(player)
#            self.list_players.append([player.name, player.first_name, player.date_birth, player.id_chess])

#        print("Print - get_player dans Controller - Len list_player :", len(self.list_players))
 #       print("NOOUVELLE LISTE = ", self.players)

    def __str__(self):
        return f"test info du joueur dans controlleur {self.players}"



    def new_tournament(self):
        info_tournament = Tournament("Tournoi des Sorciers", "15 juillet", "Poudlard")
   #     info_tournament.list_players = self.players
#        print(info_tournament)
        score = 0
        for player in self.players:
            info_tournament.list_players.append([player, score])
 #       print(self.player_with_score)

        return info_tournament


    def new_round(self, tournament):
        for round in range(ROUND_NUMBER):
            init_round = Round("Round " + str(round +1))
            tournament.list_rounds.append(init_round)
            if init_round.name_round == "Round 1":
                random.shuffle(tournament.list_players)
                players = tournament.list_players
 #               print("PREMIER ROUND", players)
            else:
                # Trouver comment faire en sorte que les joueurs ne rejouent pas direct entre eux
                players = sorted(tournament.list_players, key= lambda x: x[1], reverse=True)
            #    print("PAS LE PREMIER ROUND", init_round.name_round, players)

            print("-- ", init_round.name_round, "--")
            print(players)
            for player in range(0, len(players), 2):
                random.shuffle(MATCH_SCORE)
                player1 = players[player][0]
                score1 = MATCH_SCORE[0][0]
                player2 = players[player +1][0]
                score2 = MATCH_SCORE[0][1]
                match = Match(player1, score1, player2, score2)
                init_round.list_matchs.append(match)
 #               print("PLAYER 1 = ", player1, "score 1 = ", score1,"\nPLAYER 2 = ", player2, "score 2 = ", score2)
      #          print(match.result_match)
    #        print("Liste des matchs = ", init_round.list_matchs)
            self.result_round(init_round.list_matchs, tournament)
        return


    def result_round(self, round, tournament):
        for match in round:
            print("Resultat de match", match)
            for player in tournament.list_players:
                if player[0] == match.player1:
                    player[1] += match.score1
                elif player[0] == match.player2:
                    player[1] += match.score2
 #               print(player[0], player[1], match.player1, match.player2)
        print("Resultat du round : \n",sorted(tournament.list_players, key= lambda x: x[1], reverse=True))
        self.show_winner(tournament)

    def show_winner(self, tournament):
        print("Voir le vainqueur")git a
        print(tournament.list_players[0])
        sorted_final = sorted(tournament.list_players, key= lambda x: x[1], reverse=True)
        print("Classement final : ")
        for player in sorted_final:
            print("Joueur :",player[0],"score de :", player[1])

      #  print("Resultat du tournoi !!!!!! : \n", sorted(self.players, key=lambda x: x[5], reverse=True))

    def run(self):
        self.get_players()
        print("Run")
        tournament = self.new_tournament()

        self.new_round(tournament)









    #    print(new_round)







