import os
import pygame
from pygame.examples.aliens import Player

import images
#from src.level import Level
from src.static_grid_cell import StaticGridCell

class Coin(StaticGridCell):
    def __init__(self, game, image, locx, locy):
        pass

    def coin_get(self):
       self.process_change_coins(self, 1)
       #Level.delete_static_grid_cell(self.locx, self.locy)

    def process_logic(self):
        def on_collide(self, collisions):
            for collision in collisions:
                if isinstance(collision.opp_rb, Player): self.coin_get()
