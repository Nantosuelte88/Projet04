from typing import List

from models.player import Player
from models.tournament import Tournament
from models.match import Match
from models.round import Round


import json
import os
import random
from datetime import datetime

ROUND_NUMBER = 4
MATCH_SCORE = [(1, 0), (0.5, 0.5), (0, 1)]

file_path_tournament = "data/tournament.json"
file_path_players = "data/players.json"


def file_json_player():
    if os.path.exists(file_path_players):
        print("le fichier player.json existe")
        if os.path.getsize(file_path_tournament) > 0:
            with open(file_path_players, "r") as my_file:
                current_players = json.load(my_file)
        else:
            current_players = {"players": {}}
    else:
        current_players = {"players": {}}
    return current_players


def search_tournaments_json():
    if os.path.exists(file_path_tournament):
        if os.path.getsize(file_path_tournament) > 0:
            with open(file_path_tournament, "r") as my_file:
                tournament_data = json.load(my_file)
        else:
            tournament_data = {"tournament": {}}
    else:
        tournament_data = {"tournament": {}}
    return tournament_data


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
                player = self.get_players()
                if player:
                    print("Joueur enregistré dans le fichier")
                else:
                    print("Erreur, merci de recommencer")
            elif response == "2":
                tournament = self.new_tournament()
                if not tournament:
                    break
                elif tournament:
                    self.add_player_in_tournament(tournament)
                    self.initiate_tournament(tournament)

            elif response == "3":
                self.select_tournament()

            elif response == "4":
                self.modification_player()

            elif response == "5":
                self.show_players()
            elif response == "6":
                self.show_tournaments()
            elif response == "7":
                break

    def show_players(self):
        players = file_json_player()
        print("Quoi encore ?", players)
        sorted_players = sorted(players["players"].values(), key=lambda x: x["name"])
        self.view.show_players(sorted_players)

    def show_tournaments(self):
        tournaments = search_tournaments_json()
        print(tournaments)
        self.view.show_tournaments(tournaments)

    def get_players(self):
        current_players = file_json_player()
        player_info = self.view.prompt_for_player()

        dict_player = {
            "name": player_info[0],
            "first_name": player_info[1],
            "date_birth": player_info[2],
            "id_chess": player_info[3],
        }

        next_available_key = str(len(current_players["players"]) + 1)
        current_players["players"][next_available_key] = dict_player
        with open(file_path_players, "w") as my_file:
            json.dump(current_players, my_file, indent=4)

        return player_info

    def new_tournament(self):
        tournament_data = search_tournaments_json()
        tournament_info_view = self.view.prompt_for_tournament()
        description = self.view.description()
        date_debut = datetime.now()
        format_date = date_debut.strftime("%d/%m/%Y-%H:%M:%S")
        tournament = Tournament(tournament_info_view[0],
                                tournament_info_view[1],
                                format_date,
                                description,
                                ROUND_NUMBER)
        tournament.status = True
        self.tournaments.append(tournament)

        new_tournament = {
            "name_tournament": tournament_info_view[0],
            "locality": tournament_info_view[1],
            "start_date": format_date,
            "end_date": None,
            "number_rounds": ROUND_NUMBER,
            "list_rounds": [],
            "list_players": [],
            "description": description
            }

        next_available_key = str(len(tournament_data["tournament"]) + 1)
        tournament_data["tournament"][next_available_key] = new_tournament
        with open(file_path_tournament, "w") as my_file:
            json.dump(tournament_data, my_file, indent=4)

        return tournament

    def select_tournament(self):
        check = False
        found_tournament = []
        tournaments_json = search_tournaments_json()
        while True:
            name_tournament = self.view.choose_tournament(check)
            for tournament_key in tournaments_json:
                tournament_info = tournaments_json[tournament_key]
                for key, value in tournament_info.items():
                    if value["name_tournament"] == name_tournament:
                        found_tournament.append(value)
                        break
            if len(found_tournament) == 1:
                break
            else:
                check = True

        self.view.show_tournament(found_tournament[0])

        # Instanciation du tournoi
        tournament = Tournament(found_tournament[0]["name_tournament"],
                                found_tournament[0]["locality"],
                                found_tournament[0]["start_date"],
                                found_tournament[0]["description"],
                                found_tournament[0]["number_rounds"]
                                )

        current_players = file_json_player()
        players_json = current_players["players"]
        players_info = found_tournament[0]["list_players"]
        for player_id in players_info:
            score_tournament = player_id[0]["score_tournament"]
            for players, players_info in players_json.items():
                if player_id[0]["id_chess"] == players_info["id_chess"]:
                    # Instanciation du joueur
                    player = Player(players_info["name"],
                                    players_info["first_name"],
                                    players_info["date_birth"],
                                    players_info["id_chess"])
                    tournament.list_players.append([player, score_tournament])

        tournament.list_rounds = found_tournament[0]["list_rounds"]

        self.tournaments.append(tournament)

        if len(tournament.list_rounds) == tournament.number_rounds:
            check_tournament = False
            print("!!!!! status tournament", tournament.status)
            self.view.continue_tournament(tournament.name_tournament, check_tournament)
            self.show_winner(tournament)
        elif len(tournament.list_rounds) < tournament.number_rounds:
            check_tournament = True
            print("!!!!! status tournament", tournament.status)
            ask_user = self.view.continue_tournament(tournament.name_tournament, check_tournament)
            if ask_user:
                if not tournament.list_players:
                    players = self.add_player_in_tournament(tournament)
                    if players:
                        self.new_round(tournament)
                else:
                    self.new_round(tournament)

        return tournament

    def select_player(self):
        current_players = file_json_player()
        players_json = current_players["players"]
        check = False

        while True:
            players_selected = []
            no_player = []
            found_name = []
            good_player = []
            print("Verif de check avant ", check)
            player_name = self.view.show_player(check)
            print("Verif de check apres", check)

            for player in players_json:
                player_index = players_json[player]
                if player_name == player_index["name"]:
                    found_name.append(player_index)
                else:
                    no_player.append(player)

            if len(found_name) > 1:
                print("BUUUUG", player_name)
                print("found name", found_name)
                check_player = self.view.choose_players(found_name)
                print("check player", check_player)
                for player_details in players_json.values():
                    print("player_details", player_details)
                    if check_player == player_details:
                        print(check_player, "-", player_details)
                        # Attention, parfois il renvoie un joueur inconnu ?!!!!
                        good_player.append([player_details])
                        print(good_player)
                    else:
                        no_player.append(player_details)
            elif len(found_name) == 1:
                good_player.append(found_name)

            if len(no_player) == len(players_json):
                check = True
                print("??", no_player)
                print(players_json)
            else:
                check = False

            if not check:
                if len(good_player) == 1:
                    players_selected.append(good_player[0][0])
                    break
            else:
                print("bug ?", found_name)
                print(players_selected)
                print(good_player)

        return players_selected, check

    def ask_for_players(self, tournament, peers):
        new_player = True
        while True:
            if tournament.list_players:
                print("paire ou non ?", len(tournament.list_players))
                print(peers)
                ask_for_more_players = self.view.add_player_in_tournament(tournament.list_players, peers)
                if ask_for_more_players:
                    new_player = True
                    print(ask_for_more_players)
                    player = self.select_player()
                    print("PLAYER", player)
                    return player, new_player
                else:
                    new_player = False
                    print(ask_for_more_players)
                    return new_player
            else:
                player = self.select_player()
                return player, new_player

    def add_player_in_tournament(self, tournament):
        current_players = file_json_player()
        players_json = current_players["players"]
        score_tournament = 0
        peers = False

        while True:
            if (len(tournament.list_players) % 2) == 0:
                peers = True
            else:
                peers = False
            add_players_json = []
            ask_player = self.ask_for_players(tournament, peers)

            if not ask_player:
                if peers:
                    break
            else:
                player = ask_player[0]
                new_player = ask_player[1]
                name = player[0][0]["name"]
                id_chess = player[0][0]["id_chess"]

                for players_id, players_info in players_json.items():
                    if name == players_info["name"] and id_chess == players_info["id_chess"]:
                        player_dict = Player(players_info["name"],
                                             players_info["first_name"],
                                             players_info["date_birth"],
                                             players_info["id_chess"])
                        # Ajout des joueurs dans la liste des joueurs du tournoi
                        tournament.list_players.append([player_dict, score_tournament])
                        dict_player = {
                            "id_chess": player_dict.id_chess,
                            "score_tournament": score_tournament
                        }
                        add_players_json.append(dict_player)
                        print("!!!!! BUG BUG BUGgreokpergkoegrko", add_players_json)

                        # ajout des joueurs dans le tournoi Json
                        tournaments_json = search_tournaments_json()
                        for tournament_key in tournaments_json:
                            tournament_info = tournaments_json[tournament_key]
                            for key, value in tournament_info.items():
                                if value["name_tournament"] == tournament.name_tournament:
                                    good_path = value["list_players"]
                                    good_path.append(add_players_json[0])
                                    with open(file_path_tournament, "w") as my_file:
                                        json.dump(tournaments_json, my_file, indent=4)
                print("bug quelque part ?", peers, ask_player, player, new_player)
        print("verification de fin du add player in tournament", peers, ask_player, tournament.list_players)
        return tournament

    def initiate_tournament(self, tournament):
        play = self.view.play_game(tournament)
        if play:
            tournament.status = True
            self.new_round(tournament)
        else:
            return None

    def modification_player(self):
        good_player = self.select_player()
        players_json = file_json_player()

        for player in players_json:
            if good_player[0][0] == players_json[player]:
                new_info = self.view.modification_player(players_json[player])
                if new_info[0] == "1":
                    players_json[player]["name"] = new_info[1]
                elif new_info[0] == "2":
                    players_json[player]["first_name"] = new_info[1]
                elif new_info[0] == "3":
                    players_json[player]["date_birth"] = new_info[1]
                elif new_info[0] == "4":
                    players_json[player]["id_check"] = new_info[1]
        with open(file_path_players, "w") as my_file:
            json.dump({"players": players_json}, my_file, indent=4)
        return None

    def update_description(self, tournament):
        description_view = self.view.description()
        if description_view:
            tournament.description = description_view

            tournaments_json = search_tournaments_json()
            for tournament_key in tournaments_json:
                tournament_info = tournaments_json[tournament_key]
                for key, value in tournament_info.items():
                    if value["name_tournament"] == tournament.name_tournament:
                        value["description"] = description_view
                        with open(file_path_tournament, "w") as my_file:
                            json.dump(tournaments_json, my_file, indent=4)
        else:
            return None

    def new_round(self, tournament):
        round_number = tournament.number_rounds
        new_round = []
        date_debut = datetime.now()
        format_date_debut = date_debut.strftime("%d/%m/%Y - %H:%M:%S")
        print("verif de round", len(tournament.list_rounds))
        round_actual = len(tournament.list_rounds)
        print(round_actual)
        if round_actual <= round_number:
            print("___", round_actual)
            for round_to_play in range(round_actual, round_number):
                init_round = Round("Round " + str(len(tournament.list_rounds) + 1))
                tournament.list_rounds.append(init_round)
                print("INIT ROUUUUUUND", init_round.name_round)
                print("round acutel", round_actual)

                if init_round.name_round == "Round 1":
                    random.shuffle(tournament.list_players)
                    players = tournament.list_players

                else:
                    players = sorted(tournament.list_players, key=lambda x: x[1], reverse=True)

                # verification de l'emplacement dans le tournoi json
                tournaments_json = search_tournaments_json()
                for tournament_key in tournaments_json:
                    tournament_info = tournaments_json[tournament_key]
                    for key, value in tournament_info.items():
                        if value["name_tournament"] == tournament.name_tournament:
                            good_path_round = value["list_rounds"]
                            new_round = {
                                "name_round": init_round.name_round,
                                "list_matches": [],
                                "start_time": format_date_debut,
                                "end_time": None
                            }
                            good_path_round.append(new_round)
                with open(file_path_tournament, "w") as my_file:
                    json.dump(tournaments_json, my_file, indent=4)

                for player in range(0, len(players), 2):
                    player1 = players[player][0]
                    player2 = players[player + 1][0]
                    scores = self.view.scores_match(player1, player2)
                    score1 = float(scores[0])
                    score2 = float(scores[1])
                    match = Match(player1, score1, player2, score2)

                    result_match = [
                        [player1.id_chess, score1],
                        [player2.id_chess, score2]
                    ]

                    init_round.list_matches.append(match)

                    # ajout du match dans la liste des rounds du tournoi Json
                    new_round["list_matches"].append({"result_match": result_match})
                    date_end = datetime.now()
                    format_date_end = date_end.strftime("%d/%m/%Y - %H:%M:%S")
                    new_round["end_time"] = format_date_end
                    with open(file_path_tournament, "w") as my_file:
                        json.dump(tournaments_json, my_file, indent=4)

                self.result_round(init_round.list_matches, tournament)

                if len(tournament.list_rounds) < round_number:
                    # Demande à l'utilisateur si il veut rejouer un round
                    response_view = self.view.next_round(round_actual)
                    if response_view:
                        print("Reponse vraie", round_actual)
                    elif not response_view:
                        print("Reponse Fausse", round_actual)
                        self.show_winner(tournament)
                        if not tournament.description:
                            self.update_description(tournament)
                            break
                elif len(tournament.list_rounds) == round_number:
                    print("tournoi fini")
                    tournament.status = False
                    self.show_winner(tournament)
                    tournaments_json = search_tournaments_json()
                    end_time_tournament = datetime.now()
                    format_end_time = end_time_tournament.strftime("%d/%m/%Y - %H:%M:%S")
                    tournament.end = end_time_tournament
                    for tournament_key in tournaments_json:
                        tournament_info = tournaments_json[tournament_key]
                        for key, value in tournament_info.items():
                            if value["name_tournament"] == tournament.name_tournament:
                                if not value["end_date"]:
                                    value["end_date"] = format_end_time
                                    with open(file_path_tournament, "w") as my_file:
                                        json.dump(tournaments_json, my_file, indent=4)

        return None

    def result_round(self, matches_round, tournament):
        # Mise à jour du score des joueurs
        for match in matches_round:
            print("Resultat de match", match)
            for player in tournament.list_players:
                if player[0] == match.player1:
                    player[1] += match.score1
                elif player[0] == match.player2:
                    player[1] += match.score2

        tournaments_json = search_tournaments_json()
        for tournament_key in tournaments_json:
            tournament_info = tournaments_json[tournament_key]
            for key, value in tournament_info.items():
                if value["name_tournament"] == tournament.name_tournament:
                    good_path_round = value["list_players"]
                    for player in tournament.list_players:
                        for player_info in good_path_round:
                            if player[0].id_chess == player_info["id_chess"]:
                                player_info["score_tournament"] = player[1]

        with open(file_path_tournament, "w") as my_file:
            json.dump(tournaments_json, my_file, indent=4)
        return None

    def show_winner(self, tournament):
        sorted_final = sorted(tournament.list_players, key=lambda x: x[1], reverse=True)
        self.view.show_final_players(sorted_final, tournament.status)
        return None

    def run(self):
        self.menu()
        print("Run")
        return None
