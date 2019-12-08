import sys
import pygame
import time

<<<<<<< HEAD
from src.constants import Color
from src.gameplay_stage import GameplayStage


class Game:
    def __init__(self, width=1024, height=640):
=======
from src.ball import Ball
from src.board import Board
from src.time import TimeGame
from src.coins import Coins
from src.score import Score
from src.constants import Color
from src.highscores import Highscore


class Game:
    def __init__(self, width, height):
>>>>>>> origin/UI
        self.width = width
        self.height = height
        self.size = [self.width, self.height]
        self.loop_delay = 25
        self.library_init()
        self.game_over = False
<<<<<<< HEAD
        self.gameplay_stage = GameplayStage(self)
        self.objects = [self.gameplay_stage]
=======
        self.create_game_objects()

    def create_game_objects(self):
        self.objects = []
        for i in range(5):
            self.objects.append(Ball(self))
        self.objects.append(Board(self))
        self.objects.append(TimeGame(self))
        self.objects.append(Score(self))
        self.objects.append(Coins(self))
>>>>>>> origin/UI

    def library_init(self):
        if not pygame.display.get_init(): #Инициализация библиотеки
            pygame.display.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(self.size)  # Создание окна (установка размера)
        pygame.display.set_caption("Super Mario")  # Пишем в шапку

    def main_loop(self):
        while not self.game_over:  # Основной цикл работы программы
            start_time = time.time()
            self.process_events()
            self.process_logic()
            self.process_draw()
<<<<<<< HEAD
            time_elapsed = int((time.time() - start_time) * 1000)
            time_left = self.loop_delay - time_elapsed
            if time_left < 0:
                print(time_elapsed, self.loop_delay, sep='/')
            pygame.display.set_caption("Super Mario [!]" if time_left < 0 else "Super Mario")
            if time_left > 0:
                pygame.time.wait(time_left)
        sys.exit(0)  # Выход из программы
=======
        #sys.exit(0)  # TODO: Сделать выход в меню
        self.write_scores()

>>>>>>> origin/UI

    def process_draw(self):
        #self.screen.fill(Color.BOLD)  # Заливка цветом
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
            for item in self.objects:
                item.process_event(event)
<<<<<<< HEAD
=======

    def write_scores(self):
        self.file = open("scores/highscores.txt", mode='a', encoding='utf-8')
        self.file.write(str(self.objects[7].get_score()) + '\n') #TODO  object[7] - класс Score (как в марио он обозначен не знаю)
        self.file.close()
>>>>>>> origin/UI
