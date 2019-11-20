import pygame

from src.rigid_body import RigidBody
from src.exceptions import Exceptions

# Это сущность - игровой объект, обладающий позицией, скоростью и спрайтом
class Entity(RigidBody): #abstract
    def __init__(self, game, image, posx, posy):
        if not (isinstance(image, pygame.Surface) and isinstance(posx, int) and isinstance(posy, int)):
            Exceptions.throw(Exceptions.argument_type)
        rect = image.get_rect()
        rect.x = posx
        rect.y = posy
        super().__init__(game, rect)
        self.image = image
        self.vx = self.vy = 0

    def process_draw(self):
        self.game_object.screen.blit(self.image, self.rect)

    def apply_gravity_force(self, value):
        self.vy += value
