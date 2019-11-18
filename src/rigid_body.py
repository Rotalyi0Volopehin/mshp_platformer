import pygame

from src.base_classes import DrawableObject
from src.exceptions import Exceptions
from src.collision_info import CollisionInfo

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

    def CollideWith(other_rigid_body):
        return CollisionInfo(self, other_rigid_body)
