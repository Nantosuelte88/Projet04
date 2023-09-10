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

    def menu(self):
        while True:
            response = self.view.menu()
            print("Print du MENU", response)
            if response == "1":
                print("choix 1 - ajouter un joueur")
                self.get_players()
            elif response == "2":
                print("choix 2 - ajouter un tournoi")
                self.new_tournament()
            elif response == "3":
                print("choix 3 - choisir un tournoi")
                if self.tournaments:
                    tournament = self.select_tournament(self.tournaments)

                    # revoir correspondance entre tournoi

                    print("Choisir les joueurs")

                    if self.players:
                        print(self.players)
                        players = self.view.choose_players(self.players)
                        if players:
                            print("il y a des joueurs")
                            self.initiate_tournament(tournament, players)
                    else:
                        print("aucun joueurs enregistrés")
                        # faire boucle pour enregistrer les joueurs ou en choisir si ils existent !!!!!

                else:
                    print("Pas de tournoi enregistré")
            elif response == "4":
                print("choix 4 - quitter le menu")
                break


    def get_players(self):
        """
        player_info = PlAYERS
        for i in player_info:
            player = Player(i[0], i[1], i[2], i[3])
            self.players.append(player)
        """
        # Avec la vue
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
        return self.tournaments

    def select_tournament(self, tournaments):
        name_tournament = self.view.choose_tournament(self.tournaments)
        for tournament in tournaments:
            if name_tournament == tournament.name_tournament:
                print("NOM CORRESPONDANT !!!!! ", name_tournament, "=", tournament.name_tournament)
                return tournament
            else:
                print("NOPE pas de correspondance")

    def select_players(self):
        list_players = self.view.choose_players(self.players)
        print("PRINT SELF_PLAYYYYYERS : \n", list_players)
        for player,index in list_players:
            print("PRINT dans methode select_player, player =", player)
            print(self.players, self.players[0], self.players[0].name)
        # AJOUTER LES JOUEURS DANS tournament.list_players et faire un return

    def initiate_tournament(self, tournament, players):
        print("Methode select tournament OK \n", tournament)
        score_tournament = 0
        for player in players:
            tournament.list_players.append([player, score_tournament])
        print("LE tournoi =", tournament.name_tournament, "les joueurs selectionnés =\n", tournament.list_players)
        statut_tournament = False
        play = self.view.play_game(tournament)
        print("view play game")
        if play:
            print("OUI")
            statut_tournament = True
            self.new_round(tournament)
        else:
            print("NON")

    def new_round(self, tournament):
        for round in range(ROUND_NUMBER):
            init_round = Round("Round " + str(round +1))
            tournament.list_rounds.append(init_round)

            if init_round.name_round == "Round 1":
                random.shuffle(tournament.list_players)
                players = tournament.list_players

            else:
                players = sorted(tournament.list_players, key=lambda x: x[1], reverse=True)
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
            response_view = self.view.next_round(round)
            if response_view:
                print("Reponse vraie", round)
            elif not response_view:
                print("Reponse Fausse", round)
                break

        print("après boucle response view")
        # mettre le classement à la fin seulement
        self.show_winner(tournament)
        return

    def result_round(self, round, tournament):
        for match in round:
            print("Resultat de match", match)
            for player in tournament.list_players:
                if player[0] == match.player1:
                    player[1] += match.score1
                elif player[0] == match.player2:
                    player[1] += match.score2

    def show_winner(self, tournament):
        sorted_final = sorted(tournament.list_players, key= lambda x: x[1], reverse=True)
        print("\n\n -- Classement final -- \n")
        for player in sorted_final:
            pass
            print("Joueur :",player[0],"score de :", player[1], "\n")

    def run(self):
        self.menu()
        print("Run")

