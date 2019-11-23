import sys
import pygame
import time

from src.ball import Ball
from src.board import Board
from src.constants import Color
from src.mushroom import Mushroom
from src.level import Level


class Game:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.size = [self.width, self.height]
        self.loop_delay = 5
        self.library_init()
        self.game_over = False
        self.objects = []
        self.levels = [Level(self, "0")]
        self.objects = [self.levels[0]]
        self.current_level_index = 0
        # === TEMP ===
        self.objects.append(Mushroom(self, 0, 20))
        # === ==== ====
        #self.create_game_objects()

    def current_level(self):
        return self.levels[self.current_level_index]

    def create_game_objects(self):
        for i in range(5):
            self.objects.append(Ball(self))
        self.objects.append(Board(self))

    def library_init(self):
        if not pygame.display.get_init(): #Инициализация библиотеки
            pygame.display.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(self.size)  # Создание окна (установка размера)

    def main_loop(self):
        while not self.game_over:  # Основной цикл работы программы
            start_time = time.time()
            self.process_events()
            self.process_logic()
            self.process_draw()
            time_elapsed = int((time.time() - start_time) * 1000)
            time_left = self.loop_delay - time_elapsed
            if time_left > 0:
                pygame.time.wait(time_left)
        sys.exit(0)  # Выход из программы

    def process_draw(self):
        self.screen.fill(Color.BLACK)  # Заливка цветом
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
