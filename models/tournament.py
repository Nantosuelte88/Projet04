

class Tournament:
    """ Le tournoi contient  nom, un lieu, une date de début et de fin, un nombre de tours défini,
    un numéro du tour actuel, une liste des rounds, une liste des joueurs ainsi qu'une description
    pour les remarques générales du directeur du tournoi"""

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
