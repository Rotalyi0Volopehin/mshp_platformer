import pygame

from src.entity import Entity
from src.static_grid_cells.obstacle import Obstacle


class Player(Entity):
    speed = 0.8
    jump_force = -1.8
    resistance = 0.7
    resistance_in_air = 0.95
    max_jump_duration = 22
    fravity_force = 1
    falling_speed_limit = 10
    ignoring_jump_duration = 5

    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy)
        self.move_left = self.do_jump = self.move_right = self.move_down = False
        self.left_collision = self.top_collision = self.right_collision = self.bottom_collision = False
        self.jumped = False
        self.jump_duration = self.max_jump_duration
        self.prev_rect = pygame.Rect(0, 0, 64, 64)
        self.__renew_prev_rect()

    def process_logic(self):
        self.__renew_prev_rect()
        if self.rect.y > self.game_object.current_level().height():
            self.die()
        if self.move_left and not self.left_collision:
            self.vx -= self.speed
        if self.move_right and not self.right_collision:
            self.vx += self.speed
        if self.do_jump:
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
            self.apply_gravity_force(self.fravity_force)
        if abs(self.vx) < 0.2:
            self.vx = 0
        else:
            res = self.resistance if self.bottom_collision else self.resistance_in_air
            self.vx *= res
        #self.move_left = self.move_top = self.move_right = self.move_bottom = False
        self.left_collision = self.top_collision = self.right_collision = self.bottom_collision = False

    def __speedup_up(self):
        if self.jump_duration > self.ignoring_jump_duration:
            self.vy += self.jump_force
        self.jump_duration -= 1

    def die(self):
        self.game_object.game_over = True
        self.game_object.current_level().delete_entity(self)

    def __renew_prev_rect(self):
        if self.prev_rect != self.rect:
            self.prev_rect.x = self.rect.x
            self.prev_rect.y = self.rect.y

    def __restore_rect_from_prev(self):
        self.rect.x = self.prev_rect.x
        self.rect.y = self.prev_rect.y

    def __pull_out(self, pulling_dir):
        if pulling_dir == '<':
            self.rect.x &= 192
        elif pulling_dir == '^':
            self.rect.y &= 192
        elif pulling_dir == '>':
            self.rect.x = (self.rect.x & 192) + 64
        elif pulling_dir == 'v':
            self.rect.y = (self.rect.y & 192) + 64
        else:
            raise TypeError("<^>v")

    def on_collide(self, collisions):
        for collision in collisions:
            if isinstance(collision.opp_rb, Obstacle):
                if collision.top and (self.vy <= 0) and not self.top_collision:
                    self.vy = 0
                    if (self.rect.y & 63) < 58: #hard
                        self.__restore_rect_from_prev()
                        return
                    self.__pull_out('v')
                    self.top_collision = True
                if collision.bottom and (self.vy >= 0) and not self.bottom_collision:
                    self.__pull_out('^')
                    self.vy = 0
                    self.bottom_collision = True
                if (collision.opp_rb.rect.y - self.rect.y) < 60: #if player is not too deep in floor
                    if collision.left and (self.vx <= 0) and not self.left_collision:
                        self.__pull_out('>')
                        self.vx = 0
                        self.left_collision = True
                    if collision.right and (self.vx >= 0) and not self.right_collision:
                        self.__pull_out('<')
                        self.vx = 0
                        self.right_collision = True

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
                self.game_object.loop_delay = 75
            elif event.key == pygame.K_e:
                self.game_object.loop_delay = 10