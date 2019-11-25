import pygame

from src.entity import Entity
from src.static_grid_cells.obstacle import Obstacle


class Player(Entity):
    speed = 1
    jump_force = -10
    resistance = 0.8

    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy)
        self.move_left = self.move_up = self.move_right = self.move_down = False
        self.left_collision = self.top_collision = self.right_collision = self.bottom_collision = False

    def process_logic(self):
        if self.rect.y > self.game_object.current_level().height():
            self.die()
        if self.move_left and not self.left_collision:
            self.vx -= self.speed
        if self.move_right and not self.right_collision:
            self.vx += self.speed
        if self.move_up and not self.top_collision and self.bottom_collision:
            self.vy += self.jump_force
        if self.move_down and not self.bottom_collision:
            pass
        if not self.bottom_collision and (self.vy < 5):
            self.apply_gravity_force(1)
        #self.move_left = self.move_top = self.move_right = self.move_bottom = False
        self.left_collision = self.top_collision = self.right_collision = self.bottom_collision = False

    def die(self):
        self.game_object.game_over = True
        self.game_object.current_level().delete_entity(self)

    def __pull_out(self, obstacle, pulling_dir):
        inside = True
        while inside:
            if pulling_dir == '<':
                self.rect.x -= 1
                inside = self.collide_with(obstacle).right
            elif pulling_dir == '^':
                self.rect.y -= 1
                inside = self.collide_with(obstacle).bottom
            elif pulling_dir == '>':
                self.rect.x += 1
                inside = self.collide_with(obstacle).left
            elif pulling_dir == 'v':
                self.rect.x -= 1
                inside = self.collide_with(obstacle).top
            else:
                raise TypeError("<^>v")

    def on_collide(self, collisions):
        for collision in collisions:
            if isinstance(collision.opp_rb, Obstacle):
                if collision.left and (self.vx <= 0):
                    self.__pull_out(collision.opp_rb, '>')
                    self.vx = 0
                    self.left_collision = True
                if collision.right and (self.vx >= 0):
                    self.__pull_out(collision.opp_rb, '<')
                    self.vx = 0
                    self.right_collision = True
                if collision.top and (self.vy <= 0):
                    self.__pull_out(collision.opp_rb, 'v')
                    self.vy = 0
                    self.top_collision = True
                if collision.bottom and (self.vy >= 0):
                    self.__pull_out(collision.opp_rb, '^')
                    self.vy = 0
                    self.bottom_collision = True

    def process_event(self, event):
        keydown = event.type == pygame.KEYDOWN
        if keydown or (event.type == pygame.KEYUP):
            if event.key == pygame.K_a:
                self.move_left = keydown
            elif event.key == pygame.K_d:
                self.move_right = keydown
            elif event.key == pygame.K_w:
                self.move_up = keydown
            elif event.key == pygame.K_s:
                self.move_down = keydown