import os

IMAGES_DIR = 'images_blank'
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами


class Color:
    BLACK = [0, 0, 0]
    RED = [255, 0, 0]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]
    BOLD = [88, 88, 88]


class PLT:
    S = []


class ENT:
    S = []


class Stats:
    MOVE_SPEED = 5
    WIDTH = 64
    HEIGHT = 64
    JUMP_POWER = 10
    GRAVITY = 1.2  # Сила, которая будет тянуть нас вниз


class Display:
    WIDTH = 800  # Ширина создаваемого окна
    HEIGHT = 640  # Высота
    SIZE = (WIDTH, HEIGHT)  # Группируем ширину и высоту в одну переменную