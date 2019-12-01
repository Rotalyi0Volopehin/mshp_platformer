from src.entity import Entity
from src.static_grid_cells.obstacle import Obstacle
from src.entities.player import Player


# Родительский класс всех NPC
class NPC(Entity):

    def __init__(self, game, image, posx, posy):
        super().__init__(game, image, posx, posy)
        self.alive = True
        self.on_ground = False

    def process_logic(self):
        # self.on_ground = False
        pass

    def on_collide(self, collisions):
        for collision in collisions:
            # Коллизия с препятствием
            if isinstance(collision.opp_rb, Obstacle):
                if collision.bottom:
                    self.on_ground = True
                self.obstacle_collision(collision)
            # Коллизия с игроком
            if isinstance(collision.opp_rb, Player):
                self.player_collision(collision)

    def player_collision(self, collision):
        pass

    def obstacle_collision(self, collision):
        pass

    def die(self):
        self.alive = False
        # level = self.game_object.current_level()
        # level.delete_entity(self)
        # level.delete_static_grid_cell(collision.opp_rb.locx, collision.opp_rb.locy)
