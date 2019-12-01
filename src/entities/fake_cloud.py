from src.entity import Entity
from src.static_grid_cells.obstacle import Obstacle


# Облачко, двигающееся вправо-влево, пока не встретит препятствие или край уровня
class FakeCloud(Entity):
    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy)
        self.vx = 0.5 #Начальная скорость по X
        self.collision_left = self.collision_right = False

    def drawing_priority(self):
        return -1

    def process_logic(self):
        if (self.vx > 0) and ((self.rect.right >= self.game_object.gameplay_stage.current_level.width - 1) or self.collision_right):
            self.vx = -abs(self.vx) #Отражение налево (препятствие справа)
        elif (self.vx < 0) and ((self.rect.x <= 0) or self.collision_left):
            self.vx = abs(self.vx) #Отражение направо (препятствие слева)
        self.collision_left = self.collision_right = False

    def on_collide(self, collisions):
        for collision in collisions:
            if isinstance(collision.opp_rb, Obstacle): #Столкновение с препятствием
                if collision.left:
                    self.collision_left = True
                if collision.right:
                    self.collision_right = True
                    #level = self.game_object.current_level()
                    #level.delete_entity(self)
                    #level.delete_static_grid_cell(collision.opp_rb.locx, collision.opp_rb.locy)
                if self.collision_left and self.collision_right:
                    return