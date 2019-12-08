import pygame

from src.static_grid_cells.brick_cell import Obstacle
from src.entities.player import Player


class CastleEntry(Obstacle):
    def __init__(self, game, image, locx, locy):
        super().__init__(game, image, locx, locy)
        self.castle_image = self.level.images["Castle"]
        self.castle_rect = self.castle_image.get_rect()
        self.castle_rect.bottom = self.rect.bottom
        self.castle_rect.centerx = self.rect.centerx

    def collide_with(self, other_rigid_body):
        if isinstance(other_rigid_body, Player):
            self.game_object.gameplay_stage.next_level()

    def process_draw(self):
        super().process_draw()
        castle_rect = self.level.camera.apply(self.castle_rect)
        self.game_object.screen.blit(self.castle_image, castle_rect)

    def drawing_priority(self):
        return 11