import pygame
import math

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1020

#shootitooti
class Shoot() :
    def __init__(self,x,y,start_x, start_y) :
          self.x = x
          self.y = y
          self.start_x = start_x
          self.start_y = start_y
          self.rect = pygame.Rect(self.x,self.y,5,5)
          self.rect2 = pygame.Rect(self.start_x,self.start_y,5,5)
          #self.rect.x= x
          #self.rect.y= y
          #self.rect2.x= start_x
          #self.rect2.y= start_y
          self.speed_hor = 30
          self.speed_ver = 5
          self.gravity = 1
          self.shooting = False
          self.counter = 0

    def vector_angle(self, panzer_rohr_angle,panzer_angle):
        LINE_LENGHT = 56
        #vec = self.rohr_vector
        #vec.move_towards(self.start_x,self.start_y)
        #rotated_vec = vec.rotate(panzer_angle)
        #pygame.draw.line(screen, (255,0,0),(self.start_x,self.start_y),(self.x,self.y))
        self.rect.x = self.rect2.x + LINE_LENGHT*math.cos((panzer_rohr_angle - panzer_angle)*0.069 / 4)
        self.rect.y = self.rect2.y + LINE_LENGHT*math.sin((panzer_rohr_angle - panzer_angle)*0.069 / 4)

    def move(self, tank, speed):
        key = pygame.key.get_pressed()
        #if key[pygame.K_w] == True:
        #    self.rect.x -= 0.9
        #    self.rect.y -= 0.9

        #Player 1
        #Left Movement: Drives until Self.Tank == 0
        if (key[pygame.K_a]) and (tank >= 0):
            self.rect.x -= speed
            self.rect2.x -= speed

        #Right Movement: Drives until Self.Tank == 0
        if (key[pygame.K_d]) and (tank >= 0):
            self.rect.x += speed
            self.rect2.x += speed

        # #Player 2
        # elif self.flip == False:
        #     #Left Movement: Drives until Self.Tank == 0
        #     if (key[pygame.K_LEFT]) and (self.tank >= 0):
        #         self.position[0] -= self.speed
        #         self.tank -= self.speed
        #         self.move_left = True
        #         self.move_right = False

        #         if self.tank < 0:
        #             self.tank == 0

        #     #Right Movement: Drives until Self.Tank == 0
        #     if (key[pygame.K_RIGHT]) and (self.tank >= 0):
        #         self.position[0] += self.speed
        #         self.tank -= self.speed
        #         self.move_left = False
        #         self.move_right = True

        #         if self.tank < 0:
        #             self.tank == 0



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

    def update_y(self,panzer_position):
        #keeps the tank in place......
        #self.rect2.y = ground_height - panzer_position - 19
        self.rect2.y = panzer_position + 18
        #print(ground_height)
        #x = Offset Panzer + Rohr * cos(Winkel Panzer + Winkel Rohr)
        #y = Offset Panzer + Rohr * sin(Winkel Panzer + Winkel Rohr)
        #print(ground_height,self.rect2.y)

    def draw(self, surface):
        #if self.shooting == True:
        #print(self.rect2.y)
        pygame.draw.rect(surface, (255, 0, 255), self.rect)
        pygame.draw.rect(surface, (255, 0, 0), self.rect2)
