from datetime import datetime
from tabulate import tabulate


class View:

    def menu(self):

        while True:
            print("\n-------- MENU --------")
            choice = input("Que souhaitez-vous faire ?\n"
                           "1 - Créer un nouveau joueur \n"
                           "2 - Créer un nouveau tournoi\n"
                           "3 - Voir un tournoi\n"
                           "4 - Modifier un joueur\n"
                           "5 - Voir les joueurs\n"
                           "6 - Voir les tournois\n"
                           "7 - Quitter\n"
                           "---------------------- \n\n"
                           "Votre choix : ")
            if choice.isnumeric() and int(choice) <= 6:
                break
            elif choice.isnumeric() and int(choice) == 7:
                choose_quit = input("Attention, vous allez quitter le programme, valider votre choix ? O/N : ")
                if choose_quit.upper() == "O":
                    break
            else:
                print("\nMerci d'entrer une donnée valide")
        return choice

    def menu_tournament(self):
        pass

    def prompt_for_player(self):
        while True:
            while True:
                name = input("Nom du joueur: ")
                if name.isalpha():
                    break
                else:
                    print("Veuillez entrer un nom valide sans chiffres ni caractères spéciaux.")

            while True:
                last_name = input("Prénom du joueur: ")
                if last_name.isalpha():
                    break
                else:
                    print("Veuillez entrer un prénom valide sans chiffres ni caractères spéciaux.")

            while True:
                date_birth = input("Date de naissance du joueur JJ/MM/AAAA: ")
                try:
                    datetime.strptime(date_birth, '%d/%m/%Y')
                    break
                except ValueError:
                    print("Veuillez entrer une date au format JJ/MM/AAAA.")

            while True:
                id_chess = input("Identifiant national d'échec, au format AB12345 :")
                if len(id_chess) == 7:
                    if id_chess[0:2].isalpha():
                        if id_chess[2:7].isnumeric():
                            break
                        else:
                            print("Veuillez entrer un format d'identifiant d'échec valide AB12345")
                    else:
                        print("Veuillez entrer un format d'identifiant d'échec valide AB12345")
                else:
                    print("Veuillez entrer un format d'identifiant d'échec valide AB12345")
            return name.capitalize(), last_name.capitalize(), date_birth.capitalize(), id_chess.upper()

    def players_for_tournament(self):
        while True:
            choice = input("Souhaitez-vous ajouter des joueurs au tournoi ? O/N: ")
            if choice.upper() == "O":
                return True
            elif choice.upper() == "N":
                return False
            else:
                print("Merci d'indiquer une donnée valide, O ou N \n")

    def add_player_in_tournament(self, players, peers):
        if players:
            i = 1
            print("\n\nLes joueurs selectionnés\n")
            for player in players:
                print(i, "-",
                      player[0].name,
                      player[0].first_name,
                      player[0].id_chess,
                      "\n")
                i += 1
        if not peers:
            print("Veuillez entrer un nombre de joueurs pairs s'il vous plait\n\n")

        while True:
            another_player = input("Voulez ajouter un autre joueur? O/N? ")
            if another_player.upper() == "N":
                return False
            elif another_player.upper() == "O":
                return True
            else:
                print("Merci d'indiquer une donnée valide, O ou N \n")

    def show_player(self, check):
        if check:
            print("\nJoueur inconnu !")
        while True:
            player = input("Entrer le nom du joueur : ")
            if player.isalpha():
                return player.capitalize()
            else:
                print("Veuillez entrer un nom valide sans chiffres ni caractères spéciaux.")

    def choose_players(self, players):
        i = 1
        print("\nAttention", len(players), "joueurs portent ce nom \n")
        for player in players:
            print(i, "-", player["name"], player["first_name"], player["date_birth"], player["id_chess"])
            i += 1
        while True:
            index_player = input("Veuillez indiquer le chiffre du joueur voulu : ")
            if index_player.isnumeric() and int(index_player) <= (i-1):
                return players[int(index_player) - 1]
            else:
                print("Merci d'indiquer une donnée valide\n")

    def show_players(self, players):
        print("\n\nLes Joueurs :\n")

        player_data = []
        header = ["Nom", "Prénom", "Date de naissance", "ID d'échec"]
        for player, players_details in enumerate(players, start=1):
            player_info = [players_details["name"],
                           players_details["first_name"],
                           players_details["date_birth"],
                           players_details["id_chess"]]
            player_data.append(player_info)

        table = tabulate(player_data, headers=header, tablefmt="fancy_grid")
        print(table)
        return None

    def show_tournaments(self, tournaments):
        tournament_data = []
        header = ["Nom du tournoi", "Lieu", "Date de début", "Date de fin"]
        print("\n\nLes tournois enregistrés :\n")
        for tournament_id, tournament_details in tournaments["tournament"].items():
            tournament_info = [tournament_details["name_tournament"],
                               tournament_details["locality"],
                               tournament_details["start_date"],
                               tournament_details["end_date"]
                               ]
            tournament_data.append(tournament_info)
        table = tabulate(tournament_data, headers=header, tablefmt="fancy_grid")
        print(table)
        return None

    def modification_player(self, info_player):
        print("\n\nJoueur :"
              "\n1 - Nom :", info_player["name"],
              "\n2 - Prenom :", info_player["first_name"],
              "\n3 - Date de naissance :", info_player["date_birth"],
              "\n4 - ID d'échec :", info_player["id_chess"], "\n")
        while True:
            choice = input("\nQue souhaitez-vous changer : ")
            if choice.isnumeric() and int(choice) == 1:
                while True:
                    new_name = input("Nouveau nom du joueur: ")
                    if new_name.isalpha():
                        break
                    else:
                        print("Veuillez entrer un nom valide sans chiffres ni caractères spéciaux.")
                return choice, new_name.capitalize()

            elif choice.isnumeric() and int(choice) == 2:
                while True:
                    new_last_name = input("Nouveau prénom du joueur: ")
                    if new_last_name.isalpha():
                        break
                    else:
                        print("Veuillez entrer un prénom valide sans chiffres ni caractères spéciaux.")
                return choice, new_last_name.capitalize()

            elif choice.isnumeric() and int(choice) == 3:
                while True:
                    new_date_birth = input("Nouvelle date de naissance du joueur JJ/MM/AAAA: ")
                    try:
                        datetime.strptime(new_date_birth, '%d/%m/%Y')
                        break
                    except ValueError:
                        print("Veuillez entrer une date au format JJ/MM/AAAA.")
                return choice, new_date_birth

            elif choice.isnumeric() and int(choice) == 4:
                while True:
                    new_id_chess = input("Nouvel identifiant national d'échec, au format AB12345: ")
                    if len(new_id_chess) == 7:
                        if new_id_chess[0:2].isalpha():
                            if new_id_chess[2:7].isnumeric():
                                break
                            else:
                                print("Veuillez entrer un format d'identifiant d'échec valide AB12345")
                        else:
                            print("Veuillez entrer un format d'identifiant d'échec valide AB12345")
                    else:
                        print("Veuillez entrer un format d'identifiant d'échec valide AB12345")
                return choice, new_id_chess.upper()

            else:
                print("Merci d'indiquer une donnée valide\n")

    def prompt_for_tournament(self):
        while True:

            while True:
                name_tournament = input("Nom du tournoi: ")
                if all(char.isalpha() or char.isspace() for char in name_tournament):
                    break
                else:
                    print("Veuillez entrer un nom de tournoi valide sans chiffres ni caractères spéciaux.")

            while True:
                locality = input("Où le tournoi se situe-t-il: ")
                if all(char.isalpha() or char.isspace() for char in locality):
                    break
                else:
                    print("Veuillez entrer un lieu valide sans chiffres ni caractères spéciaux.")

            print("\nVous avez ajouté le tournoi : ", name_tournament.capitalize(), "\nlieu : ", locality.capitalize())
            choice = input("\n1 - Valider ces informations\n"
                           "2 - Modifier ces informations\n"
                           "Votre choix : ")
            if choice == "1":
                return name_tournament.capitalize(), locality.capitalize()

    def description(self):
        while True:
            ask_for_description = input("Souhaitez vous ajouter une description ? O/N : ")
            if ask_for_description.upper() == "O":
                description = input("Votre description : ")
                if all(char.isalpha() or char.isspace() or char.isnumeric() for char in description):
                    print(description.capitalize())
                    choice = input("\n1 - Valider ces informations\n"
                                   "2 - Modifier ces informations\n"
                                   "Votre choix : ")
                    if choice == "1":
                        return description.capitalize()
                else:
                    print("Veuillez entrer une description valide sans caractères spéciaux.")
            elif ask_for_description.upper() == "N":
                return None
            else:
                print("Merci de saisir une donnée valide, O ou N")

    def choose_tournament(self, check):
        if check:
            print("\nTournoi inconnu !")
        while True:
            ask_name_tournament = input("à quel tournoi souhaitez-vous jouer ? ")
            if all(char.isalpha() or char.isspace() for char in ask_name_tournament):
                break
            else:
                print("Merci d'entrer un nom de tournoi valide")

        return ask_name_tournament.capitalize()

    def show_tournament(self, tournament, bis):
        if tournament.end_date:
            end_date = tournament.end_date
        else:
            end_date = "tournoi en cours"
        if not bis:
            tournament_info = [{
                "Nom du tournoi": tournament.name_tournament,
                "Lieu": tournament.locality,
                "Date de début": tournament.start_date,
                "Date de fin": end_date
            }]
            table = tabulate(tournament_info, headers="keys", tablefmt="fancy_grid")
            print(table)
        while True:
            print("\nQue voulez-vous faire ?")
            print("1 - Revenir au menu")
            print("2 - Voir la liste des joueurs du tournoi")
            print("3 - Voir tous les rounds et matchs du tournoi")
            print("4 - Voir le classement")
            if tournament.status:
                print("5 - Continuer le tournoi")
            choice = input("Votre choix : ")
            if choice.isnumeric() and int(choice) <= 4:
                return choice
            elif choice.isnumeric() and int(choice) == 5 and tournament.status:
                return choice
            else:
                print("\nMerci d'entrer une donnée valide")

    def show_players_in_tournament(self, players):
        print("\n\nLes", len(players), "joueurs du tournoi :\n")

        player_data = []
        header = ["Nom", "Prénom", "Date de naissance", "ID d'échec", "Score "]
        for player in players:
            player_info = [player[0].name,
                           player[0].first_name,
                           player[0].date_birth,
                           player[0].id_chess,
                           player[1]]
            player_data.append(player_info)

        table = tabulate(player_data, headers=header, tablefmt="fancy_grid")
        print(table)
        return None

    def show_info_in_tournament(self, rounds):
        tournament_data = []

        for round in rounds:
            header_round = [round['name_round']]
            round_info = []

            for match in round['list_matches']:
                match_info = {
                    header_round[0]: " VS ".join([f"{player[0]}: {player[1]}" for player in match['result_match']])
                }
                round_info.append(match_info)

            tournament_data.append((header_round, round_info))

        # Utilisez .tabulate() pour formatter chaque tour comme un sous-tableau
        for header, round_info in tournament_data:
            table = tabulate(round_info, headers="keys", tablefmt="fancy_grid")
            print(table)

    def continue_tournament(self, tournament):
        print("Souhaitez-vous continuer le tournoi", tournament, "?")
        while True:
            choice = input("O/N : ")
            if choice.upper() == "O":
                return True
            elif choice.upper() == "N":
                return False
            else:
                print("Merci de saisir une donnée valide, O ou N")

    def scores_match(self, player1, player2):
        scores = []
        print("\nMATCH\n", player1.name, player1.first_name, "VS", player2.name, player2.first_name, "\n")
        print(player1.name, player1.first_name)

        while True:
            score1 = input("Score du premier joueur : ")
            if score1 == "0" or score1 == "1" or score1 == "0.5":
                scores.append(score1)
                break
            else:
                print("Merci d'entrer une donnée correcte, 0, 1 ou 0.5.")
        print(player2.name, player2.first_name)

        while True:
            score2 = input("Score du second joueur : ")
            if score2 == "0" or score2 == "1" or score2 == "0.5":
                scores.append(score2)
                break
            else:
                print("Merci d'entrer une donnée correcte, 0, 1 ou 0.5.")
        return scores

    def next_round(self):
        while True:
            get_round = input("Voulez-vous rejouer un round ? O/N ")
            if get_round.capitalize() == "O":
                return True
            elif get_round.capitalize() == "N":
                return False
            else:
                print("Merci de saisir une donnée valide")

    def play_game(self):
        while True:
            play = input("Souhaitez-vous commencer le tournoi ? O/N ")
            if play.capitalize() == "O":
                return True
            elif play.capitalize() == "N":
                return False
            else:
                print("Merci de saisir une donnée valide")

    def show_final_players(self, players, status):
        player_data = []
        number = 1
        if status:
            header = ["Classement actuel", "", "", "", "Score"]
        else:
            header = ["Classement final", "", "", "", "Score"]
        for player in players:

            player_info = [
                number,
                player[0].name,
                player[0].first_name,
                player[0].date_birth,
                player[0].id_chess,
                player[1]
            ]
            player_data.append(player_info)
            number += 1
        table = tabulate(player_data, headers=header, tablefmt="fancy_grid")
        print(table)
        return None
