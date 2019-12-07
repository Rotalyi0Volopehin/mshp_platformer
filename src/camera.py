import pygame


class Camera:
    def __init__(self, game, width, height, speed=0.1):
        self.game = game
        self.width = width
        self.height = height
        self.speed = speed
        self.state = pygame.Rect(0, 0, self.width, self.height)

    def apply(self, rect):
        return rect.move(self.state.topleft)

    def update(self, target_rect):
        x = -target_rect.centerx + (self.game.width >> 1)
        y = -target_rect.centerx + (self.game.height >> 1)
        self.__move_camera(self.state, x, y)

    def __move_camera(self, state, x, y):
        state.topleft += (pygame.Vector2(x, y) - pygame.Vector2(state.topleft)) * self.speed
        state.x = max(-(self.width - self.game.width), min(0, state.x))
        state.y = max(-(self.height - self.game.height), min(0, state.y))