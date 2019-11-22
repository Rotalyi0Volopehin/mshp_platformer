from src.entity import Entity
from src.static_grid_cell import StaticGridCell


class FakeCloud(Entity):
    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy)
        self.vx = 0.125
        self.collision_left = self.collision_right = False

    def process_logic(self):
        if (self.vx > 0) and ((self.rect.right >= self.game_object.current_level().width() - 1) or self.collision_right):
            self.vx = -abs(self.vx)
        elif (self.vx < 0) and ((self.rect.x <= 0) or self.collision_left):
            self.vx = abs(self.vx)
        self.collision_left = self.collision_right = False

    def on_collide(self, collisions):
        for collision in collisions:
            if isinstance(collision.opp_rb, StaticGridCell):
                if collision.left:
                    self.collision_left = True
                if collision.right:
                    self.collision_right = True
                if self.collision_left and self.collision_right:
                    return