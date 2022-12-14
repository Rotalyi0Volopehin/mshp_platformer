import pygame

from src.entities.death_touch_entity import DeathTouchEntity
from src.entities.death_touch_entity import DeathTouchEntityInfo
from src.static_grid_cells.obstacle import Obstacle
from src.entities.shell import Shell
from src.entities.animation import Animation


# Это босс
class Turtle(DeathTouchEntity):
    range = 512
    speed = 1

    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy, DeathTouchEntityInfo(True, False, True, True, True))
        self.collision_left = self.collision_right = False
        self.dmg_cooldown = self.cooldown = 0
        self.hp = 3
        self.fake = True
        images = self.level.images
        self.hp_images_left = [images["Turtle-halfdead"], images["Turtle-injured"], images["Turtle"]]
        self.hp_images_right = []
        for img_left in self.hp_images_left:
            self.hp_images_right.append(pygame.transform.flip(img_left, True, False))
        self.image = images["Princess"]
        self.speedup = False
        self.__bgm_stoped = False

    def process_logic(self):
        level = self.level
        if not self.__bgm_stoped:
            level.stop_bgm()
            self.__bgm_stoped = True
        if self.fake:
            if (level.player != None) and (level.player.rect.x > self.rect.x - (Turtle.range >> 1)):
                self.fake = False
                self.vx = -Turtle.speed
                self.level.play_bgm()
            return
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
        self.direct()
        self.collision_left = self.collision_right = False

    def direct(self):
        player = self.level.player
        if player is None:
            return
        dist = abs(self.rect.x - player.rect.x)
        if (dist > 96):
            self.__try_direct_on_player()
        else:
            speedup_ = self.speedup
            self.speedup = dist < 64
            if not speedup_ and self.speedup:
                self.vx = Turtle.speed << 2
                self.__try_direct_on_player()
                self.vx = -self.vx
            elif speedup_ and not self.speedup:
                self.vx = Turtle.speed if self.vx > 0 else -Turtle.speed

    def __try_direct_on_player(self):
        player = self.level.player
        if (((self.rect.x < player.rect.x) and (self.vx < 0)) or ((self.rect.x > player.rect.x) and (self.vx > 0))):
            self.vx = -self.vx

    def process_draw(self):
        if not self.fake and (self.vx != 0):
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
            self.game_object.ui_panel.score.process_get_score(9)
            self.hp -= 1
            if self.hp == 0:
                self.level.add_new_entity(Animation(self.game_object, self.level.images["Turtle-death"], self.rect.x, self.rect.y, 120, 0, 4))
                self.disappear()
                self.level.stop_bgm()

    def __try_take_damage(self):
        if self.dmg_cooldown == 0:
            self.dmg_cooldown = 8
            return True
        return False

    def try_spawn_shells(self):
        if self.level.player.rect.x + Turtle.range >= self.rect.centerx >= self.level.player.rect.x - Turtle.range:
            self.cooldown = 42
            shell = Shell(self.game_object, self.level.images["Shell"], self.rect.x, self.rect.y - 64, 240, -5)
            shell.vy = -10
            self.level.add_new_entity(shell)
            shell = Shell(self.game_object, self.level.images["Shell"], self.rect.x, self.rect.y - 64, 240, 5)
            shell.vy = -10
            self.level.add_new_entity(shell)
