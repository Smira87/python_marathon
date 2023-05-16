import pygame

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
x_speed = 1
y_speed = 1
player_speed = [x_speed, y_speed]

while playing:
    FPS.tick(240)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    main_display.fill(COLOR_BLACK)

    if player_rect.bottom >= HEIGHT:
        player_speed = [x_speed, -y_speed]

    if player_rect.top <= 0:
            player_speed = [-x_speed, y_speed]

    if player_rect.right >= WIDTH:
        player_speed = [-x_speed, -y_speed]

    if player_rect.left <= 0:
        player_speed = [x_speed, y_speed]

    print(player_speed)

    main_display.blit(player, player_rect)

    player_rect = player_rect.move(player_speed)

    pygame.display.flip()
