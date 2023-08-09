
from typing import List
class Player():

    def __init__(self, name, first_name, date_birth, id_chess):
        self.name = name
        self.first_name = first_name
        self.date_birth = date_birth
        self.id_chess = id_chess

    def __str__(self):
        return f"Nom : {self.name}. " \
               f"Prénom : {self.first_name}. " \
               f"Date de naissance : {self.date_birth}. " \
               f"Numéro d'identification : {self.id_chess}."


class ListPlayers():

    def __init__(self):
        self.players = []


    def add_player(self, name, first_name, date_birth, id_chess):
        self.name = name
        self.first_name = first_name
        self.date_birth = date_birth
        self.id_chess = id_chess
        self.players.append()




player1 = Player("Potter", "Harry", "07/31/1980", "HP12345")
player2 = Player("Granger", "Hermione", "09/19/1979", "GH12345")
#liste = ListPlayers()
#liste.add_player("Potter", "Harry", "07/31/1980", "HP12345")

print("Object 01 : ", player1, "\n Object 02 : ", player2)
