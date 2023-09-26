from datetime import datetime


class View:
    def menu(self):

        while True:
            print("\n-------- MENU --------")
            choice = input("Que souhaitez-vous faire ?\n"
                           "1 - Créer un nouveau joueur \n"
                           "2 - Créer un nouveau tournoi\n"
                           "3 - Rechercher un tournoi\n"
                           "4 - Modifier un joueur\n"
                           "5 - Voir les joueurs\n"                           
                           "6 - Quitter\n"
                           "---------------------- \n\n"
                           "Votre choix : ")
            if choice.isnumeric() and int(choice) <= 5:
                break
            elif choice.isnumeric() and int(choice) == 6:
                choose_quit = input("Attention, vous allez quitter le programme, valider votre choix ? O/N : ")
                if choose_quit.upper() == "O":
                    break
            else:
                print("\nMerci d'entrer une donnée valide")
        return choice

    def prompt_for_player(self):
        add_players = []

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
                    print("Bien 7")  # test
                    if id_chess[0:2].isalpha():
                        print("Bien alpha :", id_chess[0:2])  # test
                        if id_chess[2:7].isnumeric():
                            print("Bien numeric :", id_chess[2:7])  # test
                            break
                        else:
                            print("Veuillez entrer un format d'identifiant d'échec valide AB12345")
                    else:
                        print("Veuillez entrer un format d'identifiant d'échec valide AB12345")
                else:
                    print("Veuillez entrer un format d'identifiant d'échec valide AB12345")
    #        add_players.append((name.capitalize(), last_name.capitalize(), date_birth, id_chess.upper()))
            return name.capitalize(), last_name.capitalize(), date_birth.capitalize(), id_chess.upper()

    def add_player_in_tournament(self):
        selected_players = []
        while True:
            while True:
                ask_name_player = input("Entrer le nom du joueur ? ")

                if all(char.isalpha() or char.isspace() for char in ask_name_player):
                    print("Verif joueur", ask_name_player)
                    selected_players.append(ask_name_player.capitalize())
                else:
                    print("Merci d'entrer un nom de joueur valide")

                another_player = input("Voulez ajouter un autre joueur? O/N? ")
                if another_player.upper() == "N":
                    break
            print(len(selected_players))
            if (len(selected_players) %2) == 0:
                print("Joueurs paires")
                return selected_players
            else:
                print("merci d'entrer un nombre de joueurs paires")

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
        print("DANS CHOOSE PLAYER", players)
        i = 1
        print("\nAttention", len(players), "joueurs portent ce nom \n")
        for player in players:
            print(i, "-", player["name"], player["first_name"], player["date_birth"], player["id_chess"])
            i += 1
        while True:
            print("i =", (i-1))
            index_player = input("Veuillez indiquer le chiffre du joueur voulu : ")
            if index_player.isnumeric() and int(index_player) <= (i-1):
                return players[int(index_player) - 1]
            else:
                print("Merci d'indiquer une donnée valide\n")

    def show_players(self, players):
        print("\n\nLes Joueurs :\n")
        for player, players_details in enumerate(players, start=1):
            print(f"Joueur", player,
                  "\nNom :", players_details["name"],
                  "\nPrenom :", players_details["first_name"],
                  "\nDate de naissance :", players_details["date_birth"],
                  "\nID d'échec :", players_details["id_chess"], "\n")

    def modification_player(self, info_player):
        print(f"Joueur :"
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
                    new_id_chess = input("Nouvel dentifiant national d'échec, au format AB12345 :")
                    if len(new_id_chess) == 7:
                        print("Bien 7")  # test
                        if new_id_chess[0:2].isalpha():
                            print("Bien alpha :", new_id_chess[0:2])  # test
                            if new_id_chess[2:7].isnumeric():
                                print("Bien numeric :", new_id_chess[2:7])  # test
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
        add_tournaments = []
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
        #        add_tournaments.append((name_tournament.capitalize(), locality.capitalize()))
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
            ask_name_tournament = input("à quel tournoi souhaitez-vous jouer ?")
            if all(char.isalpha() or char.isspace() for char in ask_name_tournament):
                print("Verif tournoi", ask_name_tournament)
                break
            else:
                print("Merci d'entrer un nom de tournoi valide")

        return ask_name_tournament.capitalize()

    def show_tournament(self, tournament):
        print(f"\n\nTournoi selectionné:\n"
              "\nNom :", tournament["name_tournament"],
              "\nLieu :", tournament["locality"],
              "\nDate de debut :", tournament["start_date"],
              "\nDate de fin :", tournament["end_date"],
              "\nListe des rounds :", tournament["list_rounds"],
              "\nListe des joueurs :", tournament["list_players"],
              "\nDescription :", tournament["description"], "\n\n")
        while True:
            choice = input("Voulez-vous continuer le tournoi ? O/N: ")
            if choice == "0"
                return choice
    def scores_match(self, player1, player2):
        scores = []
        print("\nMATCH\n", player1.name, player1.first_name, "VS", player2.name, player2.first_name, "\n")
        print(player1.name, player1.first_name)

        while True:
            score1 = input("Score du premier joueur : ")
            if score1 == "0" or score1 == "1" or score1 == "0.5":
                print("bon score", score1)
                scores.append(score1)
                break
            else:
                print("Merci d'entrer une donnée correcte, 0, 1 ou 0.5.")
        print(player2.name, player2.first_name)

        while True:
            score2 = input("Score du second joueur : ")
            if score2 == "0" or score2 == "1" or score2 == "0.5":
                print("bon score", score2)
                scores.append(score2)
                break
            else:
                print("Merci d'entrer une donnée correcte, 0, 1 ou 0.5.")
        return scores


    def next_round(self, round):
        print("View next_round", round)
        while True:
            get_round = input("Voulez-vous rejouer un round ? O/N")
            if get_round.capitalize() == "O":
                return True
            elif get_round.capitalize() == "N":
                return False
            else:
                print("Merci de saisir une donnée valide")

    def play_game(self, tournament):
        print("View - play_game", tournament)
        while True:
            play = input("Souhaitez-vous commencer le tournoi ? O/N ")
            if play.capitalize() == "O":
                print("OUI", tournament)
                return True
            elif play.capitalize() == "N":
                return False
            else:
                print("Merci de saisir une donnée valide")




