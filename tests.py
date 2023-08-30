if player2 == match.result_match[0][0] or player2 == match.result_match[1][0]:
    print("\n -- CORRESPONDANCE! -- \n", "player2 = ", player2, "\nmatchresult[0][0] = ",
          match.result_match[0][0], "\nmatchresult[0][1]= ", match.result_match[1][0], "\n")
    player2_next = players[player + 2][0]
    print("TEST CHELOU", "\nplayer2", player2, "\nplayer2 +1", player2_next, "\n\n")
    a += 1






def find_match(player, potential_opponents, played_matches):
    for opponent in potential_opponents:
        if opponent[0] != player[0] and (player[0], opponent[0]) not in played_matches and (opponent[0], player[0]) not in played_matches:
            return opponent
    return None

played_matches = set()

for i, player in enumerate(sorted_players):
    potential_opponents = [p for p in sorted_players[i + 1:] if p[1] == player[1]]
    match = find_match(player, potential_opponents, played_matches)
    if match:
        played_matches.add((player[0], match[0]))
        played_matches.add((match[0], player[0]))
        match = Match(player[0], 0, match[0], 0)
        init_round.list_matchs.append(match)


















from itertools import combinations
import random

ROUND_NUMBER : 4
MATCH_SCORE = [(1, 0), (0.5, 0.5), (0, 1)]


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



class Match:
    """ un match contient un tuple ayant deux listes contenant chacune - un joueur et - un score"""

    def __init__(self, player1, score1, player2, score2):
        self.player1 = player1
        self.score1 = score1
        self.player2 = player2
        self.score2 = score2

        self.result_match = ([player1, score1], [player2, score2])


class Round:
    """ un round contient une liste des matchs, un nom, une date et une heure de début, une date et une heure de fin """

    def __init__(self, name_round):
        self.name_round = name_round
        self.round_start = "round_start" # déclaration automatique lors du début
        self.round_end = "round_end" # déclaration automatique lors de la fin
        self.list_matchs = [] # La liste des matchs de ce round


class Tournament:
    # ... autres méthodes et attributs ...

    def new_round(self, tournament):
        for round in range(ROUND_NUMBER):
            init_round = Round("Round " + str(round + 1))
            tournament.list_rounds.append(init_round)

            if init_round.name_round == "Round 1":
                random.shuffle(tournament.list_players)
                players = tournament.list_players
            else:
                players = self.generate_new_match_pairs(tournament.list_players, init_round.list_matchs)
                for player in range(0, len(players), 2):
                    random.shuffle(MATCH_SCORE)
                    player1 = players[player][0]
                    score1 = MATCH_SCORE[0][0]
                    player2 = players[player + 1][0]
                    score2 = MATCH_SCORE[0][1]
                    match = Match(player1, score1, player2, score2)
                    init_round.list_matchs.append(match)
                #               print("PLAYER 1 = ", player1, "score 1 = ", score1,"\nPLAYER 2 = ", player2, "score 2 = ", score2)
                #          print(match.result_match)
                #        print("Liste des matchs = ", init_round.list_matchs)
                self.result_round(init_round.list_matchs, tournament)
            # Reste du code pour la création des matchs et la gestion des scores

    def generate_new_match_pairs(self, players, previous_matches):
        remaining_players = set(players)
        new_pairs = []

        for match in previous_matches:
            remaining_players.discard(match.player1)
            remaining_players.discard(match.player2)

        while len(remaining_players) >= 2:
            player_combinations = list(combinations(remaining_players, 2))
            valid_pairs = []

            for pair in player_combinations:
                if pair[0] != pair[1]:
                    valid_pairs.append(pair)

            if not valid_pairs:
                break

            selected_pair = valid_pairs[0]
            new_pairs.append(selected_pair)
            remaining_players.discard(selected_pair[0])
            remaining_players.discard(selected_pair[1])

        return new_pairs


