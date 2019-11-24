from src.level import Level
from src.static_grid_cells import coin
from src.static_grid_cells.brick_cell import BrickCell


class Question(BrickCell):
    def __init__(self, game, image, locx, locy):
        # super(StaticGridCell, self).__init__(self, game, image, locx, locy)
        super().__init__(game, image, locx, locy)
        self.x = 0

    def process_logic(self):
        if self.bottom() and (self.x == 0): self.Summon()

    def Summon(self):
        #if randrange(0,3)==0: add_new_entity(mushroom,)
        #else:
        Level.add_new_static_grid_cell(coin, self, self.locx, self.locy+64)
        self.x = 1