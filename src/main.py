from src.game import Game
from src.menu import Menu


def main():
    menu = Menu()

    while not menu.quit:
        menu.show()
        if not menu.quit:
            height = menu.height
            width = menu.width
            g = Game(width, height)
            g.main_loop()
            menu.m_quit = False
            menu.quit = g.pr_quit

if __name__ == '__main__':
    main()
