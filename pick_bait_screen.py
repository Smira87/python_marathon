import pygame

pygame.init()

HEIGHT = 600
WIDTH = 800
FPS = pygame.time.Clock()
main_display = pygame.display.set_mode((WIDTH, HEIGHT))
playing = True



bg = pygame.transform.scale(pygame.image.load('materials/background.png'), (WIDTH, HEIGHT))

COLOR_GREEN = (0, 255, 0)

hook = pygame.image.load("materials/hooc.png")
hook_rect = hook.get_rect()
hook_rect.x = WIDTH/2 - 2*hook.get_width()
hooked = False

bait_1 = pygame.image.load("materials/worm.png")
bait_2 = pygame.image.load("materials/puffi.png")

bait_1_rect = bait_1.get_rect()
bait_1_rect.x = WIDTH/2 - bait_1.get_width()
bait_1_rect.y = HEIGHT - bait_1.get_height()


bait_2_rect = bait_2.get_rect()
bait_2_rect.x = WIDTH/2
bait_2_rect.y = HEIGHT - bait_2.get_height()

baits = [bait_1_rect, bait_2_rect]

active_box = None

while playing:
    FPS.tick(120)


    for event in pygame.event.get():
        if event.type == pygame.constants.QUIT:
            playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, bait in enumerate(baits):
                    if bait.collidepoint(event.pos):
                        active_box = num
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                baits[active_box].x = hook_rect.x + 20
                baits[active_box].y = hook_rect.y + 130
                active_box = None


        if event.type == pygame.MOUSEMOTION:
            if active_box != None:
                baits[active_box].move_ip(event.rel)
                if baits[active_box].colliderect(hook_rect):
                    hooked = True
                else:
                    hooked = False
            print(hooked)


    main_display.blit(bg, (0, 0))
    main_display.blit(hook, hook_rect)

    main_display.blit(bait_1, bait_1_rect)
    main_display.blit(bait_2, bait_2_rect)

    pygame.display.flip()