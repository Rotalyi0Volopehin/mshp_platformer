from src.rigid_body import RigidBody
from src.exceptions import Exceptions

# Это информация о столкновении двух RigidBody (главного и дополнительного)
# Поля left, top, right, bottom - флаги столкновения тел относительно главного тела
class CollisionInfo: #abstract
    def __init__(main_rigid_body, opp_rigid_body):
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

    def is_collision():
        return self.left or self.top or self.right or self.bottom
