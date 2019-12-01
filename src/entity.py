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
        self.posx_carry = self.posy_carry = 0

    def apply_gravity_force(self, value):
        self.vy += value

    def apply_velocity(self):
        self.rect.x += int(self.vx)
        self.posx_carry += self.__calc_carry(self.vx)
        if self.posx_carry >= 1:
            self.posx_carry -= 1
            self.rect.x += 1
        elif self.posx_carry <= -1:
            self.posx_carry += 1
            self.rect.x -= 1
        self.rect.y += int(self.vy)
        self.posy_carry += self.__calc_carry(self.vy)
        if self.posy_carry >= 1:
            self.posy_carry -= 1
            self.rect.y += 1
        elif self.posy_carry <= -1:
            self.posy_carry += 1
            self.rect.y -= 1

    def __calc_carry(self, value):
        sign = (value > 0) - (value < 0)
        return abs(value) % 1 * sign

    def pull_out(self, pulling_dir):
        if pulling_dir == '<':
            self.rect.x &= 0xFFC0
        elif pulling_dir == '^':
            self.rect.y &= 0xFFC0
        elif pulling_dir == '>':
            self.rect.x = (self.rect.x & 0xFFC0) + 64
        elif pulling_dir == 'v':
            self.rect.y = (self.rect.y & 0xFFC0) + 64
        else:
            Exceptions.throw(Exceptions.argument, "directory must be represented by one of these values \"<^>v\"")