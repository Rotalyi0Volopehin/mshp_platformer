from src.static_grid_cell import StaticGridCell
from src.entities.animation import Animation


class Princess(StaticGridCell):
    def __init__(self, game, image, locx, locy):
        super().__init__(game, image, locx, locy)
        self.thanks = None

    def process_logic(self):
        level = self.level
        if (level.boss is None) and (level.player != None):
            if (self.thanks is None) and self.quick_collide_with(level.player):
                self.thanks = Animation(self.game_object, level.images["Thanks"], self.rect.x - 64, self.rect.y - 64, 120, 0, 0)
                level.add_new_entity(self.thanks)
            elif (self.thanks != None) and (self.thanks.lifetime == 0):
                self.game_object.gameplay_stage.next_level()

    def process_draw(self):
        if self.level.boss is None:
            self.rect.x += 64
            super().process_draw()
            self.rect.x -= 64

    def do_register_collisions(self):
        return False