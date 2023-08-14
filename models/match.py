class Match:
    """ un match contient un tuple ayant deux listes contenant chacune - un joueur et - un score"""

    def __init__(self, player1, score1, player2, score2):
        self.player1 = player1
        self.score1 = score1
        self.player2 = player2
        self.score2 = score2

        self.match = ([player1, score1], [player2, score2])


    def __str__(self):
        return f"Match {self.player1.name} VS {self.player2.name}\n" \
               f"Scores :\n" \
               f"{self.player1.name} = {self.score1}\n" \
               f"{self.player2.name} = {self.score2}\n"