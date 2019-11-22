import os
import pygame

from src.constants import IMAGES_DIR
from src.entity import Entity
from src.entities.temp_entities_for_mushroom import *


class Mushroom(Entity):

    _image_name = 'mushroom.png'
    _speed = 1
    _distance = 100

    _temp_gravity = 2

    def __init__(self, game, posx, posy):
        self.game = game
        image = pygame.image.load(os.path.join(IMAGES_DIR, self._image_name))
        super().__init__(game, image, posx, posy)
        self.current_speed = self._speed
        self.current_distance = 0
        self.on_ground = False
        self.alive = True

    def process_logic(self):
        # Проверка коллизии со всеми объектами
        for entity in self.game.levels[0].entity_set.entities:
            # Если есть коллизия с платформой
            if isinstance(entity, Platform):
                collision_info = self.CollideWith(entity)
                if collision_info.is_collision():
                    if collision_info.bottom:
                        self.on_ground = True
            # Если есть коллизия с игроком
            elif isinstance(entity, Player):
                collision_info = self.CollideWith(entity)
                if collision_info.is_collision():
                    if collision_info.top:
                        self.die()
            else:
                self.on_ground = False

        # Установка гравитации
        if self.on_ground:
            self.vy = 0
            self.vx = self.current_speed
        else:
            self.vy = self._temp_gravity
            self.vx = 0

        self.apply_velocity()
        self.current_distance += abs(self.current_speed)
        if self.current_distance >= self._distance:
            self.current_speed *= -1
            self.current_distance = 0

    def die(self):
        self.alive = False
