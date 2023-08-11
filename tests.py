
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


class ClasseC:

    def __init__(self, name_tournoi):
        self.name_tournoi = name_tournoi
        self.joueurs = []


    def add_player(self, player):
        self.player = player
        self.joueurs.append([player.name, player.number])


    def __str__(self):
        return f" Nome du tournoi : {self.name_tournoi}, liste des joueurs : {self.joueurs}"

#match1 = Match("Premier Match")
joueur1 = ClasseA("Michel", 2)
joueur2 = ClasseA("Jean-Pierre", 4)
joueur3 = ClasseA("Georgette", 6)
classb = ClasseB(joueur3)
print(classb)
classc = ClasseC("Bloup")
player1 = classc.add_player(joueur1)
player2 = classc.add_player(joueur2)
print(classc)
