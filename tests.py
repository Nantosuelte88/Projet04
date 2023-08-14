class Joueur:
    def __init__(self, nom, score):
        self.nom = nom
        self.score = score

    def __str__(self):
        return f"Nom: {self.nom}\nScore: {self.score}\n"


class Match:
    def __init__(self, joueur1, score1, joueur2, score2):
        self.joueur1 = joueur1
        self.score1 = score1
        self.joueur2 = joueur2
        self.score2 = score2

    def __str__(self):
        return f"Match:\n{self.joueur1.nom} ({self.score1}) vs {self.joueur2.nom} ({self.score2})"


class Tournoi:
    def __init__(self, joueurs):
        self.joueurs = [Joueur(nom, score) for nom, score in joueurs]
        self.matchs = []

    def ajouter_match(self, match):
        self.matchs.append(match)

    def afficher_joueurs(self):
        for joueur in self.joueurs:
            print(joueur)

    def afficher_matchs(self):
        for match in self.matchs:
            print(match)

class System_game:

    def match_result(self):
        self.matchs = []



JOUEURS = [
    ("Potter", 0),
    ("Granger", 0),
    ("Weasley", 0),
    ("Weasley", 0),
    ("Malefoy", 0),
    ("Lovegood", 0),
    ("Londubat", 0),
    ("Chang", 0)
]

tournoi = Tournoi(JOUEURS)

match1 = Match(tournoi.joueurs[0], 6, tournoi.joueurs[1], 8)
match2 = Match(tournoi.joueurs[0], 3, tournoi.joueurs[2], 2)

tournoi.ajouter_match(match1)
tournoi.ajouter_match(match2)

tournoi.afficher_joueurs()
tournoi.afficher_matchs()








JOUEURS = [
    ("Potter", 0),
    ("Granger", 0),
    ("Weasley", 0),
    ("Weasley", 0),
    ("Malefoy", 0),
    ("Lovegood", 0),
    ("Londubat", 0),
    ("Chang", 0)
]



def generer_matchs(joueurs):
    matchs = []

    match_number = len(joueurs)

    for i in match_number :
        joueur1 = joueurs[0]
        joueur2 = joueurs[1]
        matchs.append((joueur1, joueur2))


    return matchs


matchs = generer_matchs(JOUEURS)

for index, match in enumerate(matchs, start=1):
    joueur1, joueur2 = match
    print(f"Match {index}: {joueur1[0]} vs {joueur2[0]}")


