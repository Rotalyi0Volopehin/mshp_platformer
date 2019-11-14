import glob
import pygame

from src.static_grid import StaticGrid

# Уровень и информация о нём
# Каждый уровень в папке levels имеет свою папку, название которой должно быть "level_*" (* - параметр name)
# Пример создания : Level(game, "0")
class Level:
    def __init__(self, game, name):
        self.images = { }
        lvl_path = "levels\\level_" + name + "\\"
        for img_path in glob.glob(lvl_path + "*.png"):
            image = pygame.image.load(img_path)
            img_name = img_path[img_path.rfind('\\') + 1 : img_path.rfind('.')]
            self.images[img_name] = image
        lvl_file = open(lvl_path + "struct.txt")
        lvl_struct_lines = lvl_file.readlines()
        lvl_file.close()
        for i in range(len(lvl_struct_lines)):
            lvl_struct_lines[i] = lvl_struct_lines[i].strip("\n\r")
        self.grid = StaticGrid(game, self, lvl_struct_lines, self.images)
        self.background = pygame.image.load(lvl_path + "background.png")
        game.objects.append(self.grid)