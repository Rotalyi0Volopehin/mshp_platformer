from src.entities.death_touch_entity import DeathTouchEntity
from src.entities.death_touch_entity import DeathTouchEntityInfo
from src.static_grid_cells.obstacle import Obstacle
from src.entities.animationTurtle import Animation
from src.entities.Shell import Shell
import pygame
# Черепаха, двигающаяся вправо-влево, пока не встретит препятствие или край уровня; убивает игрока всеми сторонами, кроме верхней
class Turtle(DeathTouchEntity):
    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy, DeathTouchEntityInfo(True, False, True, True, True))
        self.vx = 0.75 #Начальная скорость по X
        self.collision_left = self.collision_right = False
        self.u = 0 # TIME shooting
        self.life = 3
        self.alive = True

    def drawing_priority(self):
        return -2

    def process_logic(self):
        self.u += 1
        self.spawn_bllet()
        print('PHNPHPHP',self.rect.centerx, self.rect.centery)
        if (self.vx > 0) and ((self.rect.right >= self.level.width - 1) or self.collision_right):
            self.vx = -abs(self.vx) #Отражение налево (препятствие справа)
        elif (self.vx < 0) and ((self.rect.x <= 0) or self.collision_left):
            self.vx = abs(self.vx) #Отражение направо (препятствие слева)
        self.collision_left = self.collision_right = False

    def on_collide(self, collisions):
        for collision in collisions:
            if isinstance(collision.opp_rb, Obstacle): #Столкновение с препятствием
                if collision.left:
                    self.collision_left = True
                if collision.right:
                    self.collision_right = True
                    #level = self.game_object.current_level()
                    #level.delete_entity(self)
                    #level.delete_static_grid_cell(collision.opp_rb.locx, collision.opp_rb.locy)
                if self.collision_left and self.collision_right:
                    return

    def on_collide_with_player(self, collision):
        if collision.top:
            self.life -= 1
            if self.life == 2:
                self.image = pygame.image.load("levels\level_3\sprites\TurtleBroke.png")
            elif self.life == 1:
                self.image = pygame.image.load("levels\level_3\sprites\TurtleBroke2.png")
            elif self.life <= 0:
                self.level.add_new_entity(Animation(self.game_object, pygame.image.load("levels\level_3\sprites\Turtle-death.png"), self.rect.x, self.rect.y, 60, 0, -1))
                self.disappear()
                self.alive = False

    def spawn_bllet(self):
        if self.level.player.rect.x+500>=self.rect.centerx>=self.level.player.rect.x-500 and self.u>=40:
            self.u = 0
            self.level.add_new_entity(Shell(self.game_object, self.level.images["Shell"], self.rect.centerx, self.rect.centery-33))


