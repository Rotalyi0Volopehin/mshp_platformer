import pygame

from src.base_classes import DrawableObject
from src.constants import Color


class Score(DrawableObject):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.score = 0
        self.font = pygame.font.SysFont("Consolas", 45, True)
        self.text = 'Score'
        self.ts = self.font.render(self.text, True, Color.WHITE)
        self.refresh()

    def process_get_score(self, value):
        self.score += value

    def refresh(self):
        self.ts2 = self.font.render('{:0>4}'.format(self.score), False, Color.WHITE)

    def process_draw(self):
        if not self.game_object.gameplay_stage.pause:
            self.game_object.screen.blit(self.ts, [500, 22])
            self.game_object.screen.blit(self.ts2, [510, 50])