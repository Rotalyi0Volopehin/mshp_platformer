import os
#from src.level import Level

from pygame.examples.aliens import Player
from src.static_grid_cells import coin
from src.static_grid_cell import StaticGridCell


class Question(StaticGridCell):
    def __init__(self, game, image, locx, locy):
        # super(StaticGridCell, self).__init__(self, game, image, locx, locy)
        super().__init__(game, image, locx, locy)
        self.x = 0

    def process_logic(self):
        def on_collide(self, collisions):
            for collision in collisions:
                if isinstance(collision.opp_rb, Player) and collision.bottom and self.x==0 : self.Summon()

    def Summon(self):
        #if randrange(0,3)==0: add_new_entity(mushroom,)
        #else:
        #Level.add_new_static_grid_cell(coin, self, self.locx, self.locy+64)
        self.x = 1