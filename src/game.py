import sys
import pygame
import time
from src.constants import Color
from src.gameplay_stage import GameplayStage


class Game:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.size = [self.width, self.height]
        self.loop_delay = 10
        self.library_init()
        self.game_over = False
        self.gameplay_stage = GameplayStage(self)
        self.objects = [self.gameplay_stage]

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
            time_elapsed = int((time.time() - start_time) * 1000)
            time_left = self.loop_delay - time_elapsed
            if time_left > 0:
                pygame.time.wait(time_left)
        sys.exit(0)  # Выход из программы

    def process_draw(self):
        self.screen.fill(Color.BOLD)  # Заливка цветом
        for item in self.objects:
            item.process_draw()
        pygame.display.flip()  # Double buffering
        pygame.time.wait(5)

    def process_logic(self):
        for item in self.objects:
            item.process_logic()

    def process_events(self):
        for event in pygame.event.get():  # Обработка всех событий
            if event.type == pygame.QUIT:  # Обработка события выхода
                self.game_over = True
            for item in self.objects:
                item.process_event(event)
