import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):
        """Создание пули"""
        super(Bullet, self).__init__()
        self.screen = screen
        # В скобках: (координата, координата, ширина, высота)
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 84, 135, 255
        self.speed = 3

        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Отрисоква пули"""
        # В скобках: (где?, каким цветом?, каким размером?)
        pygame.draw.rect(self.screen, self.color, self.rect)