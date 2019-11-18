import pygame

from src.base_classes import DrawableObject
from src.exceptions import Exceptions
from src.rigid_body import RigidBody

# Это статические игровые объекты, применяемые в классе StaticGrid

class StaticGridCell(RigidBody): #abstract
    cell_types_from_save_symbols = None

    def init():
        StaticGridCell.cell_types_from_save_symbols = { }
        StaticGridCell.cell_types_from_save_symbols['B'] = BrickCell

    def __init__(self, game, image, locx, locy):
        if not (isinstance(image, pygame.Surface) and isinstance(locx, int) and isinstance(locy, int)):
            Exceptions.throw(Exceptions.argument_type)
        rect = image.get_rect()
        rect.x = locx << 6
        rect.y = locy << 6
        super().__init__(game, rect)
        self.image = image
        self.locx = locx
        self.locy = locy

    def process_draw(self):
        self.game_object.screen.blit(self.image, self.rect)


class BrickCell(StaticGridCell):
    def __init__(self, game, image, locx, locy):
        super().__init__(game, image, locx, locy)
