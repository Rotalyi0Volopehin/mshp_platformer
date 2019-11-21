import os
from random import randrange
import pygame

from src.base_classes import DrawableObject
from src.constants import IMAGES_DIR
from src.static_grid_cell import StaticGridCell


class Tube(StaticGridCell):

    def __init__(self, game, image, locx, locy, typpe):
        super().__init__(game, image, locx, locy)
        self.typpe = typpe
        if typpe == 0:
            image = pygame.image.load(os.path.join(IMAGES_DIR, 'pipe.xcf'))  # верняя часть трубы
        if typpe == 1:
            image = pygame.image.load(os.path.join(IMAGES_DIR, 'pipe2.xcf'))  # нижняя часть трубы