import os
import pygame
from src.base_classes import DrawableObject


class Highscore(DrawableObject):
    pygame.font.init()
    font = pygame.font.Font('font/RetroGaming.ttf', 46)

    def __init__(self):
        self.score = 0
        self.file = open("scores/highscores.txt", mode='r', encoding='utf-8')
        self.scores = []
        self.int_sc = []
        self.count = 0
        for i in self.file:
            self.count += 1
            f = i.split()
            ts = self.font.render(f[0], False, (255, 255, 255))
            self.scores.append(ts)
            self.int_sc.append(int(f[0]))
        self.file.close()

    def process_event(self):
        self.score = 0
        self.file = open("scores/highscores.txt", mode='r', encoding='utf-8')
        self.scores = []
        self.int_sc = []
        self.count = 0
        for i in self.file:
            self.count += 1
            f = i.split()
            ts = self.font.render(f[0], False, (255, 255, 255))
            self.scores.append(ts)
            self.int_sc.append(int(f[0]))
        self.file.close()

    def process_draw(self, screen):
        ts = self.font.render("Рекорды: ", False, (255, 255, 255))
        screen.blit(ts, (400, 10))
        self.pos_x = 470
        self.pos_y = 30
        self.int_sc = sorted(self.int_sc, reverse=True)
        if self.count < 8:
            a = 0
            for item in self.int_sc:
                if (a == 0):
                    self.pos_y += 50
                    a += 1
                    screen.blit(self.font.render(str(item), False, (255, 255, 0)), (self.pos_x, self.pos_y))
                elif (a == 1):
                    self.pos_y += 50
                    a += 1
                    screen.blit(self.font.render(str(item), False, (192, 192, 192)), (self.pos_x, self.pos_y))
                elif (a == 2):
                    self.pos_y += 50
                    a += 1
                    screen.blit(self.font.render(str(item), False, (177, 86, 15)), (self.pos_x, self.pos_y))
                else:
                    self.pos_y += 50
                    screen.blit(self.font.render(str(item), False, (255, 255, 255)), (self.pos_x, self.pos_y))
        else:
            a = 0
            for i in range(0, 8):
                item = self.int_sc[i]
                if (a == 0):
                    self.pos_y += 50
                    a += 1
                    screen.blit(self.font.render(str(item), False, (255, 255, 0)), (self.pos_x, self.pos_y))
                elif (a == 1):
                    self.pos_y += 50
                    a += 1
                    screen.blit(self.font.render(str(item), False, (192, 192, 192)), (self.pos_x, self.pos_y))
                elif (a == 2):
                    self.pos_y += 50
                    a += 1
                    screen.blit(self.font.render(str(item), False, (177, 86, 15)), (self.pos_x, self.pos_y))
                else:
                    self.pos_y += 50
                    screen.blit(self.font.render(str(item), False, (255, 255, 255)), (self.pos_x, self.pos_y))

