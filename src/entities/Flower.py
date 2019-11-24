import os
from random import randrange
import pygame

from src.constants import IMAGES_DIR
from src.entity import Entity
from src.exceptions import Exceptions

class Flower(Entity):
    #image = pygame.image.load(os.path.join(IMAGES_DIR, 'flower1.xcf'))

    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy)
        self.vy = 1
        self.startposy = posy
        if not (isinstance(image, pygame.Surface) and isinstance(posx, int) and isinstance(posy, int)):
            Exceptions.throw(Exceptions.argument_type)

    def process_logic(self):
        print(self.posy_carry,self.rect.y)
        self.rect.y += int(self.vy)
        self.posy_carry += self.__calc_carry(self.vy)
        if (self.rect.y <= self.startposy) or (self.rect.y >= (self.startposy+127)):
            self.vy *= -1

    def apply_gravity_force(self, value):
        self.vy += value

    def __calc_carry(self, value):
        sign = (value > 0) - (value < 0)
        return abs(value) % 1 * sign