
class Tournament:
    """ Le tournoi contient  nom, un lieu, une date de début et de fin, un nombre de tours défini,
    un numéro du tour actuel, une liste des rounds, une liste des joueurs ainsi qu'une description
    pour les remarques générales du directeur du tournoi"""

    def __init__(self, name_tournament, locality, start_date, description=None,
                 rounds=4):
        self.name_tournament = name_tournament
        self.locality = locality
        self.start_date = start_date
#        self.actual_round = actual_round # à connecter avec la classe Round
        self.description = description
        self.rounds = rounds
        self.end = "Non définit"

        self.list_rounds = []
        self.list_players = []


    def add_player(self, player):
        self.player = player
        self.list_players.append([player.name, player.first_name, player.date_birth, player.id_chess])


    def __str__(self):
        return f" Nom du tournoi : {self.name_tournament}\n" \
               f"Localisation : {self.locality}\n" \
               f"Date de début : {self.start_date}\n" \
               f"Nombre de rounds : {self.rounds}\n" \
               f"Les differents Rounds : {self.list_rounds}\n" \
               f"Date de fin : {self.end}\n" \
               f"Commentaire du directeur : {self.description}\n" \
               f"liste des joueurs : {self.list_players}"\

#              f"liste des joueurs : {self.list_players[0][1]}" ne donne que le prénom [0] = premier player de la liste [1] = le prénom