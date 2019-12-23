import pygame

from src.constants import Color
from src.constants import get_retro_font


class PauseStage:
    render = None
    render_rect = None

    @staticmethod
    def init():
        font = get_retro_font(46)
        PauseStage.render = pygame.Surface((600, 300))
        text = font.render("ПАУЗА", True, Color.WHITE)
        text_rect = text.get_rect()
        text_rect.centerx = 300
        text_rect.centery = 150
        PauseStage.render.blit(text, text_rect)
        PauseStage.render_rect = PauseStage.render.get_rect()
        PauseStage.render_rect.centerx = 512
        PauseStage.render_rect.centery = 320

    @staticmethod
    def draw(screen):
        screen.blit(PauseStage.render, PauseStage.render_rect)