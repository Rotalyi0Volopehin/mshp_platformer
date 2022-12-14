import random

from src.arch.game import Game
from src.menu import Menu


def main():
    random.seed()
    Game.library_init()
    menu = Menu()
    height = menu.height
    width = menu.width
    while not menu.quit:
        menu.show()
        if not menu.quit:
            g = Game(width, height)
            g.main_loop()
            menu.m_quit = False
            menu.quit = g.pr_quit

if __name__ == '__main__':
    main()