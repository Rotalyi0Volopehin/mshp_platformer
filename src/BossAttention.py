import os
import pygame
from src.base_classes import DrawableObject


class Label(DrawableObject):

    def __init__(self, game_object):
        super().__init__(game_object)
        self.font = pygame.font.SysFont('Comic Sans Ms', 45, True)
        self.text = 'Defeat the boss!'
        self.ts = self.font.render(self.text, True, [220, 20, 60])



    def process_draw(self):
        self.level = self.game_object.gameplay_stage.current_level
        if self.level.boss == 2:
            self.game_object.screen.blit(self.ts, [350, 120])