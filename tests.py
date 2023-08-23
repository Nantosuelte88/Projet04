def result_round(self, round):
    for match in round:
        print("\nMatch = ", match.result_match)
        if match.score1 == 1:
            print("Le gagnant est p1", match.player1[0], match.player1[1])
            for player in self.player_with_score:
                if player[0] == match.player1:
                    test = player[1]
                    for player_info in player:
                        print("Dans la boucle player_info", player_info)
                # test_choix_du_joueur = self.player_with_score[] # comment lui indiquer de chercher dans les infos de ce joeur
        #               print("TCHUUUK correspondance PLAYER 1", match.player1,"TEST 1 :", test_choix_du_joueur, "TEEEEST :", test)
        elif match.score2 == 1:
            print("Le gagnant est p2", match.player2[0], match.player2[1])
            for player in self.player_with_score:
                if player[0] == match.player2:
                    # il ne rentre jamais içi
                    test2 = player[1]
                    print("!!!! corresponcance PLAYER 2", match.player2, "TEST 2 :", test2)

        else:
            if match.player1 or match.player2 == self.player_with_score:
                print("LEs DEUX correspondent !!!", match.score1)
            print("Match nul pour ", match.player1[0], match.player1[1], "et ", match.player2[0], match.player2[1])


def result_round(self, round):
    for match in round:
        print("\nMatch = ", match.result_match)
        if match.score1 == 1:
            print("Le gagnant est p1", match.player1[0], match.player1[1])
            for player in self.player_with_score:
                if player[0] == match.player1:
                    test = player[1]
                    print("TCHUUUK correspondance PLAYER 1", match.player1, "TEST 1 :", test)
        elif match.score2 == 1:
            print("Le gagnant est p2", match.player2[0], match.player2[1])
            for player in self.player_with_score:
                if player[0] == match.player2:
                    test2 = player[1]
                    print("!!!! corresponcance PLAYER 2", match.player2, "TEST 2 :", test2)
                else:
                    print("Pas de correspondance dans Player 2", player[0])
        else:
            if any(player[0] == match.player1 or player[0] == match.player2 for player in self.player_with_score):
                print("LEs DEUX correspondent !!!", match.score1)
            print("Match nul pour ", match.player1[0], match.player1[1], "et ", match.player2[0], match.player2[1])






for match in round:
    print("\nMatch = ", match.result_match)
    if match.score1 == 1:
        print("Le gagnant est p1", match.player1[0], match.player1[1])
    elif match.score2 == 1:
        print("Le gagnant est p2", match.player2[0], match.player2[1])
    else:
        print("Match nul pour ", match.player1[0], match.player1[1], "et ", match.player2[0], match.player2[1])
        print("\n[0] = ", self.player_with_score[a][0], "Player :", match.player1, "FFIIN\n")
        if match.player1 == self.player_with_score[a][0]:
            print("TCHUUUK PLAYER 1")
        elif match.player2 == self.player_with_score[a][0]:
            print("!!!! PLAYER 2")
        else:
            print("MATCH NUL !!!")







for i in range(0, len(players), 2):
    player1 = players[i][0]
    score1 = players[i][1] + (+ score1_match)
    player2 = players[i + 1][0]
    score2 = players[i + 1][1] + (+ score2_match)
    matchs = Match(player1, score1, player2, score2)
    #      print(matchs)
    init_round.list_matchs.append(matchs)



self.result_matchs(init_round)


def result_matchs(self, init_round):
    for p in init_round.list_matchs:
        random.shuffle(MATCH_SCORE)
        score1 = MATCH_SCORE[0][0]
        score2 = MATCH_SCORE[0][1]
        print(init_round.list_matchs[000])
    #  print("tututu", p, score1, score2)
    print("Resultat du match")












"""



from typing import List


PlAYERS = [
    ("Potter", "Harry", "07/31/1980", "HP12345"),
    ("Granger", "Hermione", "09/19/1979", "GH12345"),
    ("Weasley", "Ron", "03/01/1980", "WR12345"),
    ("Weasley", "Ginny", "08/11/1981", "WG12345"),
    ("Malefoy", "Drago", "06/05/1980", "MD12345"),
    ("Lovegood", "Luna", "02/13/1980", "LL12345"),
    ("Londubat", "Neville", "07/30/1980", "LN12345"),
    ("Chang", "Cho", "04/24/1979", "CC12345")
]

class Player:
     #Le joueur a un nom, un prénom, une date de naissance et son identifiant d'échecs
     
     def __init__(self, name, first_name, date_birth, id_chess):
        self.name = name
        self.first_name = first_name
        self.date_birth = date_birth
        self.id_chess = id_chess



class Controller:


    def __init__(self):
        # mettre la vue içi
        self.players: List[Player] = []
        self.list_player = []

    def get_players(self):
        player_info = PlAYERS
        for i in player_info:
            player = Player(i[0], i[1], i[2], i[3])
            self.players.append(player)
            self.list_player.append([player.name, player.first_name, player.date_birth, player.id_chess])

    def __str__(self):
        return f"test info du joueur dans controlleur {self.list_player}"


test = Controller()
test.get_players()
print(test)




















class Joueur:
    def __init__(self, nom, score):
        self.nom = nom
        self.score = score

    def __str__(self):
        return f"Nom: {self.nom}\nScore: {self.score}\n"


class Match:
    def __init__(self, joueur1, score1, joueur2, score2):
        self.joueur1 = joueur1
        self.score1 = score1
        self.joueur2 = joueur2
        self.score2 = score2

    def __str__(self):
        return f"Match:\n{self.joueur1.nom} ({self.score1}) vs {self.joueur2.nom} ({self.score2})"


class Tournoi:
    def __init__(self, joueurs):
        self.joueurs = [Joueur(nom, score) for nom, score in joueurs]
        self.matchs = []

    def ajouter_match(self, match):
        self.matchs.append(match)

    def afficher_joueurs(self):
        for joueur in self.joueurs:
            print(joueur)

    def afficher_matchs(self):
        for match in self.matchs:
            print(match)

class System_game:

    def match_result(self):
        self.matchs = []



JOUEURS = [
    ("Potter", 0),
    ("Granger", 0),
    ("Weasley", 0),
    ("Weasley", 0),
    ("Malefoy", 0),
    ("Lovegood", 0),
    ("Londubat", 0),
    ("Chang", 0)
]

tournoi = Tournoi(JOUEURS)

match1 = Match(tournoi.joueurs[0], 6, tournoi.joueurs[1], 8)
match2 = Match(tournoi.joueurs[0], 3, tournoi.joueurs[2], 2)

tournoi.ajouter_match(match1)
tournoi.ajouter_match(match2)

tournoi.afficher_joueurs()
tournoi.afficher_matchs()








JOUEURS = [
    ("Potter", 0),
    ("Granger", 0),
    ("Weasley", 0),
    ("Weasley", 0),
    ("Malefoy", 0),
    ("Lovegood", 0),
    ("Londubat", 0),
    ("Chang", 0)
]



def generer_matchs(joueurs):
    matchs = []

    match_number = len(joueurs)

    for i in match_number :
        joueur1 = joueurs[0]
        joueur2 = joueurs[1]
        matchs.append((joueur1, joueur2))


    return matchs


matchs = generer_matchs(JOUEURS)

for index, match in enumerate(matchs, start=1):
    joueur1, joueur2 = match
    print(f"Match {index}: {joueur1[0]} vs {joueur2[0]}")
"""





