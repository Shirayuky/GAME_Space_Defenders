import pygame

class Inoplanet(pygame.sprite.Sprite):
    """Инопланетянин"""
    def __init__(self, screen):
        """Инициализирует и задает начальную позицию"""
        super(Inoplanet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Material/img/Inoplanetyanin.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Отрисует пришельца"""
        # В скобках: (что мы отрисовавыем?, как что?)
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Перемещает пришельцев"""
        self.y += 0.1
        self.rect.y = self.y