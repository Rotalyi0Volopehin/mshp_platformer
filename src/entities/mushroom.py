import os
import pygame

from src.constants import IMAGES_DIR
from src.entities.patrolling_npc import PatrollingNPC


class Mushroom(PatrollingNPC):

    # Скорость перемещения
    speed = 0.25
    # Дистанция патрулирования
    distance = 100

    def __init__(self, game, posx, posy):
        image = pygame.image.load(os.path.join(IMAGES_DIR, 'mushroom.png'))
        super().__init__(game, image, posx, posy, self.speed, self.distance)
