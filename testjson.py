"""
    ("Chang", "Cho", "04/24/1979", "CC12345")

players = {
    "name": "Granger",
    "fisrt_name": "Hermione",
    "date_birth": "09/19/1979",
    "id_chess": "GH12345"
}

import json

players = []
data_players = [
    ("Potter", "Harry", "07/31/1980", "HP12345"),
    ("Granger", "Hermione", "09/19/1979", "GH12345"),
    ("Weasley", "Ron", "03/01/1980", "WR12345"),
    ("Weasley", "Ginny", "08/11/1981", "WG12345"),
    ("Malefoy", "Drago", "06/05/1980", "MD12345"),
    ("Lovegood", "Luna", "02/13/1980", "LL12345"),
    ("Londubat", "Neville", "07/30/1980", "LN12345"),
]

for player in data_players:
    print(player[0], player[1], player[2], player[3])
    dict_player = {
        "name": player[0],
        "first_name": player[1],
        "date_birth": player[2],
        "id_chess": player[3],
    }
    players.append(dict_player)
    print("print dans boucle", players)

with open("players.json", "w") as my_file:
    json.dump(players, my_file)


    import json

tournaments = []
data_tournament = [
    ("Massacre Match", "Marseille", "07/31/1980"),
    ("Battle Blitz", "Amiens", "09/19/1979"),
    ("Infinite Invitational", "Paris", "03/01/1980")
]


for player in data_tournament:
    print(player[0], player[1], player[2])
    dict_player = {
        "name_tournament": player[0],
        "locality": player[1],
        "start_date": player[2],
        "list_rounds": [],
        "list_players": []
    }
    tournaments.append(dict_player)
    print("print dans boucle", tournaments)

with open("tournament.json", "w") as my_file:
    json.dump(tournaments, my_file)



import json
import os

file_path_tournament = "data/tournament.json"
i = 0
if os.path.exists(file_path_tournament):
    print("le fichier existe")
    if os.path.getsize(file_path_tournament) > 0:
        print("ya des trucs dans le fichier")
        file_object = open(file_path_tournament, "r")
        json_content = file_object.read()
        tournaments_data = json.loads(json_content)


        if isinstance(tournaments_data, list):
            for tournament in tournaments_data:
                if "tournament" in tournament:
                    tournament_data = tournament["tournament"]
                    for tournament_key in tournament_data.keys():

                        list_players = tournament_data[tournament_key]["list_players"]

                        print(f"Liste des joueurs pour le tournoi {tournament_key}:")
                        print(list_players)
                else:
                    print("Le format du fichier JSON n'est pas correct.")
        else:
            print("Le fichier est vide.")
    else:
       print("Le fichier n'existe pas.")
"""
import json
import os

file_path_tournament = "data/tournament.json"

if os.path.exists(file_path_tournament):
    print("Le fichier existe")
    if os.path.getsize(file_path_tournament) > 0:
        print("Il y a des données dans le fichier")
        with open(file_path_tournament, "r") as file_object:
            tournaments_data = json.load(file_object)

        # Assurez-vous que tournaments_data est une liste
        if isinstance(tournaments_data, list):
            for tournament_data in tournaments_data:
                if "tournament" in tournament_data:
                    tournament_dict = tournament_data["tournament"]

                    # Parcourez les clés du dictionnaire "tournament"
                    for tournament_key in tournament_dict.keys():
                        tournament_info = tournament_dict[tournament_key]
                        list_players = tournament_info["list_players"]
                        print(list_players)
                else:
                    print("Le format du fichier JSON n'est pas correct.")
    else:
        print("Le fichier est vide.")
else:
    print("Le fichier n'existe pas.")