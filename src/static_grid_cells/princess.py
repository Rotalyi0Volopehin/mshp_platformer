from src.arch.static_grid_cell import StaticGridCell
from src.entities.animation import Animation
from src.arch.sfx_player import SFX_Player


class Princess(StaticGridCell):
    def __init__(self, game, image, locx, locy):
        super().__init__(game, image, locx, locy)
        self.thanks = None

    def process_logic(self):
        level = self.level
        if (level.boss is None) and (level.player != None):
            if (self.thanks is None) and self.quick_collide_with(level.player):
                self.thanks = Animation(self.game_object, level.images["Thanks"], self.rect.x - 128, self.rect.y - 64, 120, 0, 0)
                level.add_new_entity(self.thanks)
                SFX_Player.play_sound("Victory")
                extra_score = self.game_object.gameplay_stage.player_lifes * 100 + self.game_object.ui_panel.time.seconds
                self.game_object.ui_panel.score.process_get_score(extra_score)
            elif (self.thanks != None) and (self.thanks.lifetime == 0):
                self.game_object.gameplay_stage.next_level()

    def process_draw(self):
        if self.level.boss is None:
            self.rect.x += 64
            super().process_draw()
            self.rect.x -= 64

    def do_register_collisions(self):
        return False