from src.entity import Entity


# Это анимация, которая может показаться на lifetime итераций, двигаться с указанной скоростью и исчезать
class Animation(Entity):
    def __init__(self, game, image, posx, posy, lifetime, vx, vy):
        super().__init__(game, image, posx, posy)
        self.lifetime = lifetime
        self.vx = vx
        self.vy = vy

    def process_logic(self):
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.disappear()