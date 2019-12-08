from src.entities.death_touch_entity import DeathTouchEntity
from src.entities.death_touch_entity import DeathTouchEntityInfo
from src.entity import Entity
from src.static_grid_cells.obstacle import Obstacle
from src.constants import Stats


class Princess(Entity):
    # Скорость перемещения
    speed = 1
    # Дистанция патрулирования
    distance = 1000

    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy)
        self.steps = 0
        self.on_ground = False
        self.bottom_collision = False

    def change_direction(self):
        if self.steps < 10:
            return
        self.speed = -self.speed
        self.steps = 0

    def on_collide(self, collisions):
        for collision in collisions:
            # Коллизия с препятствием
            if isinstance(collision.opp_rb, Obstacle):
                if collision.bottom:
                    self.on_ground = True
                    self.bottom_collision = True
                if collision.left or collision.right:
                    self.change_direction()

    def on_collide_with_player(self, collision):
        if collision.left or collision.right:
            self.change_direction()


    def process_logic(self):

        self.vx = self.speed
        self.steps += abs(self.speed)
        if self.steps >= self.distance:
            self.change_direction()