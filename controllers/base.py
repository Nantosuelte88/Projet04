from typing import List

from models.player import Player
from models.tournament import Tournament
from models.match import Match
from models.round import Round
from views.tournamenentview import View

from dataplayers import PlAYERS

import random
import datetime
from datetime import datetime

ROUND_NUMBER = 4
MATCH_SCORE = [(1, 0), (0.5, 0.5), (0, 1)]
class Controller:
    """ Le Contrôleur """

    def __init__(self, view):

        self.view = view

        self.players: List[Player] = []

        self.tournaments: List[Tournament] = []


    def get_players(self):
        """
        player_info = PlAYERS
        for i in player_info:
            player = Player(i[0], i[1], i[2], i[3])
            self.players.append(player)
        """

        # Avec la vue
   #     list_prompt_players = []
        player_info = self.view.prompt_for_player()
        print(player_info)
        for player in player_info:
            player = Player(player[0], player[1], player[2], player[3])
            self.players.append(player)
        print(self.players)
        return self.players



    def new_tournament(self):

        tournament_info_view = self.view.prompt_for_tournament()
        for tournament in tournament_info_view:
      #      date = datetime.date.today()
            date = "04 Septembre"
            tournament = Tournament(tournament[0], tournament[1], date)
            self.tournaments.append(tournament)
        print("Print self tournaments = ", self.tournaments, "fin print self tournaments")
        self.select_tournament(self.tournaments)
        return self.tournaments



    def select_tournament(self, tournaments):
        pass


    def new_round(self, tournament):
        for round in range(ROUND_NUMBER):
            init_round = Round("Round " + str(round +1))
            tournament.list_rounds.append(init_round)

            if init_round.name_round == "Round 1":
                random.shuffle(tournament.list_players)
                players = tournament.list_players

            else:
                players = sorted(tournament.list_players, key= lambda x: x[1], reverse=True)
            print("-- ", init_round.name_round, "--")
            for player in range(0, len(players), 2):
                random.shuffle(MATCH_SCORE)
                player1 = players[player][0]
                score1 = MATCH_SCORE[0][0]
                player2 = players[player +1][0]
                score2 = MATCH_SCORE[0][1]
                match = Match(player1, score1, player2, score2)
                init_round.list_matchs.append(match)
            self.result_round(init_round.list_matchs, tournament)
        self.show_winner(tournament)
        return


    def result_round(self, round, tournament):
        for match in round:
 #           print("Resultat de match", match)
            for player in tournament.list_players:
                if player[0] == match.player1:
                    player[1] += match.score1
                elif player[0] == match.player2:
                    player[1] += match.score2

    def show_winner(self, tournament):
        sorted_final = sorted(tournament.list_players, key= lambda x: x[1], reverse=True)
  #      print("\n\n -- Classement final -- \n")
        for player in sorted_final:
            pass
 #           print("Joueur :",player[0],"score de :", player[1], "\n")


    def run(self):
        self.get_players()
        print("Run")

        tournament = self.new_tournament()

        print(" print dans run", tournament)

  #      self.new_round(tournament)









    #    print(new_round)







