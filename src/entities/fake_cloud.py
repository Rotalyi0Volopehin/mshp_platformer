from src.entity import Entity


class FakeCloud(Entity):
    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy)
        self.origin_x = posx
        self.dir = 1
        self.count = 0

    def process_logic(self):
        if self.origin_x + self.rect.x * self.dir > 16:
            self.dir = -self.dir
            self.vx = 0
        overflow = self.count == 8
        self.vx = self.dir if overflow else 0
        self.count = 0 if overflow else self.count + 1