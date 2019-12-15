import glob
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
from src.entities.turtle import Turtle


# Уровень и информация о нём
# Каждый уровень в папке levels имеет свою папку
# Пример создания : Level(game, "level_0")
class Level(DrawableObject):
    active_level = None
    __prev_level = None

    def __init__(self, game, name):
        RigidBody.level_type = Level
        Level.active_level = self
        super().__init__(game)
        slash = IO_Tools.sep_slash()
        self.__level_path = "levels{1}{0}{1}".format(name, slash)
        self.__load_sprites()
        self.restart()
        Level.active_level = None
        Level.__prev_level = self

    def __load_sprites(self):
        self.images = { }
        if Level.__prev_level != None:
            for sprite_name in Level.__prev_level.images:
                self.images[sprite_name] = Level.__prev_level.images[sprite_name]
        slash = IO_Tools.sep_slash()
        sprites_dir = "{}sprites{}".format(self.__level_path, slash)
        for img_path in glob.glob(sprites_dir + "*.png"):
            image = pygame.image.load(img_path)
            img_name = img_path[img_path.rfind(slash) + 1: img_path.rfind('.')]
            self.images[img_name] = image
        self.__load_background(self.__level_path)

    def restart(self):
        lvl_file = open(self.__level_path + "struct.txt")
        lvl_struct_lines = lvl_file.readlines()
        lvl_file.close()
        for i in range(len(lvl_struct_lines)):
            lvl_struct_lines[i] = lvl_struct_lines[i].strip("\n\r")
        self.grid = StaticGrid(self.game_object, self, lvl_struct_lines, self.images)
        self.entity_set = EntitySet(self.game_object, self, lvl_struct_lines, self.images)
        self.boss = self.player = None
        self.__collect_rigid_bodies()
        self.__rigid_bodies_to_add = []
        self.__rigid_bodies_to_delete = []
        self.camera = Camera(self.game_object, self.width, self.height)
        if Level.active_level is None:
            self.game_object.display_player_lifes()

    def __load_background(self, lvl_path):
        bg_low = pygame.image.load(lvl_path + "background_low.png")
        bg_high = pygame.image.load(lvl_path + "background_high.png")
        bg_rect = bg_low.get_rect()
        self.background_even = pygame.Surface((bg_rect.width * 3, bg_rect.height))
        self.background_odd = pygame.Surface((bg_rect.width * 3, bg_rect.height))
        self.background_even.blit(bg_low, bg_rect)
        self.background_odd.blit(bg_high, bg_rect)
        bg_rect.x += bg_rect.width
        self.background_even.blit(bg_high, bg_rect)
        self.background_odd.blit(bg_low, bg_rect)
        bg_rect.x += bg_rect.width
        self.background_even.blit(bg_low, bg_rect)
        self.background_odd.blit(bg_high, bg_rect)

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
            elif isinstance(entity, Turtle):
                self.boss = entity
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
                elif rb == self.boss:
                    self.boss = None
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
                if isinstance(rb, Player) and (self.player is None):
                    self.player = rb
                elif isinstance(rb, Turtle) and (self.boss is None):
                    self.boss = rb
        if len(self.__rigid_bodies_to_add) > 0:
            self.__rigid_bodies_to_add.clear()
            self.__sort_rigid_bodies()

    def process_draw(self):
        if self.player != None:
            self.camera.update(self.player.rect)
            self.__draw_background()
        else:
            self.game_object.screen.blit(self.background_even, self.background_even.get_rect())
        for rb in self.rigid_bodies:
            rb.process_draw()

    def __draw_background(self, speed=0.2):
        max = self.width - self.game_object.width
        if (self.camera.state.x != 0) and (self.camera.state.x != -max):
            self.__draw_background_using_row(self.player.rect.centerx, speed)
        elif self.camera.state.x == -max:
            self.__draw_background_using_row(max + (self.game_object.width >> 1), speed)
        else:
            self.__draw_background_using_row(self.game_object.width >> 1, speed)

    def __draw_background_using_row(self, posx, speed):
        half_w = self.game_object.width >> 1
        bg_rect = self.background_even.get_rect()
        bg_rect.x = (half_w - posx) * speed
        even = ((bg_rect.x // half_w) & 1) == 0
        bg = self.background_even if even else self.background_odd
        bg_rect.x = (bg_rect.x % half_w) - half_w
        self.game_object.screen.blit(bg, bg_rect)

    def process_logic(self):
        self.__process_applying_velocity()
        self.__process_collisions()
        for rb in self.rigid_bodies:
            rb.process_logic()
        self.__delete_rigid_bodies()
        self.__add_new_rigid_bodies()

    def __process_applying_velocity(self):
        for rb in self.rigid_bodies:
            if isinstance(rb, Entity):
                rb.apply_velocity()

    def __process_collisions(self):
        for rb in self.rigid_bodies:
            if not rb.do_register_collisions():
                continue
            dt = isinstance(rb, DeathTouchEntity)
            collisions = []
            for opp_rb in self.rigid_bodies:
                if (rb != opp_rb) and rb.quick_collide_with(opp_rb):
                    collisions.append(rb.collide_with(opp_rb))
                    if dt and isinstance(opp_rb, Player) and not opp_rb.dead:
                        rb.on_collide_with_player(collisions[-1])
                        self.player.on_collide_with_dte(collisions[-1])
            if len(collisions) > 0:
                rb.on_collide(collisions)

    def process_event(self, event):
        for rb in self.rigid_bodies:
            rb.process_event(event)