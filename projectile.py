import pygame


SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1020

#shootitooti
class Projectile() :
    def __init__(self,x,y,start_x, start_y) :
          self.x = x
          self.y = y
          self.start_x = start_x
          self.start_y = start_y
          self.rect = pygame.Rect(self.x,self.y,5,5)
          self.rect2 = pygame.Rect(self.start_x,self.start_y,5,5)
          self.speed_hor = 30
          self.speed_ver = 5
          self.gravity = 1
          self.shooting = False
          self.counter = 0

    def use_shooting(self):
        key = pygame.key.get_pressed()
        if((key[pygame.K_e] == True) and (self.shooting == False)):
          self.counter += 1
          print(self.counter)
          if self.counter == 5:
              self.counter = 0
              self.speed_ver += 5
              print("UPGRADED: ",self.speed_ver)
            
        if(key[pygame.K_f] == True):
            self.shooting = True

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


