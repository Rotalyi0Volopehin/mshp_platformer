import pygame
from src.constants import Color

class Menu:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.width = 1024
        self.height = 640
        self.screen = pygame.display.set_mode([self.width,self.height])
        self.menuIsActive = True  # аналог game_over, для закрытия меню
        # далее - переменные, отвечающие за окна (пункты меню)
        # текущим окнам присваивается True
        self.mainIsActive = True
        self.settingsIsActive = False
        self.highscoresIsActive = False
        self.highResolution = True
        self.kx = 1
        self.ky = 1

        self.main_font = pygame.font.Font('font/RetroGaming.ttf', 46)
        self.newGameText = self.main_font.render("Новая игра", 1, Color.WHITE)
        self.settingsText = self.main_font.render("Настройки", 1, Color.WHITE) # инициализация надписей
        self.highscoresText = self.main_font.render("Рекорды", 1, Color.WHITE)
        self.exitText = self.main_font.render("Выход", 1, Color.WHITE)

        self.lowResolText = self.main_font.render("800 x 600", 1, Color.WHITE)
        self.highResolText = self.main_font.render("1024 x 640", 1, Color.WHITE)

        self.newGamePosition = self.newGameText.get_rect(center=[512, 200])
        self.settingsPosition = self.settingsText.get_rect(center=[512, 270])    # инициализация позиций надписей
        self.highscoresPosition = self.highscoresText.get_rect(center=[512, 340])
        self.exitPosition = self.exitText.get_rect(center=[512, 410])

        self.lowResolPosition = self.settingsText.get_rect(center=[535, 360])
        self.highResolPosition = self.highscoresText.get_rect(center=[495, 440])

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
        self.lowResol_show()
        self.highResol_show()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.menuIsActive = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.goBackPosition.left < mouse[0] < self.goBackPosition.right and self.goBackPosition.top < mouse[1] < self.goBackPosition.bottom:
                    self.go_back_click()
                if self.highResolPosition.left < mouse[0] < self.highResolPosition.right and self.highResolPosition.top < mouse[1] < self.highResolPosition.bottom:
                    self.highResol_click()
                if self.lowResolPosition.left < mouse[0] < self.lowResolPosition.right and self.lowResolPosition.top < mouse[1] < self.lowResolPosition.bottom:
                    self.lowResol_click()

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

    # обработка нажатий на кнопки
    def new_game_click(self):
        self.menuIsActive = False
        # начало игры

    def settings_click(self):
        self.mainIsActive = False
        self.settingsIsActive = True

    def highscores_click(self):
        self.mainIsActive = False
        self.highscoresIsActive = True

    def lowResol_click(self):
        if self.highResolution:
            self.kx = 0.6734
            self.ky = 0.9375
            self.width = 800
            self.height = 600
            self.screen = pygame.display.set_mode([self.width, self.height])
            self.resolution_change()
            self.highResolution = False

    def highResol_click(self):
        if not self.highResolution:
            self.kx = 1.485
            self.ky = 1.066666
            self.width = 1024
            self.height = 640
            self.screen = pygame.display.set_mode([self.width, self.height])
            self.resolution_change()
            self.highResolution = True


    def exit_click(self):
        self.menuIsActive = False

    def go_back_click(self):
        self.settingsIsActive = False
        self.highscoresIsActive = False
        self.mainIsActive = True

    def resolution_change(self):
        self.newGamePosition.x *= self.kx
        self.newGamePosition.y *= self.ky
        self.settingsPosition.x *= self.kx
        self.settingsPosition.y *= self.ky
        self.highscoresPosition.x *= self.kx
        self.highscoresPosition.y *= self.ky
        self.exitPosition.x *= self.kx
        self.exitPosition.y *= self.ky
        self.goBackPosition.x *= self.kx
        self.goBackPosition.y *= self.ky
        self.lowResolPosition.x *= self.kx
        self.lowResolPosition.y *= self.ky
        self.highResolPosition.x *= self.kx
        self.highResolPosition.y *= self.ky

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

    def show(self):
        while self.menuIsActive:
            self.screen.blit(self.background, self.background_rect)

            if self.mainIsActive: # если мы в главном меню
                self.main_events()
                self.new_game_show()
                self.settings_show()
                self.highscores_show()
                self.exit_show()

            elif self.settingsIsActive: # если мы в разделе настроек
                self.settings_events()
                self.go_back_show()

            elif self.highscoresIsActive: # если мы в разделе рекордов
                self.highscores_events()
                self.go_back_show()

            pygame.display.flip()
            pygame.time.wait(5)
            pygame.display.update()

def main():
    obj = Menu()
    obj.show()
if __name__ == '__main__':
    main()