import os
from random import randrange
import pygame

from src.base_classes import DrawableObject
from src.constants import Color


class Text(DrawableObject):
    pygame.font.init()

    def __init__(self, game):
        super().__init__(game)
        self.start_time = 400
        self.start_ticks = pygame.time.get_ticks()
        self.seconds = 0
        self.time_is_over = False
        self.font = pygame.font.SysFont('Comic Sans MS', 45, True)

    def process_draw(self, screen):
        ts = self.font.render(str(400 - self.seconds), False, (255, 255, 255))
        ts2 = self.font.render('Time', False, (255, 255, 255))
        self.game.screen.blit(ts, (650, 50))
        self.game.screen.blit(ts2, (640, 20))

    def process_logic(self):
        self.seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000
        if (self.seconds > 400):
            self.time_is_over = True
