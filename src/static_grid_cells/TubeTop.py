from src.exceptions import Exceptions
from src.obstacle import Obstacle
from src.rigid_body import RigidBody
from src.rigid_body import CollisionInfo

class TubeTop(Obstacle):
    def collide_with(self, other_rigid_body):
        return CollisionInfo(self, other_rigid_body)

    def quick_collide_with(self, other_rigid_body):
        if not isinstance(other_rigid_body, RigidBody):
            Exceptions.throw(Exceptions.argument_type)
        return self.rect.colliderect(other_rigid_body.rect)

    def on_collide(self, collisions):
        pass
        #if self.collide_with(Mario) == CollisionInfo.top:
            #level.change()                                    Спускаемся парни, готовьте жепу