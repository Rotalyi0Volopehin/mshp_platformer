import pygame

from src.exceptions import Exceptions
from src.arch.rigid_body import RigidBody


# Это ячейка статической сетки
class StaticGridCell(RigidBody): #abstract
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

    def disappear(self):
        self.level.delete_static_grid_cell(self.locx, self.locy)