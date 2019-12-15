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
        self.ts2 = self.font.render('Time', True, Color.WHITE)
        self.refresh()

    def process_draw(self):
        if not self.game_object.gameplay_stage.pause:
            self.game_object.screen.blit(self.ts, (650, 50))
            self.game_object.screen.blit(self.ts2, (640, 22))

    def refresh(self):
        self.ts = self.font.render(str(self.start_time - self.seconds), False, Color.WHITE)

    def process_logic(self):
        seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000
        if self.seconds == seconds:
            return
        self.seconds = seconds
        if (seconds >= self.start_time):
            self.game_object.game_over = True
        self.refresh()