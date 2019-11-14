import os
from random import randrange
import pygame

from src.base_classes import DrawableObject
from src.constants import IMAGES_DIR


class Tube(DrawableObject):

    def __init__(self, game_object, start_pos, typpe = 0):
        super().__init__(game_object)
        self.rect = self.image.get_rect()
        self.rect.x = start_pos[0]  # x
        self.rect.y = start_pos[1]  # y
        self.typpe = typpe
        if typpe == 0:
            image = pygame.image.load(os.path.join(IMAGES_DIR, 'tube0.png'))  # верняя часть трубы
        if typpe == 1:
            image = pygame.image.load(os.path.join(IMAGES_DIR, 'tube1.png'))  # нижняя часть трубы

    def process_draw(self):
        self.game_object.screen.blit(self.image, self.rect)