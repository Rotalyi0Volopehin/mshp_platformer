import os
from random import randrange
import pygame

from src.Tube import Tube
from src.base_classes import DrawableObject
from src.constants import IMAGES_DIR


class Flower(DrawableObject):
    image = pygame.image.load(os.path.join(IMAGES_DIR, 'flower.png'))

    def __init__(self, game_object, start_pos):
        super().__init__(game_object)
        self.rect = self.image.get_rect()
        self.rect.x = start_pos[0]  # x как у трубы
        self.rect.y = start_pos[1]  # y на размер(32 пикселя?) ниже, чем у трубы
        self.shift_y = 0.2 if randrange(0, 2) == 1 else -0.2

    def process_logic(self):
        if (self.rect.y <= self.start_pos[1]) or (self.rect.y >= (self.start_pos[1]+32)):
            self.shift_y *= -1