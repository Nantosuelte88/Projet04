class Match:
    """ Représente un match entre deux joueurs et leurs scores sous la forme d'un tuple """

    def __init__(self, player1, score1, player2, score2):
        self.player1 = player1
        self.score1 = score1
        self.player2 = player2
        self.score2 = score2

        self.result_match = ([player1, score1], [player2, score2])

    def __str__(self):
        return f"\n{self.player1} = {self.score1}\n" \
               f"{self.player2} = {self.score2}\n"
