from typing import List
import random

""" Dans le Modèle """


class Score:

    def __init__(self, actual_score=0, points=0):
        self.actual_score = actual_score
        self.points = points

    def points(self, actual_score, points):
        total_points = actual_score + points
        return total_points


class Player:
    """ Le joueur a un nom, un prénom, une date de naissance et son identifiant d'échecs """

    def __init__(self, name, first_name, date_birth, id_chess):
        self.name = name
        self.first_name = first_name
        self.date_birth = date_birth
        self.id_chess = id_chess


#   def __str__(self):
#      return f"Nom du joueur {self.name} Prénom {self.first_name}"


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


class Match:
    """ un match contient un tuple ayant deux listes contenant chacune - un joueur et - un score"""

    def play_game(self, point=1):
        self.point = point
        return point

    def choose_players(self):
        """ TRouver logique pour eviter les rencontres multiples"""

        """ trouver logique pour trier par score """


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

print(player1.name, player1.first_name, player1.date_birth, player1.id_chess)

# aff = print(player1)

# match01 = Match().play_game()


tournoi01 = Tournament("Tournoi des Sorciers", "Poudlard", "07 juillet", "09 juillet", "Round 01", "8 rounds",
                       "liste des joueurs", "50 points pour Griffondor !")
# print(tournoi01.name, tournoi01.locality, tournoi01.start_date, tournoi01.end_date, tournoi01.actual_round, tournoi01.list_rounds, tournoi01.rounds, tournoi01.list_players, tournoi01.description)


round01 = Round("Round01", "07 juillet", "11h", "09 juillet", "17h", True)
# print(round01.name, round01.round_start_date, round01.round_start_hours, round01.round_end_date, round01.round_end_hours, round01.round_finished)








class Controllers:

    def __init__(self):
        pass

    def get_players(self):
        while len(self.players) < 4:
            player = Player(name="bloup")
            self.players.append(player)
            return player



    def run(self):
        self.get_players()


test2 = Controllers()
#print(test2.get_players())


def run(self):
    self.get_players()
    pass



from typing import List
import random


WEAPONS = (
    "couche",
    "couteau",
    "kalash",
    "déambulateur",
    "chausson"
)

class Weap: #Card

    def __init__(self, weapons):
        self.weapons = weapons

class Hand(List):

    def append(self, object):
        if not isinstance(object, Weap):
            return ValueError("Votre arme n'est pas homoloqué !")
        return super().append(object)

class Deck:
    def __init__(self):
        """Has some cards."""

        self.append(Weap)
        self.shuffle()

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self)

class Machin:
    def __init__(self, name, points=0):
        self.name = name
        self.points = points
        self.hand: List[Weap] = Hand()

class Match:

    def __init__(self, name):
        self.name = name

    def update_score(self):
        pass

match1 = Match("Premier Match")
variable = Machin("Michel")
variable2 = Machin("Jean-Pierre")
variable3 = Machin("Georgette")

print(" Match = ", match1.name, "\n",
      "joueur 01: ",variable.name, "score : ", variable.points, "\n",
      "joueur 02: ",variable2.name, "score : ", variable2.points, "\n",
      "joueur 03: ",variable3.name, "score : ", variable3.points, "\n",)

#print(variable, variable2, variable3)






















from typing import List
class Player:

    def __init__(self):
        self.players = []


    def add_player(self, name):
        self.players.append(name)



player = Player()
player.add_player("Roger")
player.add_player("Michel")
print(player.players)













from typing import List
class Player:

    def __init__(self):
        pass




class ListPlayers:

    def __init__(self):
        self.players = []

    def add_player(self, name):
        self.players.append(name)


player = Player()
liste = ListPlayers()
liste.add_player("Roger")
liste.add_player("Michel")
print(liste.players)
