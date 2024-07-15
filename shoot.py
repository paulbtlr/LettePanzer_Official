import pygame
import math
#from weapons import Weapons

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
          self.counter = 0
          self.shooting = False
          self.speed_hor = 0
          self.speed_ver = 5
          self.gravity = 1

    def vector_angle(self, panzer_rohr_angle,panzer_angle, flip):
        #Calculates the Position of the Weapon Spawnpoint
        LINE_LENGHT = 56
        if self.shooting == False:
            if flip == True:
                #Player 1
                self.rect.x = self.rect2.x + LINE_LENGHT*math.cos((panzer_rohr_angle - panzer_angle)*0.069 / 4)
                self.rect.y = self.rect2.y + LINE_LENGHT*math.sin((panzer_rohr_angle - panzer_angle)*0.069 / 4)

            else:
                #Player 2
                self.rect.x = self.rect2.x - LINE_LENGHT*math.cos((panzer_rohr_angle - panzer_angle)*0.069 / 4)
                self.rect.y = self.rect2.y - LINE_LENGHT*math.sin((panzer_rohr_angle - panzer_angle)*0.069 / 4)


    def move(self, tank, speed, flip):
        key = pygame.key.get_pressed()
        if flip == True:
            #Player 1
            #Left Movement: Drives until Self.Tank == 0
            if (key[pygame.K_a]) and (tank >= 0):
                self.rect.x -= speed
                self.rect2.x -= speed

            #Right Movement: Drives until Self.Tank == 0
            if (key[pygame.K_d]) and (tank >= 0):
                self.rect.x += speed
                self.rect2.x += speed
        else:
            #Player 2
            #Left Movement: Drives until Self.Tank == 0
            if (key[pygame.K_LEFT]) and (tank >= 0):
                self.rect.x -= speed
                self.rect2.x -= speed

            #Right Movement: Drives until Self.Tank == 0
            if (key[pygame.K_RIGHT]) and (tank >= 0):
                self.rect.x += speed
                self.rect2.x += speed

    def use_shooting(self, flip):
        key = pygame.key.get_pressed()
        if flip == True:
            self.speed_hor = 30
            if((key[pygame.K_e] == True) and (self.shooting == False)):
                #self.speed_hor = 30
                self.counter += 1
                print(self.counter)
                if self.counter == 5:
                    self.counter = 0
                    self.speed_ver += 5
                    print("UPGRADED: ",self.speed_ver)
                    
            if key[pygame.K_f] == True:
                self.shooting = True
        else:
            self.speed_hor = -30
            if((key[pygame.K_1] == True) and (self.shooting == False)):
                #self.speed_hor -= 30
                self.counter += 1
                print(self.counter)
                if self.counter == 5:
                    self.counter = 0
                    self.speed_ver += 5
                    print("UPGRADED: ",self.speed_ver)
                    
            if (key[pygame.K_2] == True):
                self.shooting = True


    def update_shoot(self,flip):
        if self.shooting == True:
            gravity = self.gravity
            self.rect.x += self.speed_hor
            self.rect.y -= self.speed_ver
            self.speed_ver -= gravity
        if self.rect.y >= SCREEN_HEIGHT or self.rect.x >= SCREEN_WIDTH:
            self.shooting = False
            self.counter = 0
            self.rect.x = self.x
            self.rect.y = self.y
            self.speed_ver = 5
            self.gravity = 1
            if flip == True:
                self.speed_hor = 30
            else:
                self.speed_hor = -30

    def update_y(self,panzer_position):
        #Keeps the Starting Point of Rotation for the Weapon Spawner in Place
        self.rect2.y = panzer_position + 18

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 255), self.rect)
        pygame.draw.rect(surface, (255, 0, 0), self.rect2)
