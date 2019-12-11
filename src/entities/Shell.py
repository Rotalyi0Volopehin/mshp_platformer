from src.entities.death_touch_entity import DeathTouchEntity
from src.entities.death_touch_entity import DeathTouchEntityInfo
from src.static_grid_cells.obstacle import Obstacle
from src.entities.death_touch_entity import DeathTouchEntity
from src.entities.death_touch_entity import DeathTouchEntityInfo
from src.static_grid_cells.obstacle import Obstacle
from src.constants import Stats


class Shell(DeathTouchEntity):
    # Скорость перемещения
    speed = 1
    # Дистанция патрулирования
    distance = 20000

    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy, DeathTouchEntityInfo(True, False, True, True, True))
        self.steps = 0
        self.on_ground = False
        self.bottom_collision = False
        self.i = 0 #time life

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
        if collision.top:
            self.game_object.gameplay_stage.current_level.delete_entity(self)

    def process_logic(self):
        self.i +=1
        if self.i >= 250:
            self.disappear()
        if (self.vx > 0) and (self.rect.right >= self.game_object.gameplay_stage.current_level.width - 1):
            self.change_direction()
        elif (self.vx < 0) and (self.rect.x <= 0):
            self.change_direction()
        if self.on_ground:
            if self.bottom_collision:
                self.vy = -self.speed
                self.bottom_collision = False
            else:
                self.vy = 0
            self.vx = self.speed
        else:
            self.vy = Stats.GRAVITY
            self.vx = 0
        def sign(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0
        self.speed = 5 * -sign(self.rect.centerx - self.level.player.rect.x)
        self.steps += abs(self.speed)
        if self.steps >= self.distance:
            self.change_direction()