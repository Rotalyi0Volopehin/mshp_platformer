import pygame

from src.base_classes import DrawableObject
from src.constants import Color


class Coins(DrawableObject):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.coin_amount = 0
        self.text = 'Coins'
        self.text2 = '{:3}'.format(self.coin_amount)
        self.font = pygame.font.SysFont("Consolas", 45, True, False)
        self.coin_output = self.font.render(self.text, True, Color.WHITE)
        self.refresh()

    def process_draw(self):
        if not self.game_object.gameplay_stage.pause:
            self.game_object.screen.blit(self.coin_output, (350, 22))
            self.game_object.screen.blit(self.coin_output2, (350, 50))

    def process_change_coins(self, value):
        self.coin_amount += value
        self.refresh()

    def refresh(self):
        self.coin_output2 = self.font.render('{:3}'.format(self.coin_amount), False, Color.WHITE)