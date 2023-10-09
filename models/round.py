

class Round:
    """ un round contient une liste des matchs, un nom, une date et une heure de début, une date et une heure de fin """

    def __init__(self, name_round):
        self.name_round = name_round
        self.round_start = "round_start"
        self.round_end = "round_end"
        self.list_matches = []
        self.start_time = "start_time"
        self.end_time = "end_time"

    def __str__(self):
        return f" Nom du round : {self.name_round} . " \
               f"Date de début : {self.round_start} . " \
               f"Date de fin : {self.round_end} . " \
               f"MATCH : {self.list_matches}"
