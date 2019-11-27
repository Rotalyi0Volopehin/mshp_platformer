from src.level import Level
from src.exceptions import Exceptions


class GameplayStage:
    def __init__(self, game):
        if type(game).__name__ != "Game":
            Exceptions.throw(Exceptions.argument_type)
        self.game = game
        self.levels = [Level(game, "0")]
        game.objects.append(self.levels[0])
        self.current_level_index = 0

    def current_level(self):
        return self.levels[self.current_level_index]