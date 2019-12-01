import pygame

from src.base_classes import DrawableObject
from src.exceptions import Exceptions


# Это твёрдое тело с физическими параметрами (коллизией и геометрией)
class RigidBody(DrawableObject): #abstract
    def __init__(self, game, rect):
        super().__init__(game)
        if not isinstance(rect, pygame.Rect):
            Exceptions.throw(Exceptions.argument_type, "parameter \"rect\" must be pygame.Rect")
        if (rect.width != 64) or (rect.height != 64):
            Exceptions.throw(Exceptions.argument, "size of rigid body must be 64x64 pixels")
        self.rect = rect

    def drawing_priority(self):
        return 0

    def collide_with(self, other_rigid_body):
        return CollisionInfo(self, other_rigid_body)

    def quick_collide_with(self, other_rigid_body):
        if not isinstance(other_rigid_body, RigidBody):
            Exceptions.throw(Exceptions.argument_type)
        return self.rect.colliderect(other_rigid_body.rect)

    def on_collide(self, collisions): #abstract event
        pass

    def process_draw(self):
        level = self.game_object.gameplay_stage.current_level()
        rect = self.rect if level.player == None else level.camera.apply(self.rect)
        self.game_object.screen.blit(self.image, rect)


# Это информация о столкновении двух RigidBody (главного и дополнительного)
# Поля left, top, right, bottom - флаги столкновения тел относительно главного тела
class CollisionInfo:
    def __init__(self, main_rigid_body, opp_rigid_body):
        if not (isinstance(main_rigid_body, RigidBody) and isinstance(opp_rigid_body, RigidBody)):
            Exceptions.throw(Exceptions.argument_type)
        self.main_rb = main_rigid_body
        self.opp_rb = opp_rigid_body
        main_rect = self.main_rb.rect
        opp_rect = self.opp_rb.rect
        if main_rect.colliderect(opp_rect):
            self.left = (main_rect.left >= opp_rect.centerx) and (main_rect.left <= opp_rect.right)
            self.top = (main_rect.top >= opp_rect.centery) and (main_rect.top <= opp_rect.bottom)
            self.right = (main_rect.right <= opp_rect.centerx) and (main_rect.right >= opp_rect.left)
            self.bottom = (main_rect.bottom <= opp_rect.centery) and (main_rect.bottom >= opp_rect.top)
        else:
            self.left = self.top = self.right = self.bottom = False

    def is_collision(self):
        return self.left or self.top or self.right or self.bottom
