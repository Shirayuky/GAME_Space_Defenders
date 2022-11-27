import pygame.font
from ThePersons.gun import Gun
from pygame.sprite import Group


class Scores():
    """Вывд игровой информации"""

    def __init__(self, screen, stats):
        """Инициализируем подсчет очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        self.text_color = (84, 135, 255)
        # В скобках: (название_шрифта, размер)
        self.font = pygame.font.SysFont(None, 36)
        self.get_image_score()
        self.get_image_high_score()
        self.get_image_guns()

    def get_image_score(self):
        """Преобразовывает текст счета в графическое изображение"""
        # В скобках: (стр(превращаем перем с данными в строку), True - ок, рендерим, цвет текста, (фон текста))
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        # Размещение
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def get_image_high_score(self):
        """Выводит рекорд на экран как граф изображение"""
        self.high_score_img = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx

        self.high_score_rect.top = self.screen_rect.top + 20

    def get_image_guns(self):
        """Выводит кол_во жизней"""
        self.guns = Group()
        for gun_numb in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_numb * gun.rect.width
            gun.rect.y = 10
            self.guns.add(gun)

    def show_score(self):
        """Выводит счет на экран"""
        # В строке: селф.где_отрисовываем.метод(что_отрисовываем?, как_что?)
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        # В скобках: (Помещаем_где?)
        self.guns.draw(self.screen)
