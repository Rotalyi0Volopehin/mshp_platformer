import pygame
import sys
from src.constants import Color
from src.highscores import Highscore

class Menu:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.width = 1024
        self.height = 640
        self.screen = pygame.display.set_mode([self.width,self.height])
        self.volume = 5
        pygame.mixer.music.load("button-40.mp3")
        pygame.mixer.music.set_volume(self.volume / 10)
        self.menuIsActive = True  # аналог game_over, для закрытия меню
        # далее - переменные, отвечающие за окна (пункты меню)
        # текущим окнам присваивается True
        self.mainIsActive = True
        self.settingsIsActive = False
        self.highscoresIsActive = False
        self.highResolution = True
        self.k = [1.0, 1.0]
        self.quit = False
        self.m_quit = False

        self.highscore = Highscore()

        self.main_font = pygame.font.Font('font/RetroGaming.ttf', 46)
        self.newGameText = self.main_font.render("Новая игра", 1, Color.WHITE)
        self.settingsText = self.main_font.render("Настройки", 1, Color.WHITE) # инициализация надписей
        self.highscoresText = self.main_font.render("Рекорды", 1, Color.WHITE)
        self.exitText = self.main_font.render("Выход", 1, Color.WHITE)

        self.lowResolText = self.main_font.render("800 x 600", 1, Color.WHITE)
        self.highResolText = self.main_font.render("1024 x 640", 1, Color.WHITE)

        self.volumeText = self.main_font.render("Громкость", 1, Color.WHITE)
        self.volumePosition = self.volumeText.get_rect(center=[220, 200])
        self.resolutionText = self.main_font.render("Разрешение", 1, Color.WHITE)
        self.resolutionPosition = self.resolutionText.get_rect(center=[220, 390])
        self.plusText = self.main_font.render("+", 1, Color.WHITE)
        self.plusPosition = self.plusText.get_rect(center=[820, 200])
        self.volumeNumText = self.main_font.render(str(self.volume), 1, Color.WHITE)
        self.volumeNumPosition = self.volumeNumText.get_rect(center=[730, 200])
        self.minusText = self.main_font.render("-", 1, Color.WHITE)
        self.minusPosition = self.minusText.get_rect(center=[650, 200])

        self.newGamePosition = self.newGameText.get_rect(center=[512, 200])
        self.settingsPosition = self.settingsText.get_rect(center=[512, 270])    # инициализация позиций надписей
        self.highscoresPosition = self.highscoresText.get_rect(center=[512, 340])
        self.exitPosition = self.exitText.get_rect(center=[512, 410])

        self.lowResolPosition = self.lowResolText.get_rect(center=[755, 360])
        self.highResolPosition = self.highResolText.get_rect(center=[755, 440])

        self.background = pygame.image.load("images/background.jpg") # здесь можно изменить фон
        self.background_rect = self.background.get_rect()

        self.goBackText = self.main_font.render("Назад", 1, Color.WHITE)
        self.goBackPosition = self.goBackText.get_rect(center=[512, 510])

    # обработка событий главного окна (главного меню)
    def main_events(self):
        mouse = pygame.mouse.get_pos()
        self.new_game_hover(mouse)
        self.settings_hover(mouse)
        self.highscores_hover(mouse)
        self.exit_hover(mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.menuIsActive = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.newGamePosition.left < mouse[0] < self.newGamePosition.right and self.newGamePosition.top < mouse[1] < self.newGamePosition.bottom:
                    self.new_game_click()
                elif self.settingsPosition.left < mouse[0] < self.settingsPosition.right and self.settingsPosition.top < mouse[1] < self.settingsPosition.bottom:
                    self.settings_click()
                elif self.highscoresPosition.left < mouse[0] < self.highscoresPosition.right and self.highscoresPosition.top < mouse[1] < self.highscoresPosition.bottom:
                    self.highscores_click()
                elif self.exitPosition.left < mouse[0] < self.exitPosition.right and self.exitPosition.top < mouse[1] < self.exitPosition.bottom:
                    self.exit_click()


    # обработка событий раздела настроек
    def settings_events(self):
        mouse = pygame.mouse.get_pos()
        self.go_back_hover(mouse)

        self.plus_hover(mouse)
        self.minus_hover(mouse)
        self.lowResol_hover(mouse)
        self.highResol_hover(mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.menuIsActive = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.goBackPosition.left < mouse[0] < self.goBackPosition.right and self.goBackPosition.top < mouse[1] < self.goBackPosition.bottom:
                    self.go_back_click()
                elif self.highResolPosition.left < mouse[0] < self.highResolPosition.right and self.highResolPosition.top < mouse[1] < self.highResolPosition.bottom:
                    self.highResol_click()
                elif self.lowResolPosition.left < mouse[0] < self.lowResolPosition.right and self.lowResolPosition.top < mouse[1] < self.lowResolPosition.bottom:
                    self.lowResol_click()
                elif self.plusPosition.left < mouse[0] < self.plusPosition.right and self.plusPosition.top < mouse[1] < self.plusPosition.bottom:
                    self.plus_click()
                elif self.minusPosition.left < mouse[0] < self.minusPosition.right and self.minusPosition.top < mouse[1] < self.minusPosition.bottom:
                    self.minus_click()

    # обработка событий раздела рекордов
    def highscores_events(self):
        mouse = pygame.mouse.get_pos()
        self.go_back_hover(mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.menuIsActive = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.goBackPosition.left < mouse[0] < self.goBackPosition.right and self.goBackPosition.top < mouse[1] < self.goBackPosition.bottom:
                    self.go_back_click()

    #Выход на крестик))
    def sys_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.menuIsActive = False
                self.m_quit = True
                self.quit = True
                sys.exit()

    # обработка нажатий на кнопки
    def new_game_click(self):
        pygame.mixer.music.play()
        self.menuIsActive = False
        self.m_quit = True
        # начало игры

    def settings_click(self):
        pygame.mixer.music.play()
        self.mainIsActive = False
        self.settingsIsActive = True

    def highscores_click(self):
        pygame.mixer.music.play()
        self.mainIsActive = False
        self.highscoresIsActive = True

    def lowResol_click(self):
        if self.highResolution:
            self.k[0] = 0.6734
            self.k[1] = 0.9375
            self.width = 800
            self.height = 600
            self.screen = pygame.display.set_mode([self.width, self.height])
            self.resolution_change()
            self.highResolution = False

    def highResol_click(self):
        if not self.highResolution:
            self.k[0] = 1.485
            self.k[1] = 1.066666
            self.width = 1024
            self.height = 640
            self.screen = pygame.display.set_mode([self.width, self.height])
            self.resolution_change()
            self.highResolution = True


    def exit_click(self):
        pygame.mixer.music.play()
        self.menuIsActive = False
        self.quit = True
        self.m_quit = True

    def go_back_click(self):
        pygame.mixer.music.play()
        self.settingsIsActive = False
        self.highscoresIsActive = False
        self.mainIsActive = True

    def resolution_change(self):
        for i in range(1):
            self.newGamePosition[i] *= self.k[i]
            self.settingsPosition[i] *= self.k[i]
            self.highscoresPosition[i] *= self.k[i]
            self.exitPosition[i] *= self.k[i]
            self.goBackPosition[i] *= self.k[i]
            self.lowResolPosition[i] *= self.k[i]
            self.highResolPosition[i] *= self.k[i]
            self.resolutionPosition[i] *= self.k[i]
            self.volumePosition[i] *= self.k[i]
            self.volumeNumPosition[i] *= self.k[i]
            self.plusPosition[i] *= self.k[i]
            self.minusPosition[i] *= self.k[i]


    def plus_click(self):
        if self.volume < 10:
            self.volume += 1
        pygame.mixer.music.set_volume(self.volume / 10)
        self.volumeNumText = self.main_font.render(str(self.volume), 1, Color.WHITE)

    def minus_click(self):
        if self.volume > 0:
            self.volume -= 1
        pygame.mixer.music.set_volume(self.volume / 10)
        self.volumeNumText = self.main_font.render(str(self.volume), 1, Color.WHITE)

    # изменение цвета кнопок при наведении на них
    def new_game_hover(self, mouse):
        if self.newGamePosition.left < mouse[0] < self.newGamePosition.right and self.newGamePosition.top < mouse[1] < self.newGamePosition.bottom:
            self.newGameText = self.main_font.render("Новая игра", 1, Color.LIGHT_GRAY)
        else:
            self.newGameText = self.main_font.render("Новая игра", 1, Color.WHITE)

    def settings_hover(self, mouse):
        if self.settingsPosition.left < mouse[0] < self.settingsPosition.right and self.settingsPosition.top < mouse[1] < self.settingsPosition.bottom:
            self.settingsText = self.main_font.render("Настройки", 1, Color.LIGHT_GRAY)
        else:
            self.settingsText = self.main_font.render("Настройки", 1, Color.WHITE)

    def highscores_hover(self, mouse):
        if self.highscoresPosition.left < mouse[0] < self.highscoresPosition.right and self.highscoresPosition.top < mouse[1] < self.highscoresPosition.bottom:
            self.highscoresText = self.main_font.render("Рекорды", 1, Color.LIGHT_GRAY)
        else:
            self.highscoresText = self.main_font.render("Рекорды", 1, Color.WHITE)

    def exit_hover(self, mouse):
        if self.exitPosition.left < mouse[0] < self.exitPosition.right and self.exitPosition.top < mouse[1] < self.exitPosition.bottom:
            self.exitText = self.main_font.render("Выход", 1, Color.LIGHT_GRAY)
        else:
            self.exitText = self.main_font.render("Выход", 1, Color.WHITE)

    def go_back_hover(self, mouse):
        if self.goBackPosition.left < mouse[0] < self.goBackPosition.right and self.goBackPosition.top < mouse[1] < self.goBackPosition.bottom:
            self.goBackText = self.main_font.render("Назад", 1, Color.LIGHT_GRAY)
        else:
            self.goBackText = self.main_font.render("Назад", 1, Color.WHITE)

    def plus_hover(self, mouse):
        if self.plusPosition.left < mouse[0] < self.plusPosition.right and self.plusPosition.top < mouse[1] < self.plusPosition.bottom:
            self.plusText = self.main_font.render("+", 1, Color.LIGHT_GRAY)
        else:
            self.plusText = self.main_font.render("+", 1, Color.WHITE)

    def minus_hover(self, mouse):
        if self.minusPosition.left < mouse[0] < self.minusPosition.right and self.minusPosition.top < mouse[1] < self.minusPosition.bottom:
            self.minusText = self.main_font.render("-", 1, Color.LIGHT_GRAY)
        else:
            self.minusText = self.main_font.render("-", 1, Color.WHITE)

    def lowResol_hover(self, mouse):
        if self.lowResolPosition.left < mouse[0] < self.lowResolPosition.right and self.lowResolPosition.top < mouse[1] < self.lowResolPosition.bottom and self.highResolution:
            self.lowResolText = self.main_font.render("800 x 600", 1, Color.LIGHT_GRAY)
        else:
            self.lowResolText = self.main_font.render("800 x 600", 1, Color.WHITE)

    def highResol_hover(self, mouse):
        if self.highResolPosition.left < mouse[0] < self.highResolPosition.right and self.highResolPosition.top < mouse[1] < self.highResolPosition.bottom and not self.highResolution:
            self.highResolText = self.main_font.render("1024 x 640", 1, Color.LIGHT_GRAY)
        else:
            self.highResolText = self.main_font.render("1024 x 640", 1, Color.WHITE)

    # просто отображалки
    def new_game_show(self):
        self.screen.blit(self.newGameText, self.newGamePosition)

    def settings_show(self):
        self.screen.blit(self.settingsText, self.settingsPosition)

    def lowResol_show(self):
        self.screen.blit(self.lowResolText, self.lowResolPosition)

    def highResol_show(self):
        self.screen.blit(self.highResolText, self.highResolPosition)

    def highscores_show(self):
        self.screen.blit(self.highscoresText, self.highscoresPosition)

    def exit_show(self):
        self.screen.blit(self.exitText, self.exitPosition)

    def go_back_show(self):
        self.screen.blit(self.goBackText, self.goBackPosition)

    def volume_show(self):
        self.screen.blit(self.volumeText, self.volumePosition)

    def resolution_show(self):
        self.screen.blit(self.resolutionText, self.resolutionPosition)

    def plus_show(self):
        self.screen.blit(self.plusText, self.plusPosition)

    def volume_num_show(self):
        self.screen.blit(self.volumeNumText, self.volumeNumPosition)

    def minus_show(self):
        self.screen.blit(self.minusText, self.minusPosition)

    def show(self):
        while not self.m_quit:
            self.screen.blit(self.background, self.background_rect)
            if self.mainIsActive: # если мы в главном меню
                self.main_events()
                self.new_game_show()
                self.settings_show()
                self.highscores_show()
                self.exit_show()

            elif self.settingsIsActive: # если мы в разделе настроек
                self.settings_events()
                self.volume_show()
                self.resolution_show()
                self.lowResol_show()
                self.highResol_show()
                self.plus_show()
                self.volume_num_show()
                self.minus_show()
                self.go_back_show()

            elif self.highscoresIsActive: # если мы в разделе рекордов
                self.highscores_events()
                self.highscore.process_event()
                self.highscore.process_draw(self.screen)
                self.go_back_show()
            pygame.display.flip()
            pygame.time.wait(5)
            pygame.display.update()