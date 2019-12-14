import os

from src.level import Level
from src.base_classes import DrawableObject


class GameplayStage(DrawableObject):
    def __init__(self, game):
        super().__init__(game)
        self.current_level_index = 0
        self.pause = True
        self.load()
        self.player_lifes = 2

    def load(self):
        self.levels = []
        dirs = os.listdir("levels")
        dirs.sort()
        for dir in dirs:
            self.levels.append(Level(self.game_object, dir))
        self.current_level_index = 1

    def toggle_pause(self):
        self.pause = not self.pause


    @property
    def current_level(self):
        return self.levels[self.current_level_index]

    def next_level(self):
        self.current_level_index += 1
        if self.current_level_index == len(self.levels):
            self.game_object.game_over = True
            self.current_level_index = 0

    def process_draw(self):
        if not self.pause:
            self.current_level.process_draw()

    def process_logic(self):
        if not self.pause:
            self.current_level.process_logic()

    def process_event(self, event):
        if not self.pause:
            self.current_level.process_event(event)