import pygame
from pygame import *


class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.state = Rect(0, 0, self.width, self.height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        x = -target.rect.center[0] + 800 / 2
        y = -target.rect.center[0] + 600 / 2
        self.state.topleft += (pygame.Vector2((x, y)) - pygame.Vector2(self.state.topleft)) * 0.06
        self.state.x = max(-(self.width - 800), min(0, self.state.x))
        self.state.y = max(-(self.height - 600), min(0, self.state.y))