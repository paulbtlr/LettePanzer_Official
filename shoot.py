import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#shootitooti
class Shoot() :
    def __init__(self,x,y) :
          self.x = x
          self.y = y
          self.rect = pygame.Rect(self.x,self.y,20,20)
          self.rect.x=115
          self.rect.y=267
          self.speed_hor = 10
          self.speed_ver = 0
          self.gravity = 1
          self.shooting = False
          self.counter = 0

    def move(self):
        key = pygame.key.get_pressed()
        key_up = pygame.KEYUP
        SPEED = 5
        dx = 0
        dy = self.rect.y

        dx = SPEED
        dy = SPEED / 2

        if((key[pygame.K_UP] == True) and (self.shooting == False)):
          self.counter += 1
          print(self.counter)
          if self.counter == 25:
              self.counter = 0
              self.speed_ver += 1
              print("UPGRADED: ",self.speed_ver)

        if(key[pygame.K_DOWN] == True):
            self.shooting = True

        #if(key_up[pygame.K_UP] == True):
        #    self.shooting = True

        #self.rect.x += dx
        #self.rect.y += dy

    def update_patty(self):
        if self.shooting == True:
            gravity = self.gravity
            self.rect.x += self.speed_hor
            self.rect.y -= self.speed_ver
            self.speed_ver -= gravity
        if self.rect.y >= SCREEN_HEIGHT:
            self.shooting = False
            self.counter = 0
            self.rect.x = 115
            self.rect.y = 267
            self.speed_hor = 10
            self.speed_ver = 0
            self.gravity = 1


    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 255), self.rect)