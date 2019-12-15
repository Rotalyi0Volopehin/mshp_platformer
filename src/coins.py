import pygame

from src.base_classes import DrawableObject
from src.constants import Color
from src.arch.sfx_player import SFX_Player


class Coins(DrawableObject):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.coins_at_level_start = self.coins = 0
        self.text = 'Coins'
        self.text2 = '{:3}'.format(self.coins)
        self.font = pygame.font.SysFont("Consolas", 45, True, False)
        self.caption = self.font.render(self.text, True, Color.WHITE)
        self.refresh()
        self.data_rect = self.data.get_rect()
        self.data_rect.x = 350
        self.data_rect.y = 20
        self.caption_rect = self.caption.get_rect()
        self.caption_rect.x = 340
        self.data_rect.y = 50

    def next_level(self):
        self.coins_at_level_start = self.coins

    def restart_level(self):
        if self.coins != self.coins_at_level_start:
            self.coins = self.coins_at_level_start
            self.refresh()

    def process_draw(self):
        if not self.game_object.gameplay_stage.pause:
            self.game_object.screen.blit(self.caption, self.caption_rect)
            self.game_object.screen.blit(self.data, self.data_rect)

    def process_change_coins(self, value):
        self.coins += value
        SFX_Player.play_sound("Coin")
        self.refresh()

    def refresh(self):
        self.data = self.font.render('{:3}'.format(self.coins), False, Color.WHITE)