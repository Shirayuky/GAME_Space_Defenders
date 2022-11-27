import pygame, controls
from ThePersons.gun import Gun
from pygame.sprite import Group
from Statistic.stats import Stats
from Statistic.scores import Scores


# 1. Создаем пустое окно

def run():
    """Вывод окна"""
    # Инициализируем игру
    pygame.init()
    screen = pygame.display.set_mode((700, 600))
    pygame.display.set_caption("Космические защитники")

    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    # Цикл обрабатывает события
    while True:
        controls.get_events(gun, screen, bullets)
        # Пушка и пульки
        if stats.run_game:
            controls.update(bg_color, screen, stats, sc, gun, bullets, inos)
            controls.update_bullets(screen, bullets, inos, stats, sc)
            controls.update_inps_posotion(stats, screen, gun, inos, bullets, sc)

            # Move
            gun.update_gun()


run()