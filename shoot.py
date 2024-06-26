import pygame

class Shoot() :
    def __init__(self,x,y) :
          self.x = x
          self.y = y
          self.rect = pygame.Rect(self.x,self.y,20,20)
          self.rect.x=115
          self.rect.y=267
          self.speed_hor = 10
          self.speed_ver = 10
          self.gravity = 1

    def move(self):
        SPEED = 5

        dx = 0
        dy = 0

        dx = SPEED
        dy = SPEED / 2

        #self.rect.x += dx
        #self.rect.y += dy

    def update_patty(self):
        gravity = self.gravity
        self.rect.x += self.speed_hor
        self.rect.y -= self.speed_ver
        self.speed_ver -= gravity
        
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 255), self.rect)