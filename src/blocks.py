#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import os
from pygame import *
from src.constants import *
from src.base_classes import DrawableObject

 
class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM.WIDTH, PLATFORM.HEIGHT))
        self.image.fill(Colors.PLATFORM_COLOR)
        self.image = image.load("%s/block_32.png" % IMAGES_DIR)
        # если 32x32 - platform.png
        self.rect = Rect(x, y, PLATFORM.WIDTH, PLATFORM.HEIGHT)

    def process_draw(self, screen):
        x = y = 0  # координаты
        for row in Level.test_level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    # создаем блок, заливаем его цветом и рисеум его
                    self.game_object.screen.blit(self.image, self.rect)
                x += self.width  # блоки платформы ставятся на ширине блоков
            y += self.height  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

