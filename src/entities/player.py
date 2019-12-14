import pygame

from src.entity import Entity
from src.static_grid_cells.obstacle import Obstacle
from src.static_grid_cells.brick_cell import BrickCell
from src.entities.animation import Animation
from src.constants import Stats
from src.entities.turtle import Turtle


class Player(Entity):
    speed = 1
    jump_force = -2
    resistance = 0.7
    resistance_in_air = 0.95
    max_jump_duration = 16
    falling_speed_limit = 15
    ignoring_jump_duration = 8

    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy)
        self.image_left = pygame.transform.flip(self.image, True, False)
        self.image_right = self.image
        self.move_left = self.do_jump = self.move_right = self.move_down = False
        self.left_collision = self.top_collision = self.right_collision = self.bottom_collision = False
        self.jumped = False
        self.jump_duration = self.max_jump_duration
        self.prev_rect = pygame.Rect(0, 0, 64, 64)
        self.__renew_prev_rect()
        self.__try_to_die = False
        self.__try_to_die_by = None
        self.dead = False
        self.death_animation = None

    def process_logic(self):
        if self.dead:
            if self.death_animation.lifetime == 0:
                self.disappear()
                self.game_object.game_over = True
            return
        if self.__try_to_die:
            self.__try_to_die = False
            self.__collide_with_dte(self.collide_with(self.__try_to_die_by))
            self.__try_to_die_by = None
        if self.dead:
            return
        self.__renew_prev_rect()
        if self.rect.y > self.level.height:
            self.die()
        if self.move_left and not self.left_collision:
            self.vx -= self.speed
        if self.move_right and not self.right_collision:
            self.vx += self.speed
        if self.do_jump or ((self.jump_duration >= self.ignoring_jump_duration) and (self.jump_duration < self.max_jump_duration)):
            if not self.top_collision and self.bottom_collision and not self.jumped:
                self.__speedup_up()
                self.jumped = True
            elif (self.jump_duration < self.max_jump_duration) and (self.jump_duration > 0) and not self.bottom_collision:
                self.__speedup_up()
        else:
            self.jumped = False
            self.jump_duration = self.max_jump_duration
        if self.move_down and not self.bottom_collision:
            pass
        if not self.bottom_collision and (self.vy < self.falling_speed_limit):
            self.apply_gravity_force(Stats.GRAVITY)
        if abs(self.vx) < 0.2:
            self.vx = 0
        else:
            res = self.resistance if self.bottom_collision else self.resistance_in_air
            self.vx *= res
        #self.move_left = self.move_top = self.move_right = self.move_bottom = False
        self.left_collision = self.top_collision = self.right_collision = self.bottom_collision = False

    def __speedup_up(self):
        self.vy += self.jump_force
        self.jump_duration -= 1

    def die(self):
        #self.game_object.game_over = True
        self.death_animation = Animation(self.game_object, self.level.images["Player-death"], self.rect.x, self.rect.y, 60, 0, -1)
        self.level.add_new_entity(self.death_animation)
        self.dead = True
        self.vx = self.vy = 0

    def process_draw(self):
        if not self.dead:
            if self.vx != 0:
                self.image = self.image_left if self.vx < 0 else self.image_right
            super().process_draw()

    def __renew_prev_rect(self):
        if self.prev_rect != self.rect:
            self.prev_rect.x = self.rect.x
            self.prev_rect.y = self.rect.y

    def __restore_rect_from_prev(self):
        self.rect.x = self.prev_rect.x
        self.rect.y = self.prev_rect.y

    def on_collide(self, collisions):
        if self.dead:
            return
        for collision in collisions:
            if isinstance(collision.opp_rb, Obstacle):
                if collision.top and (self.vy <= 0) and not self.top_collision:
                    self.vy = 0
                    if (self.rect.y & 63) < 58: #hard
                        self.__restore_rect_from_prev()
                        return
                    self.pull_out('v')
                    self.top_collision = True
                if collision.bottom and (self.vy >= 0) and not self.bottom_collision and ((collision.opp_rb.rect.y - self.rect.bottom) < 4):
                    if self.__no_stick_check(collision.opp_rb) and self.__no_stand_on_air_check():
                        self.pull_out('^')
                        self.vy = 0
                        self.bottom_collision = True
                if (collision.opp_rb.rect.y - self.rect.y) < 60: #if player is not too deep in floor
                    if collision.left and (self.vx < 0) and not self.left_collision:
                        self.pull_out('>')
                        self.vx = 0
                        self.left_collision = True
                    if collision.right and (self.vx > 0) and not self.right_collision:
                        self.pull_out('<')
                        self.vx = 0
                        self.right_collision = True

    def __no_stick_check(self, obstacle):
        if (obstacle.locy == 0) or (obstacle.locy > len(self.level.grid.cells)):
            return True
        return not isinstance(self.level.grid.cells[obstacle.locy - 1][obstacle.locx], Obstacle)

    def __no_stand_on_air_check(self):
        modx = self.rect.centerx & 63
        if (modx < 28) or (modx > 36):
            return True
        locx = self.rect.centerx // 64
        locy = self.rect.centery // 64
        level = self.level
        if (locx < 0) or (locy < 0) or (locx >= level.grid.width) or (locy >= level.grid.height - 1):
            return True
        return level.grid.cells[locy + 1][locx] != None

    def process_event(self, event):
        keydown = event.type == pygame.KEYDOWN
        if keydown or (event.type == pygame.KEYUP):
            if event.key == pygame.K_a:
                self.move_left = keydown
            elif event.key == pygame.K_d:
                self.move_right = keydown
            elif event.key == pygame.K_w:
                self.do_jump = keydown
            elif event.key == pygame.K_s:
                self.move_down = keydown
            elif event.key == pygame.K_q:
                self.game_object.loop_delay = 100
            elif event.key == pygame.K_e:
                self.game_object.loop_delay = 25
            elif (event.key == pygame.K_SPACE) and not keydown:
                self.level.add_new_static_grid_cell(BrickCell(self.game_object, self.level.images["BrickCell"], self.rect.centerx // 64, self.rect.centery // 64))
            elif (event.key == pygame.K_HOME) and not keydown:
                self.game_object.gameplay_stage.next_level()
            elif (event.key == pygame.K_END) and not keydown:
                self.level.restart()

    def __collide_with_dte(self, collision):
        dte = collision.opp_rb
        info = dte.dt_info
        if (collision.right and info.dt_left) or (collision.bottom and info.dt_top) or (collision.left and info.dt_right) or (collision.top and info.dt_bottom):
            if not (self.level.will_rigid_body_be_deleted(dte) or (isinstance(dte, Turtle) and (dte.dmg_cooldown > 0))):
                self.die()
        if collision.bottom and info.trampoline and (self.vy > Stats.GRAVITY):
            self.vy = self.jump_force * (self.max_jump_duration - self.ignoring_jump_duration)

    def on_collide_with_dte(self, reverse_collision):
        if self.dead:
            return
        self.__try_to_die = True
        self.__try_to_die_by = reverse_collision.main_rb

    def drawing_priority(self):
        return 12