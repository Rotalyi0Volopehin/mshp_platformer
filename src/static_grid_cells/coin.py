import os
import pygame

import images
from src.level import Level
from src.static_grid_cell import StaticGridCell

class Coin(StaticGridCell):
    image = pygame.image.load(os.path.join(images, 'coin.xcf'))
    def __init__(self, game, image, locx, locy):
        pass

    def coin_get(self):
       self.process_change_coins(self, 1)
       Level.delete_static_grid_cell(self.locx, self.locy)

    def process_logic(self):
       if is_collision():
       self.coin_get()
