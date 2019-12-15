import random

from src.entities.death_touch_entity import DeathTouchEntity
from src.entities.death_touch_entity import DeathTouchEntityInfo


class Flower(DeathTouchEntity):
    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy + 1, DeathTouchEntityInfo(True, True, True, True, False))
        self.startposy = posy
        self.vy = -1
        self.max_depth = random.randint(96, 160)

    def process_logic(self):
        if (self.rect.y == self.startposy) or (self.rect.y == self.startposy + self.max_depth):
            self.vy = -self.vy

    def drawing_priority(self):
        return -1

    def process_draw(self):
        if self.rect.y - self.startposy < 64:
            super().process_draw()