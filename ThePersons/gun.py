import pygame
from pygame.sprite import Sprite

class Gun(Sprite):
    def __init__(self, screen):
        """Инициализация пушки"""
        super(Gun, self).__init__()

        self.screen = screen
        self.image = pygame.image.load('Material/img/pixil-frame-0.png')

        # Подучаем картинку на прямоугольник, чтобы в дальнейшем управлять ею
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        self.mright = False
        self.mleft = False

    def out_put(self):
        """Отрисует пушку"""
        # В скобках: (что мы отрисовавыем?, как что?)
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """Обновляет позицию пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        elif self.mleft and self.rect.left > 0:
            self.center += -1.5

        self.rect.centerx = self.center

    def create_gun(self):
        """Размещает пушку заново"""
        self.center = self.screen_rect.centerx