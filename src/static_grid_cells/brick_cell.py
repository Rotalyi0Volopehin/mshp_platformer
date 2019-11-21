from src.static_grid_cell import StaticGridCell


class BrickCell(StaticGridCell):
    def __init__(self, game, image, locx, locy):
        super().__init__(game, image, locx, locy)