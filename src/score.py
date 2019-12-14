import os
import pygame

from src.base_classes import DrawableObject
from src.constants import Color


class Score(DrawableObject):

    def __init__(self, game_object):
        super().__init__(game_object)
        self.score = 0
        self.font = pygame.font.SysFont('Comic Sans Ms', 45, True)
        self.text = 'Score'
        self.text2 = '{:0>4}'.format(self.score)
        self.ts = self.font.render(self.text, True, Color.WHITE)
        self.ts2 = self.font.render(self.text2, True, Color.WHITE)

    def process_get_score(self, value):
        self.score += value

    def get_score(self):
        return self.score

    def process_draw(self):
        self.game_object.screen.blit(self.ts, [500, 20])
        self.game_object.screen.blit(self.ts2, [510, 50])