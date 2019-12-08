import os
from random import randrange
import pygame

from src.base_classes import DrawableObject
from src.constants import Color


class TimeGame(DrawableObject):
    pygame.font.init()

    def __init__(self, game):
        super().__init__(game)
        self.start_time = 300
        self.game_object = game
        self.start_ticks = pygame.time.get_ticks()
        self.seconds = 0
        self.font = pygame.font.SysFont('Comic Sans MS', 45, True)

    def process_draw(self):
        ts = self.font.render(str(self.start_time - self.seconds), False, (255, 255, 255))
        ts2 = self.font.render('Time', False, (255, 255, 255))
        self.game_object.screen.blit(ts, (650, 50))
        self.game_object.screen.blit(ts2, (640, 20))

    def process_logic(self):
        self.seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000
        if (self.seconds >= self.start_time):
            self.game_object.game_over = True
