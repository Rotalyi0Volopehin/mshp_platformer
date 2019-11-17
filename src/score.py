import os
import pygame

from src.base_classes import DrawableObject


class Score(DrawableObject):

    def __init__(self, game_object):
        super().__init__(game_object)
        self.score = 0
        self.font = pygame.font.SysFont('Comic Sans Ms', 30, True, False)
        self.text = 'score: {:0>6}'.format(self.score)
        self.ts = font.render(text, True, [255,255,255])
    def process_get_score(self,b):
        self.score += b

    def process_draw(self):
        self.game_object.screen.blit(ts,[10,10])