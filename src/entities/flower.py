import os
from random import randrange
import pygame


from src.exceptions import Exceptions
from src.entities.death_touch_entity import DeathTouchEntity
from src.entities.death_touch_entity import DeathTouchEntityInfo
from src.static_grid_cells.obstacle import Obstacle


class Flower(DeathTouchEntity):

    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy, DeathTouchEntityInfo(False, True, False, False, False))
        self.vy = 0.75
        self.collision_bottom = self.collision_top = False

    def process_logic(self):
        if (self.rect.bottom >= 576):
            self.vy = -abs(self.vy)
        elif (self.rect.top <= 384):
            self.vy = abs(self.vy)

    def on_collide(self, collisions):
        pass

