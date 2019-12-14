'''
from src.entities.death_touch_entity import DeathTouchEntity
from src.entities.death_touch_entity import DeathTouchEntityInfo
from src.static_grid_cells.obstacle import Obstacle
from src.constants import Stats


class Shell(DeathTouchEntity):
    falling_speed_limit = 15

    def __init__(self, game, image, posx, posy, lifetime, speed):
        super().__init__(game, image, posx, posy, DeathTouchEntityInfo(True, False, True, True, False))
        self.vx = speed
        self.bottom_collision = False
        self.lifetime = lifetime

    def on_collide(self, collisions):
        for collision in collisions:
            if isinstance(collision.opp_rb, Obstacle):
                if collision.bottom:
                    self.bottom_collision = True
                if ((collision.left and (self.vx < 0)) or (collision.right and (self.vx > 0))) and (self.rect.y >= collision.opp_rb.rect.y):
                    self.vx = -self.vx

    def on_collide_with_player(self, collision):
        if collision.top:
            self.disappear()

    def process_logic(self):
        level = self.level
        if level.boss is None:
            self.disappear()
        self.lifetime -= 1
        if self.lifetime < 0:
            self.disappear()
            return
        if ((self.vx > 0) and (self.rect.right >= level.width - 1)) or ((self.vx < 0) and (self.rect.x <= 0)):
            self.vx = -self.vx
        if self.bottom_collision:
            self.bottom_collision = False
            self.pull_out('^')
            self.vy = 0
        elif self.vy < self.falling_speed_limit:
            self.apply_gravity_force(Stats.GRAVITY)

'''
from src.entities.death_touch_entity import DeathTouchEntity
from src.entities.death_touch_entity import DeathTouchEntityInfo
from src.static_grid_cells.obstacle import Obstacle
from src.constants import Stats


class Shell(DeathTouchEntity):
    falling_speed_limit = 15
    # Скорость перемещения
    speed = 1
    # Дистанция патрулирования
    distance = 20000

    def __init__(self, game, image, posx, posy, lifetime):
        super().__init__(game, image, posx, posy, DeathTouchEntityInfo(True, False, True, True, True))
        self.steps = 0
        self.on_ground = False
        self.bottom_collision = False
        self.lifetime = lifetime
        self.timer = 0

    def on_collide(self, collisions):
        for collision in collisions:
            if isinstance(collision.opp_rb, Obstacle):
                if collision.bottom:
                    self.bottom_collision = True
                if ((collision.left and (self.vx < 0)) or (collision.right and (self.vx > 0))) and (self.rect.y >= collision.opp_rb.rect.y):
                    self.vx = -self.vx
                    self.timer += 20

    def on_collide_with_player(self, collision):
        if collision.top:
            self.disappear()

    def process_logic(self):
        self.timer -= 1
        if self.timer <= 0:
            self.timer = 0
        def sign(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0
        level = self.level
        self.lifetime -= 1
        if self.lifetime < 0:
            self.disappear()
            return
        if ((self.vx > 0) and (self.rect.right >= level.width - 1)) or ((self.vx < 0) and (self.rect.x <= 0)):
            self.vx = -self.vx
            self.timer += 20
        elif self.timer <= 0:
            self.vx = 5 * -sign(self.rect.centerx - self.level.player.rect.x)
        if self.bottom_collision:
            self.bottom_collision = False
            self.pull_out('^')
            self.vy = 0
        elif self.vy < self.falling_speed_limit:
            self.apply_gravity_force(Stats.GRAVITY)



        self.steps = abs(self.speed)

