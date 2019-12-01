import pygame


class Camera:
    def __init__(self, game, width, height, speed=1):
        self.game = game
        self.width = width
        self.height = height
        self.speed = speed
        self.state = pygame.Rect(0, 0, self.width, self.height)
        self.bg_state = pygame.Rect(self.state)

    def apply(self, rect):
        return rect.move(self.state.topleft)

    def apply_bg(self, rect):
        return rect.move(self.bg_state.topleft)

    def update(self, target_rect):
        x = -target_rect.centerx + (self.game.width >> 1)
        y = -target_rect.centerx + (self.game.height >> 1)
        self.__move_camera(self.state, x, y)
        x = -target_rect.centerx * 0.9 + (self.game.width >> 1)
        y = -target_rect.centerx * 0.9 + (self.game.height >> 1)
        self.__move_camera(self.bg_state, x, y)

    def __move_camera(self, state, x, y):
        state.topleft += (pygame.Vector2(x, y) - pygame.Vector2(state.topleft)) * self.speed
        state.x = max(-(self.width - self.game.width), min(0, state.x))
        state.y = max(-(self.height - self.game.height), min(0, state.y))