import pygame
import time

from src.gameplay_stage import GameplayStage
from src.time import TimeGame
from src.coins import Coins
from src.score import Score
from src.constants import Color
from src.highscores import Highscore
from src.io_tools import IO_Tools
from src.lifes_stage import LifesStage
from src.BossAttention import Label



class Game:
    def __init__(self, width=1024, height=640):
        self.width = width
        self.height = height
        self.size = [self.width, self.height]
        self.loop_delay = 25
        self.library_init()
        self.game_over = False
        self.gameplay_stage = None
        self.gameplay_stage = GameplayStage(self)
        self.objects = [self.gameplay_stage]

        self.create_game_objects()
        self.pr_quit = False
        self.display_player_lifes()

    def create_game_objects(self):
        self.objects.append(TimeGame(self))
        self.score = Score(self)
        self.BossAttention = Label(self)
        self.objects.append(self.BossAttention)
        self.coins = Coins(self)
        self.objects.append(self.coins)

    def library_init(self):
        if not pygame.display.get_init():  # Инициализация библиотеки
            pygame.display.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(self.size)  # Создание окна (установка размера)
        pygame.display.set_caption("Super Mario")  # Пишем в шапку

    def main_loop(self):
        while not self.game_over:  # Основной цикл работы программы
            if self.__display_player_lifes_time > 0:
                self.__display_player_lifes_time -= 1
                if self.__display_player_lifes_time == 0:
                    self.gameplay_stage.pause = False
            start_time = time.time()
            self.process_events()
            self.process_logic()
            self.process_draw()
            time_elapsed = int((time.time() - start_time) * 1000)
            time_left = self.loop_delay - time_elapsed
            if time_left < 0:
                print(time_elapsed, self.loop_delay, sep='/')
            pygame.display.set_caption("Super Mario [!]" if time_left < 0 else "Super Mario")
            if time_left > 0:
                pygame.time.wait(time_left)
        self.write_scores()

    def process_draw(self):
        # self.screen.fill(Color.BOLD)  # Заливка цветом
        for item in self.objects:
            item.process_draw()
        pygame.display.flip()  # Double buffering

    def process_logic(self):
        for item in self.objects:
            item.process_logic()

    def process_events(self):
        for event in pygame.event.get():  # Обработка всех событий
            if event.type == pygame.QUIT:  # Обработка события выхода
                self.game_over = True
                self.pr_quit = True
            if event.type == pygame.KEYUP:  # Обработка события выхода
                if event.key == pygame.K_ESCAPE:
                    self.game_over = True
                elif (event.key == pygame.K_SPACE) and (self.__display_player_lifes_time == 0):
                    self.gameplay_stage.toggle_pause()
            for item in self.objects:
                item.process_event(event)

    def display_player_lifes(self):
        self.__display_player_lifes_time = 80
        self.gameplay_stage.pause = True
        LifesStage.draw(self, self.gameplay_stage.player_lifes)

    def write_scores(self):
        self.file = open("scores{}highscores.txt".format(IO_Tools.sep_slash()), mode='a', encoding='utf-8')
        self.file.write(str(self.score.get_score()) + '\n')
        self.file.close()

