import sys
import pygame
from src.io_tools import *
from src.camera import Camera
from src.constants import *
from src.static_grid_cells.brick_cell import Obstacle
from src.entities.player import Player


class CastleEntry(Obstacle):
    def __init__(self, game, image, locx, locy):
        super().__init__(game, image, locx, locy)
        slash = IO_Tools.sep_slash()
        lvl_path = "levels{1}level_{0}{1}".format('0', slash)
        sprites_dir = "{}sprites{}".format(lvl_path, slash)
        self.castle_image = pygame.image.load(sprites_dir + "Castle.png")
        self.castle_rect = self.castle_image.get_rect()
        self.castle_rect.topleft = self.rect.topleft

    def collide_with(self, other_rigid_body):
        if isinstance(other_rigid_body, Player):
            sys.exit() #ЗАМЕНИТЬ НА ПЕРЕХОД НА НОВЫЙ УРОВЕНЬ

    def process_draw(self):
        super().process_draw()
        level = self.game_object.gameplay_stage.current_level
        self.castle_rect = level.camera.apply(self.rect)
        self.game_object.screen.blit(self.castle_image, self.castle_rect)
