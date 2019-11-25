import  pygame
import sys
from src.constants import Color
from highscores import Highscore

class Menu:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode([1024, 640])
        self.menuIsActive = True  # аналог game_over, для закрытия меню
        # далее - переменные, отвечающие за окна (пункты меню)
        # текущим окнам присваивается True
        self.mainIsActive = True
        self.settingsIsActive = False
        self.highscoresIsActive = False

        self.highscore = Highscore()

        self.main_font = pygame.font.Font('font/RetroGaming.ttf', 46)
        self.newGameText = self.main_font.render("Новая игра", 1, Color.WHITE)
        self.settingsText = self.main_font.render("Настройки", 1, Color.WHITE) # инициализация надписей
        self.highscoresText = self.main_font.render("Рекорды", 1, Color.WHITE)
        self.exitText = self.main_font.render("Выход", 1, Color.WHITE)

        self.newGamePosition = self.newGameText.get_rect(center=[512, 200])
        self.settingsPosition = self.settingsText.get_rect(center=[512, 270])    # инициализация позиций надписей
        self.highscoresPosition = self.highscoresText.get_rect(center=[512, 340])
        self.exitPosition = self.exitText.get_rect(center=[512, 410])

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
                if 351 < mouse[0] < 673 and 180 < mouse[1] < 231:
                    self.new_game_click()
                elif 361 < mouse[0] < 665 and 250 < mouse[1] < 301:
                    self.settings_click()
                elif 388 < mouse[0] < 638 and 321 < mouse[1] < 371:
                    self.highscores_click()
                elif 421 < mouse[0] < 605 and 391 < mouse[1] < 435:
                    self.exit_click()


    # обработка событий раздела настроек
    def settings_events(self):
        mouse = pygame.mouse.get_pos()
        self.go_back_hover(mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.menuIsActive = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 425 < mouse[0] < 601 and 491 < mouse[1] < 536:
                    self.go_back_click()

    # обработка событий раздела рекордов
    def highscores_events(self):
        mouse = pygame.mouse.get_pos()
        self.go_back_hover(mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.menuIsActive = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 425 < mouse[0] < 601 and 491 < mouse[1] < 536:
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

    def exit_click(self):
        self.menuIsActive = False
        sys.exit(0)

    def go_back_click(self):
        self.settingsIsActive = False
        self.highscoresIsActive = False
        self.mainIsActive = True

    # изменение цвета кнопок при наведении на них
    def new_game_hover(self, mouse):
        if 351 < mouse[0] < 673 and 180 < mouse[1] < 231:
            self.newGameText = self.main_font.render("Новая игра", 1, Color.LIGHT_GRAY)
        else:
            self.newGameText = self.main_font.render("Новая игра", 1, Color.WHITE)

    def settings_hover(self, mouse):
        if 361 < mouse[0] < 665 and 250 < mouse[1] < 301:
            self.settingsText = self.main_font.render("Настройки", 1, Color.LIGHT_GRAY)
        else:
            self.settingsText = self.main_font.render("Настройки", 1, Color.WHITE)

    def highscores_hover(self, mouse):
        if 388 < mouse[0] < 638 and 321 < mouse[1] < 371:
            self.highscoresText = self.main_font.render("Рекорды", 1, Color.LIGHT_GRAY)
        else:
            self.highscoresText = self.main_font.render("Рекорды", 1, Color.WHITE)

    def exit_hover(self, mouse):
        if 421 < mouse[0] < 605 and 391 < mouse[1] < 435:
            self.exitText = self.main_font.render("Выход", 1, Color.LIGHT_GRAY)
        else:
            self.exitText = self.main_font.render("Выход", 1, Color.WHITE)

    def go_back_hover(self, mouse):
        if 425 < mouse[0] < 601 and 491 < mouse[1] < 536:
            self.goBackText = self.main_font.render("Назад", 1, Color.LIGHT_GRAY)
        else:
            self.goBackText = self.main_font.render("Назад", 1, Color.WHITE)

    # просто отображалки
    def new_game_show(self):
        self.screen.blit(self.newGameText, self.newGamePosition)

    def settings_show(self):
        self.screen.blit(self.settingsText, self.settingsPosition)

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
                self.highscore.process_draw(self.screen)
                self.go_back_show()

            pygame.display.flip()
            pygame.time.wait(5)
            pygame.display.update()

def main():
    obj = Menu()
    obj.show()
if __name__ == '__main__':
    main()