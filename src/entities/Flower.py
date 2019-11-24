import os
from random import randrange
import pygame

from src.constants import IMAGES_DIR
from src.entity import Entity
from src.exceptions import Exceptions

class Flower(Entity):
    image = pygame.image.load(os.path.join(IMAGES_DIR, 'flower1.xcf'))

    def __init__(self, game, image, posx, posy):
        self.startposy = posy
        if not (isinstance(image, pygame.Surface) and isinstance(posx, int) and isinstance(posy, int)):
            Exceptions.throw(Exceptions.argument_type)

    def apply_velocity(self):
        self.rect.y += int(self.vy)
        self.posy_carry += self.__calc_carry(self.vy)
        if (self.posy_carry <= self.startposy) or (self.posy_carry >= (self.startposy+64)):
            self.vy *= -1