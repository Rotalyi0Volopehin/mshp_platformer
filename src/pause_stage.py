import pygame

from src.io_tools import IO_Tools
from src.constants import Color


class PauseStage:
    render = None
    render_rect = None

    @staticmethod
    def init():
        font = pygame.font.Font("..{0}fonts{0}RetroGaming.ttf".format(IO_Tools.sep_slash()), 46)
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