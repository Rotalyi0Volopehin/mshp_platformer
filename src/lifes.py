import os
import pygame

from src.base_classes import DrawableObject


class Life(DrawableObject):

    def __init__(self, game_object):
        super().__init__(game_object)
        self.rheart_surf = pygame.image.load("images/redh.png")
        self.gheart_surf = pygame.image.load("images/greyh.png")
        self.lifes = 3
        self.y = 35
        self.shift_x = 50

    def process_change_lifes(self, value):  #TODO при смерти игрока передать в value 1 (или количество жизней, но убрать минус строчкой ниже)
        self.lifes -= value


    def process_draw(self):
        if self.lifes >= 3:
            self.game_object.screen.blit(self.rheart_surf, [800, 35])
            self.game_object.screen.blit(self.rheart_surf, [830, 35])
            self.game_object.screen.blit(self.rheart_surf, [860, 35])
        if self.lifes == 2:
            self.game_object.screen.blit(self.rheart_surf, [800, 35])
            self.game_object.screen.blit(self.rheart_surf, [830, 35])
            self.game_object.screen.blit(self.gheart_surf, [860, 35])
        if self.lifes == 1:
            self.game_object.screen.blit(self.rheart_surf, [800, 35])
            self.game_object.screen.blit(self.gheart_surf, [830, 35])
            self.game_object.screen.blit(self.gheart_surf, [860, 35])
        if self.lifes <= 0:
            self.game_object.screen.blit(self.gheart_surf, [800, 35])
            self.game_object.screen.blit(self.gheart_surf, [830, 35])
            self.game_object.screen.blit(self.gheart_surf, [860, 35])