import pygame

from src.entity import Entity
from src.static_grid_cells.obstacle import Obstacle


class Player(Entity):
    speed = 1
    jump_force = 10

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
            self.move_left = False
            self.vx = self.jump_force
        self.move_left = self.move_top = self.move_right = self.move_bottom = False
        self.left_collision = self.top_collision = self.right_collision = self.bottom_collision = False
        if not self.bottom_collision:
            self.apply_gravity_force(1)

    def on_collide(self, collisions):
        for collision in collisions:
            if isinstance(collision, Obstacle):
                if collision.left and (self.vx < 0):
                    self.vx = 0
                    self.left_collision = True
                if collision.right and (self.vx > 0):
                    self.vx = 0
                    self.right_collision = True
                if collision.top and (self.vy < 0):
                    self.vy = 0
                    self.top_collision = True
                if collision.bottom and (self.vy > 0):
                    self.vy = 0
                    self.bottom_collision = True

    def process_event(self, event):
        keydown = event.type == pygame.KEYDOWN
        if event.key == pygame.K_a:
            self.move_left = keydown
        elif event.key == pygame.K_d:
            self.move_right = keydown
        elif event.key == pygame.K_w:
            self.move_top = keydown
        elif event.key == pygame.K_s:
            self.move_bottom = keydown


class Player(DrawableObject):

    def __init__(self, game_object, x=0, y=0):
        super().__init__(game_object)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((Stats.WIDTH, Stats.HEIGHT))
        self.image = image.load("%s/raccoon_64.png" % IMAGES_DIR)
        self.rect = Rect(x, y, Stats.WIDTH, Stats.HEIGHT) # прямоугольный объект
        self.left = self.right = False
        self.up = False
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?

    def process_logic(self):

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
        self.collide_with_platforms(0, self.yvel, PLT.S)
        self.rect.x += self.xvel
        self.collide_with_platforms(self.xvel, 0, PLT.S)

    def process_draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))



    def collide_with_platforms(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

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
