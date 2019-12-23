from src.base_classes import DrawableObject
from src.constants import Color
from src.arch.sfx_player import SFX_Player


class Coins(DrawableObject):
    def __init__(self, game_object, font, x_offset):
        super().__init__(game_object)
        self.coins_at_level_start = self.coins = 0
        self.text = 'Монеты'
        self.text2 = '{:3}'.format(self.coins)
        self.font = font
        self.caption = font.render(self.text, True, Color.WHITE)
        self.refresh()
        self.data_rect = self.data.get_rect()
        self.data_rect.x = x_offset + 270
        self.data_rect.y = 20
        self.caption_rect = self.caption.get_rect()
        self.caption_rect.x = x_offset + 230
        self.data_rect.y = 50

    def next_level(self):
        self.coins_at_level_start = self.coins

    def restart_level(self):
        if self.coins != self.coins_at_level_start:
            self.coins = self.coins_at_level_start
            self.refresh()

    def process_draw(self):
        self.game_object.screen.blit(self.caption, self.caption_rect)
        self.game_object.screen.blit(self.data, self.data_rect)

    def process_change_coins(self, value):
        self.coins += value
        SFX_Player.play_sound("Coin")
        self.refresh()
        self.game_object.ui_panel.score.process_get_score(value * 30)

    def refresh(self):
        self.data = self.font.render('{:3}'.format(self.coins), False, Color.WHITE)