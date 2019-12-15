import pygame

from src.base_classes import DrawableObject
from src.constants import Color


class TimeGame(DrawableObject):
    def __init__(self, game):
        super().__init__(game)
        self.start_time = 300
        self.game_object = game
        self.start_ticks = pygame.time.get_ticks()
        self.seconds = 0
        self.font = pygame.font.SysFont("Consolas", 45, True)
        self.caption = self.font.render('Time', True, Color.WHITE)
        self.refresh()
        self.data_rect = self.data.get_rect()
        self.data_rect.x = 650
        self.data_rect.y = 20
        self.caption_rect = self.caption.get_rect()
        self.caption_rect.x = 640
        self.data_rect.y = 50

    def process_draw(self):
        if not self.game_object.gameplay_stage.pause:
            self.game_object.screen.blit(self.data, self.data_rect)
            self.game_object.screen.blit(self.caption, self.caption_rect)

    def unpause(self):
        seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000
        delta = seconds - self.seconds
        self.start_ticks += delta * 1000

    def refresh(self):
        self.data = self.font.render(str(self.start_time - self.seconds), False, Color.WHITE)

    def process_logic(self):
        if self.game_object.gameplay_stage.pause:
            return
        seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000
        if self.seconds == seconds:
            return
        self.seconds = seconds
        if (seconds >= self.start_time):
            self.game_object.game_over = True
        self.refresh()