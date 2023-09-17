from typing import List

from models.player import Player
from models.tournament import Tournament
from models.match import Match
from models.round import Round
from views.tournamenentview import View

from dataplayers import PlAYERS

import json
import os
import random
import datetime
from datetime import datetime

ROUND_NUMBER = 4
MATCH_SCORE = [(1, 0), (0.5, 0.5), (0, 1)]

file_path_tournament = "tournament.json"
file_path_players = "players.json"


class Controller:
    """ Le Contrôleur """

    def __init__(self, view):

        self.view = view

        self.players: List[Player] = []
        self.tournaments: List[Tournament] = []

    def menu(self):
        while True:
            response = self.view.menu()
            if response == "1":
                print("choix 1 - démarrer un tournoi")
                tournament = self.new_tournament()
            elif response == "2":
                if self.tournaments:
                    print("slef.tournament", self.tournaments)
                    tournament = self.select_tournament(self.tournaments)
                    print("Choisir les joueurs")
                    choice_for_player = self.view.menu_players()
                    print(choice_for_player)
                    if choice_for_player == "1":
                        print("TEST CHOIX JOUEUR 1")
                        new_players = self.get_players()
                        players = self.select_players(tournament, new_players)
                        if players:
                            print("il y a des joueurs")
                            self.initiate_tournament(tournament, players)
                    elif choice_for_player == "2":
                        new_players = None
                        if self.players:
                            print(self.players)
                            players = self.select_players(tournament, new_players)
                            if players:
                                print("il y a des joueurs")
                                self.initiate_tournament(tournament, players)
                        else:
                            print("aucun joueurs enregistrés")
                            # faire boucle pour enregistrer les joueurs ou en choisir si ils existent !!!!!
                    elif choice_for_player == "3":
                        print("TEST choisir 8 joueurs au hasard")
                else:
                    print("PAS de tournoi enregistré.s")
            elif response == "3":
                print("choix 3 - quitter le menu")
                break

    def activ_tournament(self):
        pass
        """
        while True:

            if self.tournaments:
                print("print premier if menu")
                for tournament in self.tournaments:
                    print(tournament.name_tournament, "statut =", tournament.statut)
                    if tournament.statut:
                        print(tournament.name_tournament, "est actif")
                        tournament_is_activ = True
                        return tournament_is_activ, tournament
                    else:
                        print(tournament.name_tournament, "statut inactif")
                        return None
            else:
                print("print activ_tournament = pas de tournoi actif")
                return None
        """

    def get_players(self):
        """
        player_info = PlAYERS
        for i in player_info:
            player = Player(i[0], i[1], i[2], i[3])
            self.players.append(player)
        """
        if os.path.exists(file_path_players):
            print("le fichier player.json existe")
            if os.path.getsize(file_path_tournament) > 0:
                with open("players.json", "r") as my_file:
                    current_players = json.load(my_file)
            else:
                current_players = []
        else:
            current_players = []
        # Avec la vue
        player_info = self.view.prompt_for_player()
        print(player_info)
        for player in player_info:
            player = Player(player[0], player[1], player[2], player[3])
            self.players.append(player)
            print("AVANT JSON")
            with open("players.json", "r") as my_file:
                current_players = json.load(my_file)

            new_player = [player.name, player.first_name, player.date_birth, player.id_chess]
            current_players.append(new_player)

            with open("players.json", "w") as my_file:
                json.dump(current_players, my_file)

            print("APRES JSON")

        print(self.players)
        return self.players

    def new_tournament(self):
        if os.path.exists(file_path_tournament):
            print("le fichier tournament.json existe")
            if os.path.getsize(file_path_tournament) > 0:
                with open("tournament.json", "r") as my_file:
                    current_tournament = json.load(my_file)
            else:
                current_tournament = []
        else:
            current_tournament = []

        tournament_info_view = self.view.prompt_for_tournament()
     #   date = datetime.datetime.now().strftime("%d.%m.%Y;%H:%M:%S")
        for tournament in tournament_info_view:

       #     date = datetime.date.today()
            date = "04 Septembre"
            tournament = Tournament(tournament[0], tournament[1], date)
            self.tournaments.append(tournament)
            print("AVANT JSON - tournoi")
            print(tournament.name_tournament)
            new_tournament = [tournament.name_tournament, tournament.locality, date]
            current_tournament.append(new_tournament)

            with open("tournament.json", "w") as my_file:
                json.dump(current_tournament, my_file)

            print("APRES JSON - tournoi")
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

    def select_players(self, tournament, new_players):
        print("TEST select players, tournoi :", tournament, "new_players :", new_players)
        score_tournament = 0
        if not new_players:
            print("print, select players, pas des nouveaux joueurs")
            list_players = self.view.choose_players(self.players)
            print("PRINT SELF_PLAYYYYYERS : \n", list_players)

        else:
            print("print, select players, ce sont des nouveaux joueurs")
            list_players = new_players

        for player in list_players:
            print("PRINT dans methode select_player, player =", player)
            print(self.players, self.players[0], self.players[0].name)
            tournament.list_players.append([player, score_tournament])
        return tournament.list_players

        # AJOUTER LES JOUEURS DANS tournament.list_players et faire un return

    def initiate_tournament(self, tournament, players):
        print("Methode select tournament OK \n", tournament)
        print("LE tournoi =", tournament.name_tournament, "les joueurs selectionnés =\n", tournament.list_players)
        play = self.view.play_game(tournament)
        print("view play game")
        if play:
            print("OUI")
            tournament.statut = True
            self.new_round(tournament)
        else:
            print("NON")
            return None

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

