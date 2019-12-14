from src.static_grid_cell import StaticGridCell


class Princess(StaticGridCell):
    def process_logic(self):
        level = self.level
        if (level.boss is None) and (level.player != None):
            if self.quick_collide_with(level.player):
                self.game_object.gameplay_stage.next_level()

    def process_draw(self):
        if self.level.boss is None:
            self.rect.x += 64
            super().process_draw()
            self.rect.x -= 64

    def do_register_collisions(self):
        return False