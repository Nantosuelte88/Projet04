

from controllers.base import Controller


def main():

    game = Controller()
    game.run()
    game.new_tournament()
    players_with_score = game.new_tournament()[1]  # totalement tiré par les cheveux -_-'
    # Penser à mettre les scores initialisé à zero seulement pour le 1er Round !
    # if round == 1:
    #     game.select_player_for_match(players_with_score)
    # else:
    #    game.select_player_for_match(update_score)
    game.sorted_players(players_with_score)


if __name__ == "__main__":
    main()

