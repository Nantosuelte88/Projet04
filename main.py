from typing import List


""" Dans le Modèle """
class Player:
    """ Le joueur a un nom, un prénom, une date de naissance et son identifiant d'échecs """

    def __init__(self, name, first_name, date_birth, id_chess):
        self.name = name
        self.first_name = first_name
        self.date_birth = date_birth
        self.id_chess = id_chess


    def points(self, add_point=0):
        self.points = points
        self.add_points = add_point


    def update_points(self, points):
        update = points + add_points
        return update



#        print(
#            f"Nom : {name} \n"
#            f"Prenom : {first_name} \n"
#            f"Date de naissance : {date_birth} \n"
#            f"Identification nationnal d'echec : {id_chess} \n"
#            f"Nombre de points : {points}"
#        )





""" - ajouter les joueurs
    - faire tri des joueurs par point(s)
    - 
    """


player1 = Player("Smith", "John", "02/05/1999", "AB12345")
obj = print(player1)

