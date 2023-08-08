
PLAYERS = (("Potter", "Harry", "07/31/1980", "HP12345"),
           ("Granger", "Hermione", "09/19/1979", "GH12345"),
           ("Weasley", "Ron", "03/01/1980", "WR12345", 2),
           ("Weasley", "Ginny", "08/11/1981", "WG12345"),
           ("Malefoy", "Drago", "06/05/1980", "MD12345"),
           ("Lovegood", "Luna", "02/13/1980", "LL12345"),
           ("Londubat", "Neville", "07/30/1980", "LN12345"),
           ("Chang", "Cho", "04/24/1979", "CC12345")
           )


class Player:
    """ Le joueur a un nom, un prénom, une date de naissance et son identifiant d'échecs """

    def __init__(self, name, first_name, date_birth, id_chess, player_points=0):
        self.name = name
        self.first_name = first_name
        self.date_birth = date_birth
        self.id_chess = id_chess
        self.player_points = player_points




class Controllers:

    def __init__(self):
        pass

    def get_players(self):
        pass



class Match:

    def __init__(self, match_score=0, score=0):
        self.match_score = match_score
        self.score = score

    def winner_match(self, Player, score=0):
        self.score = score
        return f"Le gagnant est {Player.name}"

    def play_game(self):
        self.match_score = 9


class Score:

    def __init__(self):
        pass

    def update_points(self, player_points, Match):
        update = player_points + Match.play_game()
        return update



#player1 = Player("Potter", "Harry", "07/31/1980", "HP12345")
print("Base de point, joueur :", Player.name, Player.player_points)
#print(player1.name, player1.first_name, player1.date_birth, player1.id_chess, player1.player_points)

#print(player3.player_points)

match = Match()
score = Score()

print("Match :", match.winner_match(Player), " ----- Score :", score.update_points(Player))

