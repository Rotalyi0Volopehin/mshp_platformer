import pygame
from src.base_classes import DrawableObject
from src.constants import *
from pygame import *

from src.entities.Flower import *
from src.rigid_body import *



class Player(DrawableObject):
    def __init__(self, game, x = 0 , y = 0):
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((Stats.WIDTH, Stats.HEIGHT))
        self.image = image.load("%s\Player.png" % IMAGES_DIR)
        self.rect = Rect(x, y, Stats.WIDTH, Stats.HEIGHT)  # прямоугольный объект
        self.left = self.right = False
        self.up = False
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.alive = True  # смэрт?

    def process_logic(self):
            if self.alive:
                if self.up:
                    if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                        self.yvel = -Stats.JUMP_POWER

                if self.left:
                    self.xvel = -Stats.MOVE_SPEED  # Лево = x- n

                if self.right:
                    self.xvel = Stats.MOVE_SPEED  # Право = x + n

                if not (self.left or self.right):  # стоим, когда нет указаний идти
                    self.xvel = 0

            if not self.onGround:
                self.yvel += Stats.GRAVITY

            self.onGround = False  # Мы не знаем, когда мы на земле((

            # Передвижение
            self.rect.y += self.yvel
            if self.alive:
                self.collide_with_platforms(0, self.yvel, PLT.S)
                self.rect.x += self.xvel
                self.collide_with_platforms(self.xvel, 0, PLT.S)

            if not self.alive:
                self.rect.y = 0
                self.rect.x = 0
                self.alive = True

    def process_draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def process_event(self, event):

        if event.type == KEYDOWN and event.key == K_a:
            self.left = True
        if event.type == KEYUP and event.key == K_a:
            self.left = False

        if event.type == KEYDOWN and event.key == K_d:
            self.right = True
        if event.type == KEYUP and event.key == K_d:
            self.right = False

        if event.type == KEYDOWN and event.key == K_SPACE:
            self.up = True
        if event.type == KEYUP and event.key == K_SPACE:
            self.up = False

    def collide_with_platforms(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                print(p)
                if str(p).find('Flower', 0, len(str(p))) != -1:
                    self.alive = False
                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

    def collide_with_entity(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
            #lolol
                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает
