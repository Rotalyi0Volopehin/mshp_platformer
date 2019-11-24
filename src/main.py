from src.game import Game
from src.menu import Menu


def main():
    menu = Menu()
    menu.show()
    height = menu.height
    width = menu.width
    g = Game(width, height)
    g.main_loop()


if __name__ == '__main__':
    main()
