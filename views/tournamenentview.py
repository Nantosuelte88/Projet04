from datetime import datetime


class View:

    def prompt_for_tournament(self):
        name_tournament = input("Nom du tournoi: ")
        if not name_tournament:
            return None
        locality = input("Où le tournoi se situe-t-il: ")
        if not locality:
            return None
        return  name_tournament, locality

    def prompt_for_player(self):

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
                print("Bien 7")
                if id_chess[0:2].isalpha():
                    print("Bien alpha :", id_chess[0:2])
                    if id_chess[2:7].isnumeric():
                        print("Bien numeric :", id_chess[2:7])
                        break
                    else:
                        print("Veuillez entrer un format d'identifiant d'échec valide AB12345")
                else:
                    print("Veuillez entrer un format d'identifiant d'échec valide AB12345")
            else:
                print("Veuillez entrer un format d'identifiant d'échec valide AB12345")



        return name, last_name, date_birth, id_chess