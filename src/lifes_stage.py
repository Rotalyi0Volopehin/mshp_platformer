import pygame

from src.constants import Color
from src.constants import get_retro_font


class LifesStage:
    @staticmethod
    def draw(game, lifes):
        #draw Mario
        level = game.gameplay_stage.current_level
        mario_image = level.images["PlayerGhost"]
        game.screen.fill((24, 12, 12))
        mario_rect = mario_image.get_rect()
        mario_rect.centerx = (game.width >> 1) - 48
        mario_rect.centery = game.height >> 1
        game.screen.blit(mario_image, mario_rect)
        #draw lifes count
        text = "X " + str(lifes)
        font = get_retro_font(32)
        render = font.render(text, True, Color.WHITE)
        render_rect = render.get_rect()
        render_rect.x = (game.width >> 1) + 8
        render_rect.centery = game.height >> 1
        game.screen.blit(render, render_rect)
        #draw level's name
        render = font.render(level.name, True, Color.WHITE)
        render_rect = render.get_rect()
        render_rect.centerx = game.width >> 1
        render_rect.centery = (game.height >> 1) - 64
        game.screen.blit(render, render_rect)