import os
from random import randrange
import pygame

from src.base_classes import DrawableObject
from src.constants import IMAGES_DIR
from src.static_grid_cells import StaticGridCell


class Tube(StaticGridCell):

    def __init__(self, game, image, locx, locy, typpe):
        super().__init__(game, image, locx, locy)
        self.typpe = typpe
        if typpe == 0:
            image = pygame.image.load(os.path.join(IMAGES_DIR, 'tube0.png'))  # верняя часть трубы
        if typpe == 1:
            image = pygame.image.load(os.path.join(IMAGES_DIR, 'tube1.png'))  # нижняя часть трубы

    def process_draw(self):
        self.game_object.screen.blit(self.image, self.rect)