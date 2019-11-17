import pygame
from src.base_classes import DrawableObject


class Coins(DrawableObject):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.coin_amount = 0
        self.text = 'COINS: {:5}'.format(self.coin_amount)
        self.font = pygame.font.SysFont('Comic Sans Ms', 30, True, False)
        self.coin_output = self.font.render(self.text, True, [255, 255, 255])

    def process_draw(self):
        self.game_object.screen.blit(self.coin_output, [300, 10])

    def process_change_coins(self, num):
        self.coin_amount += num