"""
 
 
 
 
 
 
            for i in range(0, len(players), 2):
                random.shuffle(MATCH_SCORE)
                score1_match = MATCH_SCORE[0][0]
                score2_match = MATCH_SCORE[0][1]
                player1 = players[i][1]
                score1 = players[i][1] + (score1_match)
                player2 = players[i + 1][0]
                score2 = players[i + 1][1] + (score2_match)
                matchs = Match(player1, score1, player2, score2)
                #      print(matchs)
                init_round.list_matchs.append(matchs)
   #             print(matchs)
      #      print("PRINT liste des maths dans init_round", init_round.list_matchs)
            print("Résultat du", init_round.name_round)
            self.result_round(init_round, tournament)
 #           self.update_score_round(init_round)
        return


    def result_round(self, round, tournament):
   #     player_score_tournament = [list(player) for player in self.player_with_score] # pour créer un liste à part
        for match in round:
            print("\nMatch = ", match.result_match)
            for player in tournament.list_players:
                if player[0] == match.player1:
                    player[1] += match.score1
                elif player[0] == match.player2:
                    player[1] += match.score2


            #       print("§§§§§§§§", result_round_scores,self.player_with_score)

      #      print(self.player_with_score)
      #          print("Le Gagnant est :", )
       #     elif match.score2 == 1:
         #       print("Bravo", match.player2)


    def update_score_round(self, round):
        pass


















def add_scores(self, score_tournament):
    updated_list_players = []  # Nouvelle liste pour stocker les informations mises à jour

    for player_info in self.list_players:
        player_info_without_score = player_info[:-1]  # Exclure le score actuel du joueur
        updated_player_info = player_info_without_score + [score_tournament]  # Ajouter le nouveau score
        updated_list_players.append(updated_player_info)  # Ajouter à la nouvelle liste

    self.list_players = updated_list_players  # Remplacer la liste existante par la nouvelle liste mise à jour

# Utilisation de la fonction add_scores pour ajouter un score à tous les joueurs
score_tournament = 10  # Remplacez cela par le score réel du tournoi
self.add_scores(score_tournament)







            if match.score1 == 1:
                print("Le gagnant est p1", match.player1[0], match.player1[1])
                for i, player in enumerate(self.list_players):
          #          print(self.list_players[i])
                    if player[0] == match.player1:
                        print(self.list_players[5])
               #         self.player_with_score[i] = (player[0], player[1] + 1)
           #             player_score_tournament[i] = (player[0], player[1] + 1)
                        print("Test nouvelle boucle", "\nPlayer with score = ", self.player_with_score[i], "\n")
                       # test_choix_du_joueur = self.player_with_score[] # comment lui indiquer de chercher dans les infos de ce joeur
         #               print("TCHUUUK correspondance PLAYER 1", match.player1,"TEST 1 :", test_choix_du_joueur, "TEEEEST :", test)
                    else:
                        print("NOPE else, P1 pas de correspondance")
            elif match.score2 == 1:
                print("Le gagnant est p2", match.player2[0], match.player2[1])
                for i, player in enumerate(self.player_with_score):
                    if player[0] == match.player2:
                        self.player_with_score[i] = (player[0], player[1] + 1)
                        print("!!!! corresponcance PLAYER 2", match.player2,"TEST 2 :", self.player_with_score[i], "\n")

            else:
                if match.player1 or match.player2 == self.player_with_score:
                    print("LEs DEUX correspondent !!!", match.score1)
#                print("Match nul pour ", match.player1[0], match.player1[1], "et ", match.player2[0], match.player2[1], "MAtch nul score = ", self.player_with_score)












from typing import List

from models.player import Player
from models.tournament import Tournament
from models.match import Match
from models.round import Round

from dataplayers import PlAYERS

import random

ROUND_NUMBER = 4
MATCH_SCORE = [(1, 0), (0.5, 0.5), (0, 1)]
MATCHS = 4
class Controller:


    def __init__(self):
        # mettre la vue içi
        self.players: List[Player] = []
        self.list_players = []
        self.player_with_score = []


    def get_players(self):
        player_info = PlAYERS
        for i in player_info:
            player = Player(i[0], i[1], i[2], i[3])
            self.players.append(player)
            self.list_players.append([player.name, player.first_name, player.date_birth, player.id_chess])
#        print("Print - get_player dans Controller - Len list_player :", len(self.list_players))


    def __str__(self):
        return f"test info du joueur dans controlleur {self.list_players}"



    def new_tournament(self):
        info_tournament = Tournament("Tournoi des Sorciers", "15 juillet", "Poudlard")
        info_tournament.list_players = self.list_players
#        print(info_tournament)
        score = 0
        for player in self.list_players:
            self.player_with_score.append([player, score])
 #       print(self.player_with_score)
        # verifier si il est mieux de ne prendre que l'id et le score ou garder les autres infos du joueur en stock içi ???
        return info_tournament, self.player_with_score


    def update_score(self):
        pass


    def new_round(self):
        for round in range(ROUND_NUMBER):
            init_round = Round("Round " + str(round +1))
            print(init_round.name_round)
            if init_round.name_round == "Round 1":
                players = self.player_with_score
                random.shuffle(players)
            #    print("PREMIER ROUND", players)
            else:
                # Trouver comment faire en sorte que les joueurs ne rejouent pas direct entre eux
                players = sorted(self.player_with_score, key= lambda x: x[1], reverse=True)
            #    print("PAS LE PREMIER ROUND", init_round.name_round, players)

            for i in range(0, len(players), 2):
                random.shuffle(MATCH_SCORE)
                score1_match = MATCH_SCORE[0][0]
                score2_match = MATCH_SCORE[0][1]
                player1 = players[i][0]
                score1 = players[i][1] + (score1_match)
                player2 = players[i + 1][0]
                score2 = players[i + 1][1] + (score2_match)
                matchs = Match(player1, score1, player2, score2)
                #      print(matchs)
                init_round.list_matchs.append(matchs)
   #             print(matchs)
      #      print("PRINT liste des maths dans init_round", init_round.list_matchs)
            print("Résultat du", init_round.name_round)
            self.result_round(init_round.list_matchs)
 #           self.update_score_round(init_round)
        return init_round #ne retourne que le PREMIER ROUND !!! ATTENTION !!


    def result_round(self, round):
   #     player_score_tournament = [list(player) for player in self.player_with_score] # pour créer un liste à part
        for match in round:
            print("\nMatch = ", match.result_match)
            if match.score1 == 1:
                print("Le gagnant est p1", match.player1[0], match.player1[1])
                for i, player in enumerate(self.player_with_score):
                    if player[0] == match.player1:
                        self.player_with_score[i] = (player[0], player[1] + 1)
           #             player_score_tournament[i] = (player[0], player[1] + 1)
                        print("Test nouvelle boucle", "\nPlayer with score = ", self.player_with_score[i], "\n")
                       # test_choix_du_joueur = self.player_with_score[] # comment lui indiquer de chercher dans les infos de ce joeur
         #               print("TCHUUUK correspondance PLAYER 1", match.player1,"TEST 1 :", test_choix_du_joueur, "TEEEEST :", test)
            elif match.score2 == 1:
                print("Le gagnant est p2", match.player2[0], match.player2[1])
                for i, player in enumerate(self.player_with_score):
                    if player[0] == match.player2:
                        self.player_with_score[i] = (player[0], player[1] + 1)
                        print("!!!! corresponcance PLAYER 2", match.player2,"TEST 2 :", self.player_with_score[i], "\n")

            else:
                if match.player1 or match.player2 == self.player_with_score:
                    print("LEs DEUX correspondent !!!", match.score1)
                print("Match nul pour ", match.player1[0], match.player1[1], "et ", match.player2[0], match.player2[1], "MAtch nul score = ", self.player_with_score)


            #       print("§§§§§§§§", result_round_scores,self.player_with_score)

      #      print(self.player_with_score)
      #          print("Le Gagnant est :", )
       #     elif match.score2 == 1:
         #       print("Bravo", match.player2)


    def update_score_round(self, round):
        pass



    def run(self):
        self.get_players()
        print("Run")

        self.new_tournament()

        self.new_round()








    #    print(new_round)































































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





