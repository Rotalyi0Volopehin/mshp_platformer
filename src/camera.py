import pygame


class Camera:
    def __init__(self, game, width, height):
        self.game = game
        self.width = width
        self.height = height
        self.state = pygame.Rect(0, 0, self.width, self.height)

    def apply(self, rect):
        return rect.move(self.state.topleft)

    def update(self, target_rect):
        x = -target_rect.center[0] + self.game.width / 2
        y = -target_rect.center[0] + self.game.height / 2
        self.state.topleft += (pygame.Vector2(x, y) - pygame.Vector2(self.state.topleft)) * 0.06
        self.state.x = max(-(self.width - self.game.width), min(0, self.state.x))
        self.state.y = max(-(self.height - self.game.height), min(0, self.state.y))