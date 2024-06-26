import pygame

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Lette Panzer")

running = True
while running:

    for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == QUIT:
                running = False


    pygame.display.flip()