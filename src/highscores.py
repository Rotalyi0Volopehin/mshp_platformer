import pygame

from src.io_tools import IO_Tools
from src.constants import Color


class Highscore:
    highscore = None

    def __init__(self):
        Highscore.highscore = self
        self.score = 0
        self.font = pygame.font.Font('..{0}fonts{0}RetroGaming.ttf'.format(IO_Tools.sep_slash()), 24)
        self.load()
        self.process_render()

    def load(self):
        self.scores = []
        file = open("scores{}highscores.txt".format(IO_Tools.sep_slash()), 'r', encoding='utf-8')
        for line in file:
            if len(line) == 0:
                continue
            self.scores.append(int(line.strip()))
        file.close()

    def process_render(self):
        self.render = pygame.Surface((100, 320))
        self.render.fill((96, 150, 255))
        for i in range(len(self.scores)):
            score = self.scores[i]
            score_img = self.font.render(str(score), False, Color.WHITE)
            rect = score_img.get_rect()
            rect.centerx = 50
            rect.y = i * 30 + 10
            self.render.blit(score_img, rect)

    def draw(self, screen):
        rect = self.render.get_rect()
        screen_rect = screen.get_rect()
        rect.centerx = screen_rect.width >> 1
        rect.centery = screen_rect.height >> 1
        screen.blit(self.render, rect)

    def add_score(self, score):
        if len(self.scores) == 10:
            if (score <= self.scores[-1]) and (len(self.scores) == 10):
                return
            self.scores.pop(-1)
        self.scores.append(score)
        self.scores.sort()
        self.process_render()

    def save(self):
        file = open("scores{}highscores.txt".format(IO_Tools.sep_slash()), 'w', encoding='utf-8')
        for score in self.scores:
            file.write(str(score) + '\n')
        file.close()