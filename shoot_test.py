import pygame
import math
import sys
from shoot import Shoot

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    K_s,
    QUIT
)

#initialise pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Lette Panzer")

clock = pygame.time.Clock()
FPS = 60


pxarray = pygame.PixelArray(screen)

color = 255, 0, 0
first = True
prev_x, prev_y = 0, 0

#def angle(A, B, aspectRatio):
#    x = B[0] - A[0]
#   y = B[1] - A[1]
#   angle = math.atan2(-y, x / aspectRatio)
#   return angle

#a1 = angle((75, 300),(250, 175), 500/350)
#a2 = angle((400, 315),(250, 175), 500/350)
x = 10
y = 100
shoot = Shoot(x, y)

running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == QUIT:
                running = False
    
    screen.fill((0,0,0))
    
    #for y, py in enumerate(pxarray):
    #    for x, px in enumerate(py):
    #        if int(x) == (int(y)*int(y)) - 30*int(y) + 450:
    #            pxarray[y][x] = 0xFFFFFF

    #            if first:
    #                first = False
    #                prev_x, prev_y = x, y
    #                continue
                
    #            pygame.draw.line(screen, color, (prev_y, prev_x), (y, x))
    #            prev_x, prev_y = x, y
    shoot.move()
    shoot.update_shoot()
    shoot.draw(screen)

    pygame.draw.line(screen, (0, 255, 0),[0, 600],[SCREEN_WIDTH, 600], 10)
    #pygame.draw.polygon(screen, (0,0,255), [[300, 300], [100, 400],[170, 300]], 5)
    #pygame.draw.arc(screen, (255,0,255), (0, 0, 800, 600), a1, a2, 5)

    first = True

    pygame.display.flip()