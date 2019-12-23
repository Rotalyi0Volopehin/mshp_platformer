import random

from src.entities.player import Player
from src.static_grid_cells.obstacle import Obstacle
from src.entities.animation import Animation
from src.static_grid_cells.brick_cell import BrickCell
from src.entities.shell import Shell
from src.static_grid_cells.player_ghost import PlayerGhost


class Question(Obstacle):
    def on_collide(self, collisions):
        for collision in collisions:
            if isinstance(collision.opp_rb, Player):
                if collision.bottom:
                    self.summon()
                return

    def summon(self):
        self.disappear()
        key = random.getrandbits(3)
        if key == 0:
            self.summon_ghost()
        elif key < 4:
            self.summon_shells()
        else:
            self.summon_coin()
        self.level.add_new_static_grid_cell(BrickCell(self.game_object, self.level.images["BrickCell"], self.locx, self.locy))

    def summon_shells(self):
        shell = Shell(self.game_object, self.level.images["Shell"], self.rect.x, self.rect.y - 64, 240, -5)
        shell.vy = -10
        self.level.add_new_entity(shell)
        shell = Shell(self.game_object, self.level.images["Shell"], self.rect.x, self.rect.y - 64, 240, 5)
        shell.vy = -10
        self.level.add_new_entity(shell)

    def summon_coin(self):
        self.level.add_new_entity(Animation(self.game_object, self.level.images["Coin"], self.rect.x, self.rect.y, 20, 0, -3))
        self.game_object.ui_panel.coins.process_change_coins(1)

    def summon_ghost(self):
        if (self.locy == 0) or (self.level.grid.cells[self.locy - 1][self.locx] != None):
            return
        ghost = PlayerGhost(self.game_object, self.level.images["PlayerGhost"], self.locx, self.locy - 1)
        self.level.add_new_static_grid_cell(ghost)