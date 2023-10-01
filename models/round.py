

class Round:
    """ un round contient une liste des matchs, un nom, une date et une heure de début, une date et une heure de fin """

    def __init__(self, name_round):
        self.name_round = name_round
        self.round_start = "round_start" # déclaration automatique lors du début
        self.round_end = "round_end" # déclaration automatique lors de la fin
        self.list_matches = [] # La liste des matchs de ce round
        self.start_time = "start_time"
        self.end_time = "end_time"
    def __str__(self):
        return f" Nom du round : {self.name_round} . " \
               f"Date de début : {self.round_start} . " \
               f"Date de fin : {self.round_end} . " \
               f"MATCH : {self.list_matches}"



"""
    def modification_player(self):
        check = False
        no_player = []
        found_name = []
        good_player = []

        # Prochaine version du select joueur
        while True:
            u = 0
            player_name = self.view.show_player(check)
            players_json = self.search_players_json()
            for player in players_json:
                print("print index =", player)
                player_index = players_json[player]
                print("player index=", player_index)
                print(u, "name ?", player_index["name"])
                u += 1
                if player_name == player_index["name"]:
                    print("correspondance!", player_name, " et ", player_index["name"])
                    found_name.append(player_index)
                else:
                    no_player.append(player)

            if len(found_name) > 1:
                print("sup à 1 = ", len(found_name))
                check_player = self.view.choose_players(found_name)
                print("!!!", check_player, "!!!!", players_json)
                for player_details in players_json.values():
                    if check_player == player_details:
                        print("id correspondant", player_details["name"], player_details["first_name"],
                              player_details["id_chess"])
                        good_player.append(player_details)
                    else:
                        print("player non correspondant", check_player, "!=", player_details["name"])
                        no_player.append(player_details)
            elif len(found_name) == 1:
                print("egal à 1 = ", len(found_name))
                good_player.append(found_name)
            else:
                print("pas de joueur à ce nom")
                check = True

            if len(no_player) == len(players_json):
                print("joueur inconnu!", no_player)
                check = True
            else:
                print("le joueur est ok", no_player)
                break

        print("verif de check ->", check)
        if not check:
            print(good_player)
            if len(good_player) == 1:
                print("un seul joueur ok", good_player)
            elif len(good_player) > 1:
                print("plusieurs joueurs dedans", good_player)
        print("FIN BOUCLE MODIF\n joueur ? =", good_player[0][0])

        # Fin version select !!!
        p = 0
        for player in players_json:
            print(p, players_json[player])
            p += 1
            if good_player[0][0] == players_json[player]:
                print("bon joueur")
                new_info = self.view.modification_player(players_json[player])
                print(new_info)
                if new_info[0] == "1":
                    print("nouveau nom", new_info[1])
                    players_json[player]["name"] = new_info[1]
                elif new_info[0] == "2":
                    print("nouveau prenom", new_info[1])
                    players_json[player]["first_name"] = new_info[1]
                elif new_info[0] == "3":
                    print("nouvelle date de naissance", new_info[1])
                    players_json[player]["date_birth"] = new_info[1]
                elif new_info[0] == "4":
                    print("nouvel id", new_info[1])
                    players_json[player]["id_check"] = new_info[1]
            else:
                print("mauvais joueur")
        with open("data/players.json", "w") as my_file:
            json.dump(players_json, my_file, indent=4)
        print("fin de modif")

"""























