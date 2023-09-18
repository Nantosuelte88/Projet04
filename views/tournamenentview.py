from datetime import datetime


class View:
    def menu(self):

        while True:
            print("\n-------- MENU --------")
            choice = input("Que souhaitez-vous faire ?\n"
                           "1 - Créer un nouveau joueur \n"
                           "2 - Créer un nouveau tournoi\n"
                           "3 - Rechercher un tournoi\n"
                           "4 - Quitter\n"
                           "---------------------- \n\n"
                           "Votre choix : ")
            if choice.isnumeric() and int(choice) <= 3:
                break
            elif choice.isnumeric() and int(choice) == 4:
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
            add_players.append((name.capitalize(), last_name.capitalize(), date_birth, id_chess.upper()))
            return add_players

    def add_player_in_tournament(self):
        while True:
            ask_name_player = input("Entrer le nom du joueur ? ")

            if all(char.isalpha() or char.isspace() for char in ask_name_player):
                print("Verif joueur", ask_name_player)
                return ask_name_player.capitalize()
            else:
                print("Merci d'entrer un nom de joueur valide")

            another_player = input("Voulez ajouter un autre joueur? O/N? ")
            if another_player.upper() == "N":
                break

    def choose_players(self, players):
        id_chess = input("plusieurs joueurs ont le même nom, merci de preciser son identifiant d'echec : ")
        return id_chess.upper()

    def prompt_for_tournament(self):
        add_tournaments =[]
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
                add_tournaments.append((name_tournament.capitalize(), locality.capitalize()))
                return add_tournaments



    def choose_tournament(self, tournaments):
        print("Liste des tournois : ")
        for tournament in tournaments:
            print("Print select tournament\n", tournament)
        while True:
            ask_name_tournament = input("à quel tournoi souhaitez-vous jouer ?")
            if all(char.isalpha() or char.isspace() for char in ask_name_tournament):
                print("Verif tournoi", ask_name_tournament)
                break
            else:
                print("Merci d'entrer un nom de tournoi valide")

        return ask_name_tournament.capitalize()

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



