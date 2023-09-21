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

file_path_tournament = "data/tournament.json"
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
                print("choix 1 - crée un nouveau joueur")
                new_players = self.get_players()
            elif response == "2":
                print("choix 2 - créer un tournoi")
                tournament = self.new_tournament()
                if not tournament:
                    break
                elif tournament:
                    print("retour menu- tournoi marche", tournament)
                    self.select_players(tournament)
                    print("RETOUR dans le menu, select_players -> joueur dans la liste du tournoi :", tournament.name_tournament, "\n", tournament.list_players)

            elif response == "3":
                print("choix 3 - rechercher un tournoi existant")
                tournament = self.select_tournament(self.tournaments)
                print("RETOUR MENU ->", tournament)


            elif response == "4":
                print("choix 4 - quitter le menu")
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

    def file_json_player(self):
        pass

    def get_players(self):
        new_player = []
        if os.path.exists(file_path_players):
            print("le fichier player.json existe")
            if os.path.getsize(file_path_tournament) > 0:
                with open("players.json", "r") as my_file:
                    current_players = json.load(my_file)
            else:
                current_players = []
        else:
            current_players = []

        player_info = self.view.prompt_for_player()
        print(player_info)
        for player in player_info:
            player = Player(player[0], player[1], player[2], player[3])
            self.players.append(player)
            print("AVANT JSON")
            with open("players.json", "r") as my_file:
                current_players = json.load(my_file)
            dict_player = {
                "name": player.name,
                "first_name": player.first_name,
                "date_birth": player.date_birth,
                "id_chess": player.id_chess,
            }
            new_player.append(dict_player)
            current_players.append(dict_player)

            with open("players.json", "w") as my_file:
                json.dump(current_players, my_file)

            print("APRES JSON")

        print(self.players)
        return self.players

    def search_tournaments_json(self):
        if os.path.exists(file_path_tournament):
            print("le fichier tournament.json existe")
            if os.path.getsize(file_path_tournament) > 0:
                file_object = open("tournament.json", "r")
                json_content = file_object.read()
                tournaments = json.loads(json_content)
                return tournaments

    def new_tournament(self):
        if os.path.exists(file_path_tournament):
            print("le fichier tournament.json existe")
            if os.path.getsize(file_path_tournament) > 0:
                with open("data/tournament.json", "r") as my_file:
                    tournament_data = json.load(my_file)
            else:
                tournament_data = {"tournament": {}}
        else:
            tournament_data = {"tournament": {}}

        tournament_info_view = self.view.prompt_for_tournament()
     #   date = datetime.datetime.now().strftime("%d.%m.%Y;%H:%M:%S")
        print("ENTIER:", tournament_info_view, "+[0]", tournament_info_view[0], "+[1]", tournament_info_view[1])
   #     date = datetime.date.today()
        date = "04 Septembre"
 #       tournament = Tournament(tournament_info_view[0], tournament_info_view[1], date)
 #       self.tournaments.append(tournament)
#        with open("tournament.json", "r") as my_file:
 #           current_tournament = json.load(my_file)
        print(tournament_data)
        print("AVANT if tournament, créeation tournoi dans fichier JSON")

        new_tournament = {
            "name_tournament": tournament_info_view[0],
            "locality" : tournament_info_view[1],
            "start_date": date,
            "list_rounds": [],
            "list_players": [],
            "description": None
            }

        next_available_key = str(len(tournament_data["tournament"]) + 1)
        tournament_data["tournament"][next_available_key] = new_tournament
        with open("data/tournament.json", "w") as my_file:
            json.dump(tournament_data, my_file, indent=4)

        print("APRES JSON - tournoi")
        print("Print self tournaments = ", self.tournaments, "fin print self tournaments")
        return None

    def select_tournament(self, tournaments):
        name_tournament = self.view.choose_tournament(self.tournaments)
        for tournament in tournaments:
            if name_tournament == tournament.name_tournament:
                print("NOM CORRESPONDANT !!!!! ", name_tournament, "=", tournament.name_tournament)
                return tournament
            else:
                print("NOPE pas de correspondance")

    def search_players_json(self):
        if os.path.exists(file_path_players):
            print("le fichier player.json existe")
            if os.path.getsize(file_path_tournament) > 0:
                file_object = open("players.json", "r")
                json_content = file_object.read()
                players = json.loads(json_content)
    #            with open("players.json", "r") as my_file:
     #               current_players = json.load(my_file)
      #              players = current_players
                return players

    def select_players(self, tournament):
        print("TEST select players, tournoi :", tournament)
        print("PRINT test du nom du t-ournoi, bug ou pas ? --- >", tournament.name_tournament)
        score_tournament = 0
        players_json = self.search_players_json()
        player_name = self.view.add_player_in_tournament()
        players_selected = []

        for name in player_name:
            found_name = []
            print(name)
            for player in players_json:
                print("!!print du nom du joeur :", player["name"])
                if player["name"] == name:
                    print("Correspondance du nom !", player["name"], player["first_name"], player["date_birth"], player["id_chess"])
                    found_name.append(player)
                else:
                    print("pas de correspondance", name)

            if len(found_name) > 1:
                print("sup à 1 = ", len(found_name))
                id_chess_view = self.view.choose_players(found_name)
                for player in players_json:
                    if id_chess_view == player["id_chess"]:
                        print("id correspondant", player["name"], player["first_name"], player["id_chess"])
                        players_selected.append(player)
            elif len(found_name) == 1:
                print("egal à 1 = ", len(found_name))
                players_selected.append(found_name)
            else:
                print("pas de joueur à ce nom")
            print("PRINT de le liste polayers dans select players = \n\n ->", players_selected)

        for players in players_selected:
            for player_json in players:
                print("test de nom", player_json["name"])
                player = Player(player_json["name"],
                                player_json["first_name"],
                                player_json["date_birth"],
                                player_json["id_chess"])
                tournament.list_players.append(player, score_tournament)

        return tournament



  #      for player in players:
   #         print("PRINT dans methode select_player, player =", player)
    #        print(self.players, self.players[0], self.players[0].name)
     #       tournament.list_players.append([player, score_tournament])

#        return tournament.list_players

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
                init_round.list_matches.append(match)
            self.result_round(init_round.list_matches, tournament)
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

