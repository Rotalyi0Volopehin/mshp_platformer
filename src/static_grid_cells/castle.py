import pygame

from src.static_grid_cell import StaticGridCell
from src.entities.player import Player


class CastleEntry(StaticGridCell):
    def __init__(self, game, image, locx, locy):
        super().__init__(game, image, locx, locy)
        self.castle_image = self.level.images["Castle"]
        self.castle_rect = self.castle_image.get_rect()
        self.castle_rect.bottom = self.rect.bottom
        self.castle_rect.centerx = self.rect.centerx

    def do_register_collisions(self):
        return False

    def process_logic(self):
        level = self.level
        if (level.player != None) and self.quick_collide_with(level.player):
            self.game_object.gameplay_stage.next_level()

    def process_draw(self):
        super().process_draw()
        castle_rect = self.level.camera.apply(self.castle_rect)
        self.game_object.screen.blit(self.castle_image, castle_rect)

    def drawing_priority(self):
        return 11