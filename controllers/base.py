from typing import List

from models.player import Player
from models.tournament import Tournament
from models.match import Match
from models.round import Round
from views.tournamenentview import View


import json
import os
import random
import datetime
from datetime import datetime

ROUND_NUMBER = 4
MATCH_SCORE = [(1, 0), (0.5, 0.5), (0, 1)]

file_path_tournament = "data/tournament.json"
file_path_players = "data/players.json"


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
                player = self.get_players()
                if player:
                    print("Joueur enregistré dans le fichier")
                else:
                    print("Erreur, merci de recommencer")
            elif response == "2":
                print("choix 2 - créer un tournoi")
                tournament = self.new_tournament()
                if not tournament:
                    break
                elif tournament:
                    print("retour menu- tournoi marche", tournament)
                    self.select_players(tournament)
                    print("RETOUR dans le menu, select_players -> joueur dans la liste du tournoi :",
                          tournament.name_tournament, "\n", tournament.list_players)
                    self.initiate_tournament(tournament)

            elif response == "3":
                print("choix 3 - rechercher un tournoi existant")
                tournament = self.select_tournament(self.tournaments)
                print("RETOUR MENU ->", tournament)

            elif response == "4":
                print("choix 4 - Modifier un joueur")
                self.modification_player()

            elif response == "5":
                print("choix 5 - voir les joueurs")
                self.show_players()
            elif response == "6":
                print("choix 6 - quitter le menu")
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
        if os.path.exists(file_path_players):
            print("le fichier player.json existe")
            if os.path.getsize(file_path_tournament) > 0:
                with open("data/players.json", "r") as my_file:
                    current_players = json.load(my_file)
            else:
                current_players = {"players": {}}
        else:
            current_players = {"players": {}}
        return current_players

    def show_players(self):
        players = self.file_json_player()
        sorted_players = sorted(players["players"].values(), key=lambda x: x["name"])
        self.view.show_players(sorted_players)

    def get_players(self):
        current_players = self.file_json_player()
        player_info = self.view.prompt_for_player()
        print(player_info)

        print("AVANT JSON")
        dict_player = {
            "name": player_info[0],
            "first_name": player_info[1],
            "date_birth": player_info[2],
            "id_chess": player_info[3],
        }

        next_available_key = str(len(current_players["players"]) + 1)
        current_players["players"][next_available_key] = dict_player
        with open("data/players.json", "w") as my_file:
            json.dump(current_players, my_file, indent=4)

        print("APRES JSON")
        return player_info

    def search_tournaments_json(self):
        if os.path.exists(file_path_tournament):
            print("le fichier tournament.json existe")
            if os.path.getsize(file_path_tournament) > 0:
                with open("data/tournament.json", "r") as my_file:
                    tournament_data = json.load(my_file)
            else:
                tournament_data = {"tournament": {}}
        else:
            tournament_data = {"tournament": {}}
        return tournament_data

    def new_tournament(self):
        tournament_data = self.search_tournaments_json()
        tournament_info_view = self.view.prompt_for_tournament()
        description = self.view.description()
        print("Print de description == ", description)
     #   date = datetime.datetime.now().strftime("%d.%m.%Y;%H:%M:%S")
        print("ENTIER:", tournament_info_view, "+[0]", tournament_info_view[0], "+[1]", tournament_info_view[1])
   #     date = datetime.date.today()
        date = "04 Septembre"
        tournament = Tournament(tournament_info_view[0], tournament_info_view[1], date, description, ROUND_NUMBER)
        self.tournaments.append(tournament)
        print(tournament_data)
        print("AVANT if tournament, créeation tournoi dans fichier JSON")

        new_tournament = {
            "name_tournament": tournament_info_view[0],
            "locality": tournament_info_view[1],
            "start_date": date,
            "end_date": None,
            "number_rounds": ROUND_NUMBER,
            "list_rounds": [],
            "list_players": [],
            "description": description
            }

        next_available_key = str(len(tournament_data["tournament"]) + 1)
        tournament_data["tournament"][next_available_key] = new_tournament
        with open("data/tournament.json", "w") as my_file:
            json.dump(tournament_data, my_file, indent=4)

        print("APRES JSON - tournoi")
        print("Print self tournaments = ", self.tournaments, "fin print self tournaments")
        return tournament

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
                file_object = open("data/players.json", "r")
                json_content = file_object.read()
                json_dict = json.loads(json_content)
                players = json_dict["players"]

        return players

    def select_players(self, tournament):
        print("TEST select players, tournoi :", tournament)
        print("PRINT test du nom du t-ournoi, bug ou pas ? --- >", tournament.name_tournament)
        score_tournament = 0
        players_json = self.search_players_json()
        player_name = self.view.add_player_in_tournament()
        players_selected = []
        add_players_json = []

        print("!!!!!TEST!!!!!", players_json)
        u = 0

        for name in player_name:
            found_name = []
            for index in players_json:

                print("print index =", index)
                player_index = players_json[index]
                print("player index=", player_index)
                print(u, "name ?", player_index["name"])
                u +=1
                if name == player_index["name"]:
                    print("correspondance!", name, " et ", player_index["name"])
                    found_name.append(index)
                else:
                    print("ne correspond pas", name, " et ", player_index["name"])

            # Vérification des doublons de noms de joueurs
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

            # Instanciation de la classe Player, des joueurs selectionnés, depuis fichier JSon
            for index in players_json:
                player_index = players_json[index]
                print("test de nom", player_index["name"])
                if name == player_index["name"]:
                    print("instanciation de :", name)
                    player = Player(player_index["name"],
                                    player_index["first_name"],
                                    player_index["date_birth"],
                                    player_index["id_chess"])
                    # Ajout des joueurs dans la liste des joueurs du tournoi
                    tournament.list_players.append([player, score_tournament])
                    dict_player = {
                            "id_chess": player_index["id_chess"],
                            "score_tournament": score_tournament
                        }
                    add_players_json.append(dict_player)
            print(add_players_json)
        # ajout des joueurs dans le tournoi Json
        tournaments_json = self.search_tournaments_json()
        for tournament_key in tournaments_json:
            tournament_info = tournaments_json[tournament_key]
            for key, value in tournament_info.items():
                print(value["name_tournament"])
                if value["name_tournament"] == tournament.name_tournament:
                    print("LE BON TOURNOI", tournament.name_tournament)
                    print(value["list_players"])
                    good_path = value["list_players"]
                    good_path.extend(add_players_json)
                    with open("data/tournament.json", "w") as my_file:
                        json.dump(tournaments_json, my_file, indent=4)
                else:
                    print("PAS LE BON TOURNOI", tournament.name_tournament)

        return tournament

    def initiate_tournament(self, tournament):
        # faire instanciation du tournoi ici en choissisant les options
        # -> si nouveau tournoi = ne pas faire la vue et l'instancier directement
        # sinon faire choisir quel tournoi
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

    def modification_player(self):
        check = False
        no_player = []
        found_name = []
        good_player = []

        # Prochaine version du select joueur
        while True:
            u = 0
            player_name = self.view.show_player(check)
            players_json = self.search_players_json()
            for player in players_json:
                print("print index =", player)
                player_index = players_json[player]
                print("player index=", player_index)
                print(u, "name ?", player_index["name"])
                u += 1
                if player_name == player_index["name"]:
                    print("correspondance!", player_name, " et ", player_index["name"])
                    found_name.append(player_index)
                else:
                    no_player.append(player)

            if len(found_name) > 1:
                print("sup à 1 = ", len(found_name))
                check_player = self.view.choose_players(found_name)
                print("!!!", check_player, "!!!!", players_json)
                for player_details in players_json.values():
                    if check_player == player_details:
                        print("id correspondant", player_details["name"], player_details["first_name"],
                              player_details["id_chess"])
                        good_player.append(player_details)
                    else:
                        print("player non correspondant", check_player, "!=", player_details["name"])
                        no_player.append(player_details)
            elif len(found_name) == 1:
                print("egal à 1 = ", len(found_name))
                good_player.append(found_name)
            else:
                print("pas de joueur à ce nom")
                check = True

            if len(no_player) == len(players_json):
                print("joueur inconnu!", no_player)
                check = True
            else:
                print("le joueur est ok", no_player)
                break

        print("verif de check ->", check)
        if not check:
            print(good_player)
            if len(good_player) == 1:
                print("un seul joueur ok", good_player)
            elif len(good_player) > 1:
                print("plusieurs joueurs dedans", good_player)
        print("FIN BOUCLE MODIF\n joueur ? =", good_player[0][0])
        # Fin version select !!!
        p = 0
        for player in players_json:
            print(p, players_json[player])
            p +=1
            if good_player[0][0] == players_json[player]:
                print("bon joueur")
                new_info = self.view.modification_player(players_json[player])
                print(new_info)
                if new_info[0] == "1":
                    print("nouveau nom", new_info[1])
                    players_json[player]["name"] = new_info[1]
                elif new_info[0] == "2":
                    print("nouveau prenom", new_info[1])
                    players_json[player]["first_name"] = new_info[1]
                elif new_info[0] == "3":
                    print("nouvelle date de naissance", new_info[1])
                    players_json[player]["date_birth"] = new_info[1]
                elif new_info[0] == "4":
                    print("nouvel id", new_info[1])
                    players_json[player]["id_check"] = new_info[1]
            else:
                print("mauvais joueur")
        with open("data/players.json", "w") as my_file:
            json.dump(players_json, my_file, indent=4)
        print("fin de modif")

    def update_description(self, tournament):
        description_view = self.view.description()
        if description_view:
            tournament.description = description_view

            tournaments_json = self.search_tournaments_json()
            for tournament_key in tournaments_json:
                tournament_info = tournaments_json[tournament_key]
                for key, value in tournament_info.items():
                    print(value["name_tournament"])
                    if value["name_tournament"] == tournament.name_tournament:
                        print("LE BON TOURNOI", tournament.name_tournament)
                        value["description"] = description_view
                        with open("data/tournament.json", "w") as my_file:
                            json.dump(tournaments_json, my_file, indent=4)
                    else:
                        print("PAS LE BON TOURNOI", tournament.name_tournament)
        else:
            return None

    def new_round(self, tournament):

        new_round = []
        date_debut = "09/12/2121"
        date_end = "02/01/2122"
        for round in range(ROUND_NUMBER):
            init_round = Round("Round " + str(round +1))
            tournament.list_rounds.append(init_round)

            if init_round.name_round == "Round 1":
                random.shuffle(tournament.list_players)
                players = tournament.list_players

            else:
                players = sorted(tournament.list_players, key=lambda x: x[1], reverse=True)
            print("-- ", init_round.name_round, "--")

            # verification de l'emplacement dans le tournoi json
            tournaments_json = self.search_tournaments_json()
            for tournament_key in tournaments_json:
                tournament_info = tournaments_json[tournament_key]
                for key, value in tournament_info.items():
                    print(value["name_tournament"])
                    if value["name_tournament"] == tournament.name_tournament:
                        print("LE BON TOURNOI", tournament.name_tournament)
                        good_path_round = value["list_rounds"]
                        new_round = {
                            "name_round": init_round.name_round,
                            "list_matches": [],
                            "star_time": date_debut,
                            "end_time": date_end
                        }
                        print("!!!!!!! print init round", init_round.name_round)
                        good_path_round.append(new_round)
                        print("good_path", good_path_round)
                    else:
                        print("PAS LE BON TOURNOI", tournament.name_tournament)
            with open("data/tournament.json", "w") as my_file:
                json.dump(tournaments_json, my_file, indent=4)

            for player in range(0, len(players), 2):
  #              random.shuffle(MATCH_SCORE)
                player1 = players[player][0]
  #              score1 = MATCH_SCORE[0][0]
                player2 = players[player +1][0]
  #              score2 = MATCH_SCORE[0][1]
   #             match = self.play_match(player1, player2)
                scores = self.view.scores_match(player1, player2)
                score1 = float(scores[0])
                score2 = float(scores[1])
                print("Test View resultat de match\n"
                      "p1 =", player1, "score1 =", score1, "\n",
                      "p2 =", player2, "score2 =", score2)
                match = Match(player1, score1, player2, score2)

                result_match = [
                    [player1.id_chess, score1],
                    [player2.id_chess, score2]
                ]

                init_round.list_matches.append(match)

                # ajout du match dans la liste des rounds du tournoi Json
                new_round["list_matches"].append({"result_match": result_match})
                with open("data/tournament.json", "w") as my_file:
                    json.dump(tournaments_json, my_file, indent=4)

            self.result_round(init_round.list_matches, tournament)

            if round +1 != ROUND_NUMBER:
                print("pas le meme Round =", round)
            else:
                print("FIN ddes rounds ?!", round)

            # Demande à l'utilisateur si il veut rejouer un round
            response_view = self.view.next_round(round)
            if response_view:
                print("Reponse vraie", round)
            elif not response_view:
                print("Reponse Fausse", round)
                if not tournament.description:
                    self.update_description(tournament)
                break

        print("après boucle response view")
        # mettre le classement à la fin seulement
  #      self.show_winner(tournament)
        return

    def play_match(self, player1, player2):
        pass

    def result_round(self, round, tournament):
        # Mise à jour du score des joueurs
        for match in round:
            print("Resultat de match", match)
            for player in tournament.list_players:
                if player[0] == match.player1:
                    player[1] += match.score1
                elif player[0] == match.player2:
                    player[1] += match.score2

        tournaments_json = self.search_tournaments_json()
        for tournament_key in tournaments_json:
            tournament_info = tournaments_json[tournament_key]
            for key, value in tournament_info.items():
                print(value["name_tournament"])
                if value["name_tournament"] == tournament.name_tournament:
                    print("LE BON TOURNOI", tournament.name_tournament)
                    good_path_round = value["list_players"]
                    for player in tournament.list_players:
                        for player_info in good_path_round:
                            if player[0].id_chess == player_info["id_chess"]:
                                player_info["score_tournament"] = player[1]

        with open("data/tournament.json", "w") as my_file:
            json.dump(tournaments_json, my_file, indent=4)

    def show_winner(self, tournament):
        sorted_final = sorted(tournament.list_players, key= lambda x: x[1], reverse=True)
        print("\n\n -- Classement final -- \n")
        for player in sorted_final:
            pass
            print("Joueur :",player[0],"score de :", player[1], "\n")

    def run(self):
        self.menu()
        print("Run")

