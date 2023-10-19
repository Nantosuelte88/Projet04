class Player:
    """ Le joueur a un nom, un prénom, une date de naissance et son identifiant d'échec """

    def __init__(self, name, first_name, date_birth, id_chess):
        self.name = name
        self.first_name = first_name
        self.date_birth = date_birth
        self.id_chess = id_chess

    def __str__(self):
        return f"Nom : {self.name} " \
               f"Prénom : {self.first_name} " \
               f"Date de naissance : {self.date_birth} " \
               f"Numéro d'identification : {self.id_chess}"
