import pygame

from src.entity import Entity
from src.static_grid_cells.obstacle import Obstacle


class Player(Entity):
    speed = 1
    jump_force = -10

    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy)
        self.move_left = self.move_top = self.move_right = self.move_bottom = False
        self.left_collision = self.top_collision = self.right_collision = self.bottom_collision = False

    def process_logic(self):
        if self.move_left and not self.left_collision:
            self.vx = -self.speed
        if self.move_right and not self.right_collision:
            self.vx = self.speed
        if self.move_top and not self.top_collision:
            self.vy = self.speed
        if self.move_left and not self.left_collision:
            self.vx = self.jump_force
        if not self.bottom_collision and (self.vy < 5):
            self.apply_gravity_force(1)
        else:
            self.rect.y -= 1
        #self.move_left = self.move_top = self.move_right = self.move_bottom = False
        self.left_collision = self.top_collision = self.right_collision = self.bottom_collision = False

    def on_collide(self, collisions):
        for collision in collisions:
            if isinstance(collision.opp_rb, Obstacle):
                if collision.left and (self.vx <= 0):
                    self.vx = 0
                    self.left_collision = True
                if collision.right and (self.vx >= 0):
                    self.vx = 0
                    self.right_collision = True
                if collision.top and (self.vy <= 0):
                    self.vy = 0
                    self.top_collision = True
                if collision.bottom and (self.vy >= 0):
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
                self.move_top = keydown
            elif event.key == pygame.K_s:
                self.move_bottom = keydown