import random

import pygame
from pygame import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT

pygame.init()

FPS = pygame.time.Clock()
HEIGHT = 600
WIDTH = 800
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)


playing = True
player_size = (20, 20)
main_display = pygame.display.set_mode((WIDTH, HEIGHT))
player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
player_move_down = [0, 1]
player_move_up = [0, -1]
player_move_right = [1, 0]
player_move_left = [-1, 0]

while playing:
    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

    main_display.fill(COLOR_BLACK)

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)

    elif keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)

    elif keys[K_RIGHT] and player_rect.right > 0:
        player_rect = player_rect.move(player_move_right)

    elif keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)

    main_display.blit(player, player_rect)



    pygame.display.flip()
