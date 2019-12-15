import pygame

from src.base_classes import DrawableObject
from src.constants import Color
from src.io_tools import IO_Tools


class Score(DrawableObject):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.score_at_level_start = self.score = 0
        self.font = pygame.font.SysFont("Consolas", 45, True)
        self.caption = self.font.render('Score', True, Color.WHITE)
        self.refresh()
        self.data_rect = self.data.get_rect()
        self.data_rect.x = 510
        self.data_rect.y = 20
        self.caption_rect = self.caption.get_rect()
        self.caption_rect.x = 500
        self.data_rect.y = 50

    def next_level(self):
        self.score_at_level_start = self.score

    def restart_level(self):
        if self.score != self.score_at_level_start:
            self.score = self.score_at_level_start
            self.refresh()

    def process_get_score(self, value):
        self.score += value
        self.refresh()

    def refresh(self):
        self.data = self.font.render('{:0>4}'.format(self.score), False, Color.WHITE)

    def process_draw(self):
        if not self.game_object.gameplay_stage.pause:
            self.game_object.screen.blit(self.caption, self.caption_rect)
            self.game_object.screen.blit(self.data, self.data_rect)