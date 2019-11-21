from src.entity import Entity


class FakeCloud(Entity):
    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy)
        self.origin_x = posx
        self.vx = 0.125

    def process_logic(self):
        delta = self.rect.x - self.origin_x
        if delta > 16:
            self.vx = -abs(self.vx)
        elif delta < -16:
            self.vx = abs(self.vx)