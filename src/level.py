﻿import glob
import pygame

from src.static_grid import StaticGrid
from src.entity import Entity
from src.io_tools import IO_Tools
from src.entity_set import EntitySet
from src.base_classes import DrawableObject
from src.exceptions import Exceptions
from src.static_grid_cell import StaticGridCell
from src.entities.player import Player
from src.camera import Camera
from src.entities.death_touch_entity import DeathTouchEntity
from src.rigid_body import RigidBody


# Уровень и информация о нём
# Каждый уровень в папке levels имеет свою папку
# Пример создания : Level(game, "level_0")
class Level(DrawableObject):
    def __init__(self, game, name):
        super().__init__(game)
        self.images = { }
        slash = IO_Tools.sep_slash()
        lvl_path = "levels{1}{0}{1}".format(name, slash)
        sprites_dir = "{}sprites{}".format(lvl_path, slash)
        for img_path in glob.glob(sprites_dir + "*.png"):
            image = pygame.image.load(img_path)
            img_rect = image.get_rect()
            if (img_rect.width == 64) and (img_rect.height == 64):
                img_name = img_path[img_path.rfind(slash) + 1 : img_path.rfind('.')]
                self.images[img_name] = image
        self.background = pygame.image.load(lvl_path + "background.png")
        lvl_file = open(lvl_path + "struct.txt")
        lvl_struct_lines = lvl_file.readlines()
        lvl_file.close()
        for i in range(len(lvl_struct_lines)):
            lvl_struct_lines[i] = lvl_struct_lines[i].strip("\n\r")
        self.grid = StaticGrid(game, self, lvl_struct_lines, self.images)
        self.entity_set = EntitySet(game, self, lvl_struct_lines, self.images)
        self.player = None
        self.__collect_rigid_bodies()
        self.__rigid_bodies_to_add = []
        self.__rigid_bodies_to_delete = []
        self.camera = Camera(game, self.width, self.height)

    def will_rigid_body_be_deleted(self, rigid_body):
        if not isinstance(rigid_body, RigidBody):
            Exceptions.throw(Exceptions.argument_type)
        return rigid_body in self.__rigid_bodies_to_delete

    def __collect_rigid_bodies(self):
        self.rigid_bodies = []
        for row in self.grid.cells:
            for cell in row:
                if cell != None:
                    self.rigid_bodies.append(cell)
        for entity in self.entity_set.entities:
            self.rigid_bodies.append(entity)
            if isinstance(entity, Player):
                self.player = entity
        self.__sort_rigid_bodies()

    def __sort_rigid_bodies(self):
        self.rigid_bodies.sort(key=lambda elem: elem.drawing_priority())

    @property
    def width(self):
        return self.grid.width << 6

    @property
    def height(self):
        return self.grid.height << 6

    def delete_static_grid_cell(self, locx, locy):
        cell = self.grid.cells[locy][locx]
        if cell != None:
            self.__rigid_bodies_to_delete.append(cell)

    def delete_entity(self, entity):
        if not isinstance(entity, Entity):
            Exceptions.throw(Exceptions.argument_type)
        self.__rigid_bodies_to_delete.append(entity)

    def __delete_rigid_bodies(self):
        for rb in self.__rigid_bodies_to_delete:
            self.rigid_bodies.remove(rb)
            if isinstance(rb, StaticGridCell):
                self.grid.cells[rb.locy][rb.locx] = None
            else:
                self.entity_set.entities.remove(rb)
                if rb == self.player:
                    self.player = None
        self.__rigid_bodies_to_delete.clear()

    def add_new_static_grid_cell(self, cell):
        if not isinstance(cell, StaticGridCell):
            Exceptions.throw(Exceptions.argument_type)
        self.__rigid_bodies_to_add.append(cell)

    def add_new_entity(self, entity):
        if not isinstance(entity, Entity):
            Exceptions.throw(Exceptions.argument_type)
        self.__rigid_bodies_to_add.append(entity)

    def __add_new_rigid_bodies(self):
        for rb in self.__rigid_bodies_to_add:
            self.rigid_bodies.append(rb)
            if isinstance(rb, StaticGridCell):
                if self.grid.cells[rb.locy][rb.locx] != None:
                    Exceptions.throw(Exceptions.invalid_operation, "the specified location already contains a cell")
                self.grid.cells[rb.locy][rb.locx] = rb
            else:
                self.entity_set.entities.append(rb)
                if (self.player == rb) and (self.player == None):
                    self.player = rb
        if len(self.__rigid_bodies_to_add) > 0:
            self.__rigid_bodies_to_add.clear()
            self.__sort_rigid_bodies()

    def process_draw(self):
        if self.player != None:
            self.camera.update(self.player.rect)
            self.__draw_background()
        else:
            self.game_object.screen.blit(self.background, self.background.get_rect())
        for rb in self.rigid_bodies:
            rb.process_draw()

    def __draw_background(self, speed=0.2):
        bg_rect = self.background.get_rect()
        max = self.width - self.game_object.width
        if (self.camera.state.x != 0) and (self.camera.state.x != -max):
            bg_rect.x = ((self.game_object.width >> 1) - self.player.rect.centerx) * speed
            bg_rect.x %= self.game_object.width
            self.game_object.screen.blit(self.background, bg_rect)
            bg_rect.x -= self.game_object.width
        elif self.camera.state.x == -max:
            bg_rect.x = max * -speed
            self.game_object.screen.blit(self.background, bg_rect)
            bg_rect.x += self.game_object.width
        self.game_object.screen.blit(self.background, bg_rect)

    def process_logic(self):
        for rb in self.rigid_bodies:
            if isinstance(rb, Entity):
                rb.apply_velocity()
        for rb in self.rigid_bodies:
            if not rb.do_register_collisions():
                continue
            dt = isinstance(rb, DeathTouchEntity)
            collisions = []
            for opp_rb in self.rigid_bodies:
                if (rb != opp_rb) and rb.quick_collide_with(opp_rb):
                    collisions.append(rb.collide_with(opp_rb))
                    if dt and isinstance(opp_rb, Player):
                        rb.on_collide_with_player(collisions[-1])
                        self.player.on_collide_with_dte(collisions[-1])
            if len(collisions) > 0:
                rb.on_collide(collisions)
        for rb in self.rigid_bodies:
            rb.process_logic()
        self.__delete_rigid_bodies()
        self.__add_new_rigid_bodies()

    def process_event(self, event):
        for rb in self.rigid_bodies:
            rb.process_event(event)
