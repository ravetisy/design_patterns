import pygame
from time import sleep

# pygame.init()
# screen = pygame.display.set_mode(size=(800, 600))
# pygame.draw.rect(screen, (255, 0, 34), pygame.Rect(42, 15, 40, 32))
# sleep(10)
# pygame.display.flip()
# sleep(10)

# simple game loop example which waits for some user input until quit
import pygame
screen_width = 800
screen_height = 600
x = 100
y = 100
screen = pygame.display.set_mode(size=(screen_width, screen_height))
player_quits = False
while not player_quits:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player_quits = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            y -= 4
            if y < 0:
                y =0
        if pressed[pygame.K_DOWN]:
            y += 4
            if y > 580:
                y = 580
        if pressed[pygame.K_LEFT]:
            x -= 4
            if x < 0:
                x = 0
        if pressed[pygame.K_RIGHT]:
            x += 4
            if x > 780:
                x = 780
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(x, y, 20, 20))
    pygame.display.flip()
