
class Player:

    """ Le joueur a un nom, un prénom, une date de naissance et son identifiant d'échecs  -- et des points ?? -- """

    def __init__(self, name, first_name, date_birth, id_chess, points=0):
        self.name = name
        self.first_name = first_name
        self.date_birth = date_birth
        self.id_chess = id_chess
        self.points = points

    def __str__(self):
        return f"Nom : {self.name}. " \
               f"Prénom : {self.first_name}. " \
               f"Date de naissance : {self.date_birth}. " \
               f"Numéro d'identification : {self.id_chess}."


class Match:

    """ un match contient un tuple ayant deux listes contenant chacune - un joueur et - un score"""


    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def select_player(self):
        """ trouver logique pour trier par score """
        """ Trouver logique pour eviter les rencontres multiples"""
        pass

    def who_win(self, winner="*Gagnant*"):
        self.winner = winner #indiquer qui a gagné
        return winner

    def __str__(self):
        return f"Test Match : {self.player1.name} VS {self.player2.name}. "



class Round:
    """ un round contient une liste des matchs, un nom, une date et une heure de début, une date et une heure de fin """

    def __init__(self, name_round, round_start_date, round_start_hours, round_end_date, round_end_hours, list_matchs):
        self.name_round = name_round
        self.round_start_date = round_start_date # déclaration automatique lors du début
        self.round_start_hours = round_start_hours # déclaration automatique lors du début
        self.round_end_date = round_end_date # déclaration automatique lors de la fin
        self.round_end_hours = round_end_hours # déclaration automatique lors de la fin
        self.list_matchs = list_matchs # La liste des matchs de ce round

    def __str__(self):
        return f" Nom du round : {self.name_round} . " \
               f"Date de début : {self.round_start_date} . " \
               f"Heure de début : {self.round_start_hours} . " \
               f"Date de fin : {self.round_end_date} . " \
               f"heure de fin : {self.round_end_hours} . " \
               f"MATCH : {self.list_matchs}"


class Tournament:
    """ Le tournoi contient  nom, un lieu, une date de début et de fin, un nombre de tours défini,
    un numéro du tour actuel, une liste des rounds, une liste des joueurs ainsi qu'une description
    pour les remarques générales du directeur du tournoi"""

    def __init__(self, name_tournament, locality, start_date, end_date, actual_round, list_rounds, list_players, description=None,
                 rounds=4):
        self.name_tournament = name_tournament
        self.locality = locality
        self.start_date = start_date
        self.end_date = end_date
        self.actual_round = actual_round # à connecter avec la classe Round
        self.list_rounds = list_rounds # à connecter avec une liste des objets de la classe Round
        self.list_players = list_players # à connecter avec la liste des joueurs
        self.description = description
        self.rounds = rounds

    def __str__(self):
        return f" Nom du tournoi : {self.name_tournament}\n" \
               f"Localisation : {self.locality}\n" \
               f"Date de début : {self.start_date}\n" \
               f"Round actuel : {self.actual_round}\n" \
               f"Nombre de rounds : {self.rounds}\n" \
               f"Les differents Rounds : {self.list_rounds}\n" \
               f"Liste des joueurs : {self.list_players}\n" \
               f"Date de fin : {self.end_date}\n" \
               f"Commentaire du directeur : {self.description}"




player1 = Player("Potter", "Harry", "07/31/1980", "HP12345")
player2 = Player("Granger", "Hermione", "09/19/1979", "GH12345")
player3 = Player("Weasley", "Ron", "03/01/1980", "WR12345")
player4 = Player("Weasley", "Ginny", "08/11/1981", "WG12345")
player5 = Player("Malefoy", "Drago", "06/05/1980", "MD12345")
player6 = Player("Lovegood", "Luna", "02/13/1980", "LL12345")
player7 = Player("Londubat", "Neville", "07/30/1980", "LN12345")
player8 = Player("Chang", "Cho", "04/24/1979", "CC12345")

players = [player1.name, player2.name]
#print("Object 01 : ", player1, "\n Object 02 : ", player2)

match = Match(player1, player2)
#print("TEST", match)
#print("Le gagnant est", match.who_win(player2.name))

round01 = Round("Round01", "07 juillet", "11h", "09 juillet", "17h", match)
#print(round01)

tournoi01 = Tournament("Tournoi des Sorciers", "Poudlard", "07 Août", "30 Août", round01.name_round, "8 rounds",
                       players, "50 points pour Griffondor !")
print(tournoi01)