
class Player:

    """ Le joueur a un nom, un prénom, une date de naissance et son identifiant d'échecs """

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


    """ TRouver logique pour eviter les rencontres multiples"""

    """ trouver logique pour trier par score """

    def __init__(self, id_player):
        self.id_player = id_player

    def select_player(self, points=0):
        self.points = points

    def __str__(self):
        pass
        return f"Test Match : {self.id_player}."



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
        self.actual_round = actual_round
        self.list_rounds = list_rounds
        self.list_players = list_players
        self.description = description
        self.rounds = rounds



class Round:
    """ un round contient une liste des matchs, un nom, une date et une heure de début, une date et une heure de fin,
    indiqué quand le round est terminé"""

    def __init__(self, name_round, round_start_date, round_start_hours, round_end_date, round_end_hours, round_finished=None):
        self.name_round = name_round
        self.round_start_date = round_start_date
        self.round_start_hours = round_start_hours
        self.round_end_date = round_end_date
        self.round_end_hours = round_end_hours
        self.round_finished = round_finished


class Score:

    def __init__(self, actual_score=0, points=0):
        self.actual_score = actual_score
        self.points = points

    def points(self, actual_score, points):
        total_points = actual_score + points
        return total_points





"""

def points(self, add_point=0):
    self.points = points
    self.add_points = add_point
    return add_point


def update_points(self, points):
    update = points + add_points
    return update
    """



player1 = Player("Potter", "Harry", "07/31/1980", "HP12345")
player2 = Player("Granger", "Hermione", "09/19/1979", "GH12345")
player3 = Player("Weasley", "Ron", "03/01/1980", "WR12345")
player4 = Player("Weasley", "Ginny", "08/11/1981", "WG12345")
player5 = Player("Malefoy", "Drago", "06/05/1980", "MD12345")
player6 = Player("Lovegood", "Luna", "02/13/1980", "LL12345")
player7 = Player("Londubat", "Neville", "07/30/1980", "LN12345")
player8 = Player("Chang", "Cho", "04/24/1979", "CC12345")
print("Object 01 : ", player1, "\n Object 02 : ", player2)

match = Match(player1.id_chess)
print("TEST", match)



tournoi01 = Tournament("Tournoi des Sorciers", "Poudlard", "07 juillet", "09 juillet", "Round 01", "8 rounds",
                       "liste des joueurs", "50 points pour Griffondor !")
# print(tournoi01.name, tournoi01.locality, tournoi01.start_date, tournoi01.end_date, tournoi01.actual_round, tournoi01.list_rounds, tournoi01.rounds, tournoi01.list_players, tournoi01.description)


round01 = Round("Round01", "07 juillet", "11h", "09 juillet", "17h", True)
# print(round01.name, round01.round_start_date, round01.round_start_hours, round01.round_end_date, round01.round_end_hours, round01.round_finished)

