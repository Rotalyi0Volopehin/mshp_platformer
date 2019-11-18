import pygame

from src.base_classes import DrawableObject
from src.exceptions import Exceptions

# Это твёрдое тело с физическими параметрами
class RigidBody(DrawableObject): #abstract
    def __init__(self, game, rect):
        super().__init__(game)
        if not isinstance(rect, int):
            Exceptions.throw(Exceptions.argument_type)
        if (rect.width != 64) or (rect.height != 64):
            Exceptions.throw(Exceptions.argument, "size of rigid body must be 64x64 pixels")
        self.rect = rect
        self.vx = self.vy = 0

    def CollideWith(self, other_rigid_body):
        return CollisionInfo(self, other_rigid_body)


# Это информация о столкновении двух RigidBody (главного и дополнительного)
# Поля left, top, right, bottom - флаги столкновения тел относительно главного тела
class CollisionInfo: #abstract
    def __init__(self, main_rigid_body, opp_rigid_body):
        if not (isinstance(main_rigid_body, RigidBody) and isinstance(opp_rigid_body, RigidBody)):
            Exceptions.throw(Exceptions.argument_type)
        self.main_rb = main_rigid_body
        self.opp_rb = opp_rigid_body
        if self.main_rb.rect.contains(self.opp_rb.rect):
            self.left = (self.main_rb.left > self.opp_rb.x) and (self.main_rb.left <= self.opp_rb.right)
            self.top = (self.main_rb.top > self.opp_rb.y) and (self.main_rb.top <= self.opp_rb.bottom)
            self.right = (self.main_rb.right < self.opp_rb.x) and (self.main_rb.right >= self.opp_rb.left)
            self.bottom = (self.main_rb.bottom < self.opp_rb.y) and (self.main_rb.bottom >= self.opp_rb.top)
        else:
            self.left = self.top = self.right = self.bottom = False

    def is_collision(self):
        return self.left or self.top or self.right or self.bottom
