import pygame
from src.base_classes import DrawableObject


class Coins(DrawableObject):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.coin_amount = 0
        self.text = 'Coins'
        self.text2 = '{:3}'.format(self.coin_amount)
        self.font = pygame.font.SysFont('Comic Sans Ms', 45, True, False)
        self.coin_output = self.font.render(self.text, True, [255, 255, 255])
        self.coin_output2 = self.font.render(self.text2, True, [255, 255, 255])

    def process_draw(self):
        self.game_object.screen.blit(self.coin_output, [350, 20])
        self.game_object.screen.blit(self.coin_output2, [350, 50])

    def process_change_coins(self, value):

        self.coin_amount += value
        self.coin_output2 = self.font.render('{:3}'.format(self.coin_amount), True, [255, 255, 255])
