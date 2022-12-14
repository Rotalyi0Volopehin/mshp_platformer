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
        self.boss_summon = self.level.boss != None

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
        if self.boss_summon and (level.boss is None):
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