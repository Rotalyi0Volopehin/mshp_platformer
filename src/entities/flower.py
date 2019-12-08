from src.entities.death_touch_entity import DeathTouchEntity
from src.entities.death_touch_entity import DeathTouchEntityInfo


class Flower(DeathTouchEntity):
    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy + 1, DeathTouchEntityInfo(True, True, True, True, False))
        self.startposy = posy
        self.vy = -1

    def process_logic(self):
        if (self.rect.y == self.startposy) or (self.rect.y == self.startposy + 128):
            self.vy = -self.vy

    def drawing_priority(self):
        return -1