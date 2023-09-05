from datetime import datetime


class View:

    def prompt_for_player(self):
        add_players =[]

        while True:
            ask = input("Ajouter un joueur ? O/N : ")
            if ask == "O":
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
                add_players.append((name, last_name, date_birth, id_chess))

            elif ask == "N":
                break
            else:
                print("Merci de saisir une donnée valide, O ou N")

        return add_players




    def prompt_for_tournament(self):
        add_tournaments =[]

        while True:
            ask = input("Ajouter un tournoi ? O/N : ")
            if ask == "O":
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

                add_tournaments.append((name_tournament, locality))

            elif ask == "N":
                break
            else:
                print("Merci de saisir une donnée valide, O ou N")
        return add_tournaments


    def choose_tournament(self, tournaments):
        print("Liste des tournois : ")
        for tournament in tournaments:
            print("Print select tournament\n", tournament)
        ask_name_tournament = input("à quel tournoi souhaitez-vous jouer ?")
        while True:
            if all(char.isalpha() or char.isspace() for char in ask_name_tournament):
                print("Verif tournoi", ask_name_tournament)
                break
            else:
                print("Merci d'entrer un nom de tournoi valide")
        return ask_name_tournament
