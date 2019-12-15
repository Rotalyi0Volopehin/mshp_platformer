import pygame

from src.arch.static_grid_cell import StaticGridCell


class PlayerGhost(StaticGridCell):
    def __init__(self, game, image, locx, locy):
        image = pygame.transform.flip(image, True, False)
        super().__init__(game, image, locx, locy)

    def process_logic(self):
        if (self.level.player != None) and self.quick_collide_with(self.level.player):
            self.disappear()
            self.game_object.gameplay_stage.player_lifes += 1

    def do_register_collisions(self):
        return False