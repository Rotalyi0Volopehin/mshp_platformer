from src.entities.death_touch_entity import DeathTouchEntity
from src.entities.death_touch_entity import DeathTouchEntityInfo
from src.entity import Entity
from src.static_grid_cells.obstacle import Obstacle
from src.constants import Stats
from src.entities.player import Player

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

    def on_collide(self, collisions):
        for collision in collisions:
            # Коллизия с препятствием
            if isinstance(collision.opp_rb, Player):
                if self.level.boss.alive == False:
                    #TODO: ДОБАВЬТЕ ТУТ КОНЦОВКУ
                    pass

            if isinstance(collision.opp_rb, Obstacle):
                if collision.bottom:
                    self.on_ground = True
                    self.bottom_collision = True

    def process_logic(self):
        def sign(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0
        self.speed = 5*-sign(self.rect.centerx-self.level.player.rect.x)
        self.vx = self.speed
        self.steps += abs(self.speed)
