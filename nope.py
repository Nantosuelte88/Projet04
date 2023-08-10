from typing import List
import random

""" Dans le Modèle """







"""

def points(self, add_point=0):
    self.points = points
    self.add_points = add_point
    return add_point


def update_points(self, points):
    update = points + add_points
    return update
    """


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










class ClasseA:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class ClasseB:
    def __init__(self, classe_a_instance):
        self.classe_a_instance = classe_a_instance
        self.solution = classe_a_instance.number * 2

    def __str__(self):
        return f"Test de phrase {self.classe_a_instance.name} : {self.solution}."

classa = ClasseA("Test1", 42)
classb = ClasseB(classa)
print(classb)