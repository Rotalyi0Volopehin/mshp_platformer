from src.entities.death_touch_entity import DeathTouchEntity
from src.entities.death_touch_entity import DeathTouchEntityInfo
from src.static_grid_cells.coin import Coin
from src.static_grid_cells.obstacle import Obstacle
from src.entities.minishell import Shell
from src.entities.player import Player
from src.static_grid_cells.obstacle import Obstacle
from src.entities.animation import Animation
from src.static_grid_cells.brick_cell import BrickCell

import pygame


# Черепаха, двигающаяся вправо-влево, пока не встретит препятствие или край уровня; убивает игрока всеми сторонами, кроме верхней

class Miniboss(DeathTouchEntity):
    range = 512

    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy, DeathTouchEntityInfo(True, False, True, True, True))
        self.dead = False
        self.collision_left = self.collision_right = False
        self.dmg_cooldown = self.cooldown = 0
        self.hp = 3
        self.vx = -1
        self.level.boss = 2
        images = self.level.images
        self.hp_images_left = [images["Turtlebroke2"], images["Turtlebroke"], images["Miniboss"]]
        self.hp_images_right = []
        for img_left in self.hp_images_left:
            self.hp_images_right.append(pygame.transform.flip(img_left, True, False))
        self.image = images["Miniboss"]

    def process_logic(self):

        if not self.dead:
            self.level.boss = 2
        level = self.level
        if self.dmg_cooldown > 0:
            self.dmg_cooldown -= 1
        if self.cooldown > 0:
            self.cooldown -= 1
        else:
            self.try_spawn_shells()

        if (self.vx > 0) and ((self.rect.right >= level.width - 1) or self.collision_right):
            self.vx = -abs(self.vx)
        elif (self.vx < 0) and ((self.rect.x <= 0) or self.collision_left):
            self.vx = abs(self.vx)
        self.collision_left = self.collision_right = False

    def process_draw(self):
        self.image = (self.hp_images_left if self.vx < 0 else self.hp_images_right)[self.hp - 1]
        super().process_draw()

    def on_collide(self, collisions):
        for collision in collisions:
            if isinstance(collision.opp_rb, Obstacle):
                if collision.left:
                    self.collision_left = True
                if collision.right:
                    self.collision_right = True

    def on_collide_with_player(self, collision):
        if collision.top and self.__try_take_damage():
            self.hp -= 1
            if self.hp == 2:
                self.image = self.level.images["Turtlebroke"]
            elif self.hp == 1:
                self.image = self.level.images["Turtlebroke2"]
            else:
                self.level.add_new_entity(Animation(self.game_object, self.level.images["Coin"], self.rect.x, self.rect.y, 20, 0, -3))
                self.game_object.coins.process_change_coins(1)
                self.level.add_new_entity(
                    Animation(self.game_object, self.level.images["Coin"], self.rect.x, self.rect.y, 20, -2, -3))
                self.game_object.coins.process_change_coins(1)
                self.level.add_new_entity(
                    Animation(self.game_object, self.level.images["Coin"], self.rect.x, self.rect.y, 20, 2, -3))
                self.game_object.coins.process_change_coins(1)
                self.level.boss = None
                self.dead = True
                self.disappear()

    def __try_take_damage(self):
        if self.dmg_cooldown == 0:
            self.dmg_cooldown = 8
            return True
        return False

    def try_spawn_shells(self):
        if self.level.player.rect.x + Miniboss.range >= self.rect.centerx >= self.level.player.rect.x - Miniboss.range:

            self.cooldown = 42
            shell = Shell(self.game_object, self.level.images["Shell"], self.rect.x, self.rect.y - 32, 240)
            shell.vy = -1
            self.level.add_new_entity(shell)
            shell = Shell(self.game_object, self.level.images["Shell"], self.rect.x, self.rect.y - 32, 240)
            shell.vy = -1
            self.level.add_new_entity(shell)
