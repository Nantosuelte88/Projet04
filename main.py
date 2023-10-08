

from controllers.base import Controller
from views.tournamenentview import View


def main():

    active_view = View()

    game = Controller(active_view)
    game.run()


if __name__ == "__main__":
    main()
