import pygame, sys
from bullet import Bullet
from ThePersons.inoplanet import Inoplanet
import time

def update(bg_color, screen, stats, sc, gun, bullets, inos):
    """Обновляет экран"""
    # Заливка
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.out_put()
    inos.draw(screen)
    # Концовка
    pygame.display.flip()

def get_events(gun, screen, bullets):
    """Обработка событий"""
    # Закрыть окно на крестик
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # QUIT - крестик
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # GUN - Right
            if event.key == pygame.K_d:
                gun.mright = True
            # GUN - Left
            elif event.key == pygame.K_a:
                gun.mleft = True

            # BULLET - Up
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # GUN - Right
            if event.key == pygame.K_d:
                gun.mright = False
            # GUN - Left
            elif event.key == pygame.K_a:
                gun.mleft = False

def update_bullets(screen, bullets, inos, stats, sc):
    """Обновляет позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # Подбробнее в скобках: (прог прочесывает группы пуль и пришельцев, True/True - при коллизии уничтожает обе группы,
    # если F/T - то не уничтожались бы только пули, след-но, T/F - не пропадут только пришельцы)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():
            # Сколько пришельцв было, на столько раз мы и увеличиваем на 10
            stats.score += 10 * len(inos)
        sc.get_image_score()
        check_hidh_score(stats, sc)
        sc.get_image_guns()
    # Сщздаем новые при выигрыше
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)

def create_army(screen, inos):
    """Создает армию пришельцев"""
    ino = Inoplanet(screen)
    ino_width = ino.rect.width
    ino_height = ino.rect.height
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    number_ino_y = int((600 - 200 - 2 * ino_height) / ino_height)
    # Столбик пришельцев
    for row_number in range(number_ino_y):
        # Строчка пришельцев
        for number_ino in range(number_ino_x):
            ino = Inoplanet(screen)
            ino.x = ino_width + (ino_width * number_ino)
            ino.y = ino_height + (ino_height * row_number)

            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino)

def gun_kill(stats, screen, sc, gun, inos, bullets):
    """Столькновение пушки и армии"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.get_image_guns()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_inps_posotion(stats, screen, gun, inos, bullets, sc):
    """Обновляет позицию прищельцев"""
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, sc, gun, inos, bullets)
    inos_check(stats, screen, gun, inos, bullets, sc)

def inos_check(stats, screen, gun, inos, bullets, sc):
    """Проверка добралась ли армия до края экрана"""
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom > screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, inos, bullets)
            break

def check_hidh_score(stats, sc):
    """Проверка новых рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.get_image_high_score()
        # Записываем рекорд
        with open('./high_score.txt', 'w') as file:
            file.write(str(stats.high_score))
