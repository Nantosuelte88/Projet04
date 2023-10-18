

class Round:
    """ un round contient une liste des matchs, un nom, une date et une heure de début, une date et une heure de fin """

    def __init__(self, name_round):
        self.name_round = name_round
        self.list_matches = []
        self.start_time = "start_time"
        self.end_time = "end_time"

    def __str__(self):
        return f" Nom du round : {self.name_round} . " \
               f"Date de début : {self.start_time} . " \
               f"Date de fin : {self.end_time} . " \
               f"MATCH : {self.list_matches}"
