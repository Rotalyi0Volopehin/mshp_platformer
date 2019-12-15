import os

from src.arch.level import Level
from src.base_classes import DrawableObject


class GameplayStage(DrawableObject):
    def __init__(self, game):
        super().__init__(game)
        self.current_level_index = 0
        self.__pause_was = self.pause = True
        self.load()
        self.player_lifes = 2

    def load(self):
        self.levels = []
        dirs = os.listdir("levels")
        dirs.sort()
        for dir in dirs:
            self.levels.append(Level(self.game_object, dir))

    def toggle_pause(self):
        self.pause = not self.pause

    @property
    def current_level(self):
        return self.levels[self.current_level_index]

    def restart_level(self):
        self.game_object.coins.restart_level()
        self.game_object.score.restart_level()
        self.current_level.restart()

    def next_level(self):
        self.current_level.stop_bgm()
        self.current_level_index += 1
        self.game_object.coins.next_level()
        self.game_object.score.next_level()
        if self.current_level_index == len(self.levels):
            self.game_object.game_over = True
            self.current_level_index = 0
        else:
            self.current_level.restart()

    def process_draw(self):
        if not self.pause:
            self.current_level.process_draw()

    def process_logic(self):
        if self.__pause_was != self.pause:
            if self.pause:
                self.current_level.stop_bgm()
            else:
                self.current_level.play_bgm()
            self.__pause_was = self.pause
        if not self.pause:
            self.current_level.process_logic()

    def process_event(self, event):
        if not self.pause:
            self.current_level.process_event(event)