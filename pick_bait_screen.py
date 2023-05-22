import pygame

pygame.init()

HEIGHT = 600
WIDTH = 800
FPS = pygame.time.Clock()
main_display = pygame.display.set_mode((WIDTH, HEIGHT))
playing = True

bg = pygame.transform.scale(pygame.image.load('materials/background.png'), (WIDTH, HEIGHT))

COLOR_GREEN = (0, 255, 0)

hooc = pygame.image.load("materials/hooc.png")
hooc_rect = hooc.get_rect()
hooc_rect.x = WIDTH/2 - 2*hooc.get_width()

while playing:
    FPS.tick(120)
    main_display.fill(COLOR_GREEN)

    for event in pygame.event.get():
        if event.type == pygame.constants.QUIT:
            playing = False

    main_display.blit(bg, (0, 0))
    main_display.blit(hooc, hooc_rect)

    pygame.display.flip()