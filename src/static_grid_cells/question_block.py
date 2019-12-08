from src.entities.player import Player
from src.static_grid_cell import StaticGridCell
from src.entities.animation import Animation
from src.static_grid_cells.brick_cell import BrickCell


class Question(StaticGridCell):
    def on_collide(self, collisions):
        for collision in collisions:
            if isinstance(collision.opp_rb, Player):
                if collision.bottom:
                    self.summon()
                return

    def summon(self):
        level = self.level
        self.disappear()
        level.add_new_entity(Animation(self.game_object, level.images["Coin"], self.rect.x, self.rect.y, 20, 0, -3))
        level.add_new_static_grid_cell(BrickCell(self.game_object, level.images["BrickCell"], self.locx, self.locy))