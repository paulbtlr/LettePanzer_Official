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

    def vector_angle(self, panzer_rohr_angle,panzer_angle, flip):
        #Calculates the Position of the Weapon Spawnpoint
        LINE_LENGHT = 56
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

    def update_y(self,panzer_position):
        #Keeps the Starting Point of Rotation for the Weapon Spawner in Place
        self.rect2.y = panzer_position + 18

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 255), self.rect)
        pygame.draw.rect(surface, (255, 0, 0), self.rect2)
