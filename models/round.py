class Round:
    """ un round contient une liste des matchs, un nom, une date et une heure de début, une date et une heure de fin """

    def __init__(self, name_round):
        self.name_round = name_round
        self.round_start = "round_start" # déclaration automatique lors du début
        self.round_end = "round_end" # déclaration automatique lors de la fin
        self.list_matchs = [] # La liste des matchs de ce round

    def __str__(self):
        return f" Nom du round : {self.name_round} . " \
               f"Date de début : {self.round_start} . " \
               f"Date de fin : {self.round_end} . " \
               f"MATCH : {self.list_matchs}"
