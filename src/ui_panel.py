from src.base_classes import DrawableObject
from src.coins import Coins
from src.score import Score
from src.time import TimeGame
from src.constants import get_retro_font


class UI_Panel(DrawableObject):
    def __init__(self, game):
        super().__init__(game)
        font = get_retro_font(30)
        self.coins = Coins(game, font, 325)
        self.score = Score(game, font, 325)
        self.time = TimeGame(game, font, 325)

    def process_draw(self):
        if not self.game_object.gameplay_stage.pause:
            self.coins.process_draw()
            self.score.process_draw()
            self.time.process_draw()

    def process_logic(self):
        if not self.game_object.gameplay_stage.pause:
            self.time.process_logic()