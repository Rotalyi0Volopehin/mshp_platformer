from src.entity import Entity
from src.exceptions import Exceptions


class DeathTouchEntity(Entity): #abstract
    def __init__(self, game, image, posx, posy, dt_left, dt_top, dt_right, dt_down, trampoline):
        super().__init__(game, image, posx, posy)
        self.dt_info = DeathTouchEntityInfo(dt_left, dt_top, dt_right, dt_down, trampoline)

    def on_collide_with_player(self, collision): #event
        pass


class DeathTouchEntityInfo:
    def __init__(self, dt_left, dt_top, dt_right, dt_bottom, trampoline):
        if not (isinstance(dt_left, bool) and isinstance(dt_top, bool) and isinstance(dt_right, bool) and isinstance(dt_bottom, bool) and isinstance(trampoline, bool)):
            Exceptions.throw(Exceptions.argument_type)
        self.dt_left = dt_left
        self.dt_top = dt_top
        self.dt_right = dt_right
        self.dt_bottom = dt_bottom
        self.trampoline = trampoline