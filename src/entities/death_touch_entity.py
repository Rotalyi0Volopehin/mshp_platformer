from src.entity import Entity
from src.exceptions import Exceptions


# Это сущность, убивающая с тычка
class DeathTouchEntity(Entity): #abstract
    def __init__(self, game, image, posx, posy, death_touch_info):
        super().__init__(game, image, posx, posy)
        if not isinstance(death_touch_info, DeathTouchEntityInfo):
            Exceptions.throw(Exceptions.argument_type)
        self.dt_info = death_touch_info

    def on_collide_with_player(self, collision): #event
        pass


# Это просто информация о сущности, убивающей с тычка
class DeathTouchEntityInfo:
    def __init__(self, dt_left, dt_top, dt_right, dt_bottom, trampoline):
        if not (isinstance(dt_left, bool) and isinstance(dt_top, bool) and isinstance(dt_right, bool) and isinstance(dt_bottom, bool) and isinstance(trampoline, bool)):
            Exceptions.throw(Exceptions.argument_type)
        self.dt_left = dt_left
        self.dt_top = dt_top
        self.dt_right = dt_right
        self.dt_bottom = dt_bottom
        self.trampoline = trampoline