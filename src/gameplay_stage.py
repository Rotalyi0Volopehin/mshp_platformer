import os

from src.level import Level
from src.base_classes import DrawableObject


class GameplayStage(DrawableObject):
    def __init__(self, game):
        super().__init__(game)
        self.levels = []
        dirs = os.listdir("levels")
        dirs.sort()
        for dir in dirs:
            self.levels.append(Level(game, dir))
        self.current_level_index = 3

    @property
    def current_level(self):
        return self.levels[self.current_level_index]

    def next_level(self):
        self.current_level_index += 1
        if self.current_level_index == len(self.levels):
            self.game_object.game_over = True
            self.current_level_index = 0

    def process_draw(self):
        self.current_level.process_draw()

    def process_logic(self):
        self.current_level.process_logic()

    def process_event(self, event):
        self.current_level.process_event(event)