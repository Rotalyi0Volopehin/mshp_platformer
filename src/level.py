import glob
import pygame

from src.static_grid import StaticGrid
from src.entity import Entity
from src.io_tools import IO_Tools
from src.entity_set import EntitySet

# Уровень и информация о нём
# Каждый уровень в папке levels имеет свою папку, название которой должно быть "level_*" (* - параметр name)
# Пример создания : Level(game, "0")
class Level:
    def __init__(self, game, name):
        self.images = { }
        slash = IO_Tools.sep_slash()
        lvl_path = "levels{1}level_{0}{1}".format(name, slash)
        sprites_dir = "{}sprites{}".format(lvl_path, slash)
        for img_path in glob.glob(sprites_dir + "*.png"):
            image = pygame.image.load(img_path)
            img_rect = image.get_rect()
            if (img_rect.width == 64) and (img_rect.height == 64):
                img_name = img_path[img_path.rfind(slash) + 1 : img_path.rfind('.')]
                self.images[img_name] = image
        self.background = pygame.image.load(lvl_path + "background.png")
        lvl_file = open(lvl_path + "struct.txt")
        lvl_struct_lines = lvl_file.readlines()
        lvl_file.close()
        for i in range(len(lvl_struct_lines)):
            lvl_struct_lines[i] = lvl_struct_lines[i].strip("\n\r")
        self.grid = StaticGrid(game, self, lvl_struct_lines, self.images)
        game.objects.append(self.grid)
        self.entity_set = EntitySet(game, self, lvl_struct_lines, self.images)
        game.objects.append(self.entity_set)
