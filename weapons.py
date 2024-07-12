import pygame

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1020

#shootitooti
class Weapons() :
    def __init__(self,image,sprite_sheet1,sprite_sheet2, animation_steps) :
          self.speed_hor = 30
          self.speed_ver = 5
          self.gravity = 1
          self.shooting = False
          self.rect = pygame.Rect(500,500, 640, 640)
          self.counter = 0
          self.img = pygame.image.load(image)
          self.animation_list1 = self.load_weapon(sprite_sheet1, animation_steps)
          self.type = 0 #0 = Basic Projectile, 1 = Milbradt Fass 640x640 x 24, 2 = Lightning Ball 640x640 x 8

    def load_weapon(self,sprites,steps):
         self.sprites = "Deine MUm"
         #extract images from spritesheet
         animation_list1 = []
         for y, animation in enumerate(steps):
             temp_img_list = []
             for x in range(animation):
                 temp_img = sprites.subsurface(x * self.size, y * self.size, self.size, self.size)
                 temp_img_list.append(temp_img)
             animation_list1.append(temp_img_list)
         return animation_list1

    def draw_weapon(self,screen):
        #screen.blit(self.img,(100,100))
        screen.blit(self.image, (self.rect.x + (0), self.rect.y))