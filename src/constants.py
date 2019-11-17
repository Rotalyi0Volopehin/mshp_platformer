import os

IMAGES_DIR = 'images'
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами


class Colors:
    BLACK = [0, 0, 0]
    RED = [255, 0, 0]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]
    BOLD = [88, 88, 88]
    PLATFORM_COLOR = [255, 62, 62]


class Level:
    test_level = [
        "-                                                              -",
        "-                                                              -",
        "-                                                              -",
        "-                                                              -",
        "-                                                              -",
        "-                                                              -",
        "-                                                              -",
        "-                        ----------                            -",
        "-            ----                                              -",
        "-                                                              -",
        "-                                                              -",
        "-             ----    --                                       -",
        "-                                 --- --- --                   -",
        "-                                                              -",
        "-                                               ---------      -",
        "-         -------                        ---                   -",
        "-                                                              -",
        "----------------------------------------------------------------",
 ]


class Stats:
    MOVE_SPEED = 7
    WIDTH = 32  # 64
    HEIGHT = 32  # 64
    JUMP_POWER = 10
    GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз


class PLATFORM:
    WIDTH = 32  # 64
    HEIGHT = 32  # 64
    S = []


class Display:
    WIDTH = 800  # Ширина создаваемого окна
    HEIGHT = 640  # Высота
    SIZE = (WIDTH, HEIGHT)  # Группируем ширину и высоту в одну переменную