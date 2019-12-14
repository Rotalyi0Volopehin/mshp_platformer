import pygame

from src.constants import Color


class LifesStage:
    @staticmethod
    def draw(game, lifes):
        mario_image = game.gameplay_stage.current_level.images["Player"]
        game.screen.fill(Color.BLACK)
        mario_rect = mario_image.get_rect()
        mario_rect.centerx = (game.width >> 1) - 64
        mario_rect.centery = game.height >> 1
        game.screen.blit(mario_image, mario_rect)
        text = "X " + str(lifes)
        font = pygame.font.SysFont("Consolas", 32, True, False)
        render = font.render(text, True, Color.WHITE)
        render_rect = render.get_rect()
        render_rect.x = game.width >> 1
        render_rect.centery = game.height >> 1
        game.screen.blit(render, render_rect)