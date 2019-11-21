import pygame

from src.base_classes import DrawableObject
from src.exceptions import Exceptions

# Это статические игровые объекты, применяемые в классе StaticGrid

class StaticGridCell(DrawableObject): #abstract
    cell_types_from_save_symbols = None

    def init(self):
        StaticGridCell.cell_types_from_save_symbols = { }
        StaticGridCell.cell_types_from_save_symbols['B'] = BrickCell
        StaticGridCell.cell_types_from_save_symbols['T'] = BrickCell
        StaticGridCell.cell_types_from_save_symbols['F'] = BrickCell

    def __init__(self, game, image, locx, locy):
        super().__init__(game)
        if not (isinstance(image, pygame.Surface) and isinstance(locx, int) and isinstance(locy, int)):
            Exceptions.throw(Exceptions.argument_type)
        self.image = image
        self.locx = locx
        self.locy = locy
        self.rect = image.get_rect()
        self.rect.x = locx << 6
        self.rect.y = locy << 6

    def process_draw(self):
        self.game_object.screen.blit(self.image, self.rect)


class BrickCell(StaticGridCell):
    def __init__(self, game, image, locx, locy):
        super().__init__(game, image, locx, locy)