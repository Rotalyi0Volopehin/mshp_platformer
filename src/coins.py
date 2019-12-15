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
        self.caption = self.font.render(self.text, True, Color.WHITE)
        self.refresh()
        self.data_rect = self.data.get_rect()
        self.data_rect.x = 350
        self.data_rect.y = 20
        self.caption_rect = self.caption.get_rect()
        self.caption_rect.x = 340
        self.data_rect.y = 50

    def process_draw(self):
        if not self.game_object.gameplay_stage.pause:
            self.game_object.screen.blit(self.caption, self.caption_rect)
            self.game_object.screen.blit(self.data, self.data_rect)

    def process_change_coins(self, value):
        self.coin_amount += value
        self.refresh()

    def refresh(self):
        self.data = self.font.render('{:3}'.format(self.coin_amount), False, Color.WHITE)