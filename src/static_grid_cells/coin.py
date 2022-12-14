from src.entities.player import Player
from src.arch.static_grid_cell import StaticGridCell


class Coin(StaticGridCell):
    def on_collide(self, collisions):
        for collision in collisions:
            if isinstance(collision.opp_rb, Player):
                self.disappear()
                self.game_object.ui_panel.coins.process_change_coins(1)