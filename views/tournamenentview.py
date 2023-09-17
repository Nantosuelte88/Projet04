from datetime import datetime


class View:
    def menu(self):

        while True:
            print("\n-------- MENU --------")
            choice = input("Que souhaitez-vous faire ?\n"
                           "Créer un nouveau tournoi = 1\n"
                           "Choisir un tournoi = 2\n"
                           "Quitter = 3\n"
                           "---------------------- \n\n"
                           "Votre choix : ")
            if choice.isnumeric() and int(choice) <= 2:
                break
            elif choice.isnumeric() and int(choice) ==3:
                choose_quit = input("Attention, vous allez quitter le programme, valider votre choix ? O/N : ")
                if choose_quit.upper() == "O":
                    break
            else:
                print("Merci d'entrer une donnée valide")
        return choice

    def menu_players(self):
        while True:
            print("\n-------- Choix des joueurs --------")
            choice_for_players = \
                input("Ajouter un nouveau joueur = 1\n"
                      "Choisir un joueur existant = 2\n"
                      "Selectionner 8 joueurs au hasard = 3\n"
                      "Revenir au menu principal = 4\n"
                      "---------------------- \n\n"
                      "Votre choix : ")
            if choice_for_players.isnumeric() and int(choice_for_players) <= 4:
                break
            else:
                print("Meri d'entrer une donnée valide")
        return choice_for_players

    def prompt_for_player(self):
        add_players = []

        while True:
            ask = input("Ajouter un joueur ? O/N : ")
            if ask.capitalize() == "O":
                print("Yep")
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

            elif ask.capitalize() == "N":
                break
            else:
                print("Merci de saisir une donnée valide, O ou N")

        return add_players

    def choose_players(self, players):
        players_list = []
        while True:
            if players_list:
                print("Joueur.s ajouté.s :", players_list)
                for player in players_list:
                    print(player.name, player.first_name, player.id_chess)
            add_player = input("Choisir un joueur ? O/N: ")
            if add_player.capitalize() == "O":
                print("YEEES")

                while True:  # 2eme while

                    ask_name_player = input("Entrer le nom du joueur ? ")

                    if all(char.isalpha() or char.isspace() for char in ask_name_player):
                        print("Verif joueur", ask_name_player)

                        matching_list = []

                        u = 0
                        for player in players:
                            u += 1
                            if ask_name_player.capitalize() == player.name:
                                print(u, "NOOOOM DU JOUEUUUUUR correspondant", ask_name_player, "=", player.name)
                                print(u, "Tous les joueurs correpondant ?", player)
                                matching_list.append(player)

                            else:
                                print(u, "Joueur inconnu", player.name)

                        if len(matching_list) >= 2:
                            print(u, "plus de 2 correspondance dans la liste de joueurs.", len(matching_list),
                                  "Ask_name =", ask_name_player, "matching_list = ",
                                  matching_list)
                            print("Plusieurs joueurs portent ce nom de famille : ")
                            o = 0

                            for player in matching_list:
                                o +=1
                                print(o, player.name, player.first_name, player.id_chess)
                            select_player = input("Merci d'indiquer l'ID du joueur que vous souhaitez ajouter: ")
                            player_found = False
                            f = 0

                            for player in matching_list:
                                f +=1
                                if select_player.upper() == player.id_chess:
                                    print(f, "verif id correct", player.name, player.first_name, player.id_chess)
                                    players_list.append(player)
                                    player_found = True
                                    break

                            if not player_found:
                                print(f, "id incorrect")
                            print(u, "fin du if")

                        #             players_list.append(ask_name_player)
                        elif len(matching_list) == 1:
                            player = matching_list[0]
                            print(u, "Correpondance normale", player.name, player.first_name)
                            players_list.append(player)

                    else:
                        print("Merci d'entrer un nom de joueur valide")

                    print("liste des joueurs : ", players_list)

                    another_player = input("Voulez ajouter un autre joueur? O/N? ")
                    if another_player == "N":
                        break

            elif add_player.capitalize() == "N":
                print("Vous avez ajouté : \n", players_list)
                break
            else:
                print("Merci de saisir une donnée valide, O ou N")

        return players_list

    def prompt_for_tournament(self):
        add_tournaments =[]

        while True:
            ask = input("Ajouter un tournoi ? O/N : ")
            if ask.capitalize() == "O":
                print("Yep")

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

                add_tournaments.append((name_tournament.capitalize(), locality.capitalize()))

            elif ask.capitalize() == "N":
                break
            else:
                print("Merci de saisir une donnée valide, O ou N")
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



