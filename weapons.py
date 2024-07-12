import pygame

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1020

#shootitooti
class Weapons() :
    def __init__(self,sprites) :
          self.sprites = pygame.image.load(sprites)
          self.speed_hor = 30
          self.speed_ver = 5
          self.gravity = 1
          self.shooting = False
          self.counter = 0

    def update_shoot(self):
        if self.shooting == True:
            gravity = self.gravity
            self.rect.x += self.speed_hor
            self.rect.y -= self.speed_ver
            self.speed_ver -= gravity
        if self.rect.y >= SCREEN_HEIGHT:
            self.shooting = False
            self.counter = 0
            self.rect.x = self.x
            self.rect.y = self.y
            self.speed_hor = 30
            self.speed_ver = 5
            self.gravity = 1

