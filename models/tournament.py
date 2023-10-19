

class Tournament:
    """ Le tournoi contient prend comme arguments un nom, un lieu, une date de début,
    une description et un nombre de round
    On ajoute ensuite une date de fin, un statut

    - une liste de rounds qui contient les rounds de la classe Round
    - une liste de joueurs provenant de la classe Player"""

    def __init__(self, name_tournament, locality, start_date, description,
                 number_rounds):
        self.name_tournament = name_tournament
        self.locality = locality
        self.start_date = start_date
        self.description = description
        self.number_rounds = number_rounds
        self.end_date = False

        self.list_rounds = []
        self.list_players = []

        self.status = True

    def __str__(self):
        return f"Nom du tournoi : {self.name_tournament}\n" \
               f"Localisation : {self.locality}\n" \
               f"Date de début : {self.start_date}\n"
