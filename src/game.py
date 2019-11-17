import sys
import pygame

from src.ball import Ball
from src.board import Board
from src.constants import Colors
from src.camera import *
from src.player import *
from src.blocks import *
from pygame import *


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + Display.WIDTH / 2, -t + Display.HEIGHT / 2

    l = min(0, l)  # Не движемся дальше левой границы
    l = max(-(camera.width - Display.WIDTH), l)  # Не движемся дальше правой границы
    t = max(-(camera.height - Display.HEIGHT), t)  # Не движемся дальше нижней границы
    t = min(0, t)  # Не движемся дальше верхней границы

    return Rect(l, t, w, h)


class Game:
    def __init__(self, width=1024, height=640):
        self.width = width
        self.height = height
        self.size = [self.width, self.height]
        self.library_init()
        self.game_over = False
        self.create_game_objects()
        self.timer = pygame.time.Clock()
        self.platforms = []  # то, во что мы будем врезаться или опираться

    def create_game_objects(self):
        self.objects = []
        self.hero = Player(50, 50)
        self.objects.append(self.hero)
        self.entities = []
        self.entities.append(self.hero)

    def library_init(self):
        pygame.init()  # Инициализация библиотеки
        pygame.font.init()
        self.screen = pygame.display.set_mode(self.size)  # Создание окна (установка размера)
        pygame.display.set_caption("Super Mario")  # Пишем в шапку

    def test_level(self):
        x = y = 0  # координаты
        for row in Level.test_level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    self.platforms.append(pf)
                    self.entities.append(pf)
                x += PLATFORM.WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM.HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля

    def main_loop(self):
        while not self.game_over:  # Основной цикл работы программы
            self.process_events()
            self.process_logic()
            self.process_draw()
        sys.exit(0)  # Выход из программы

    def process_draw(self):
        self.screen.fill(Colors.RED)  # Заливка цветом TODO: Работа дизайнеров
        self.test_level()

        for item in self.objects:
            item.process_draw(self.screen)

        self.total_level_width = len(Level.test_level[0]) * PLATFORM.WIDTH  # Высчитываем фактическую ширину уровня
        self.total_level_height = len(Level.test_level) * PLATFORM.HEIGHT  # высоту
        camera = Camera(camera_configure, self.total_level_width, self.total_level_height)
        camera.update(self.hero)

        #self.hero.update(self.platforms)
        for ent in self.entities:
            self.screen.blit(ent.image, camera.apply(ent))
        pygame.display.flip()
        pygame.time.wait(5)

    def process_logic(self):
        for item in self.objects:
            item.update(self.platforms)
            item.process_logic()

    def process_events(self):
        for event in pygame.event.get():  # Обработка всех событий
            if event.type == pygame.QUIT:  # Обработка события выхода
                self.game_over = True
            for item in self.objects:
                item.process_event(event)
