import os
from random import randrange
import pygame

from src.base_classes import DrawableObject
from src.constants import IMAGES_DIR


class Mushroom(DrawableObject):
    image = pygame.image.load(os.path.join(IMAGES_DIR, 'mushroom.png'))

    shift_speed = 1
    shift_distance = 400

    def __init__(self, game_object, start_pos):
        super().__init__(game_object)
        self.rect = self.image.get_rect()
        self.rect.x = start_pos[0]
        self.rect.y = start_pos[1]
        self.shift_x = 1
        self.current_distance = 0

    def process_logic(self):
        self.rect.x += self.shift_x * self.shift_speed
        self.current_distance += abs(self.shift_x * self.shift_speed)
        if self.current_distance >= self.shift_distance:
            self.shift_x *= -1
            self.current_distance = 0

    def process_draw(self):
        self.game_object.screen.blit(self.image, self.rect)
