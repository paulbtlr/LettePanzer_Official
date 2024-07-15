import pygame
# import spritesheet

# SCREEN_WIDTH = 1920
# SCREEN_HEIGHT = 1020

# #shootitooti
class Weapons() :
     def __init__(self,sprite_sheet, animation_steps) :
           self.speed_hor = 30
           self.speed_ver = 5
           self.gravity = 1
           self.shooting = False
           self.rect = pygame.Rect(0,0, 640, 640)
           self.hitbox = 0
           self.size = 640
           self.counter = 0
           self.sprite = sprite_sheet
           self.animation_steps = animation_steps
           self.animation_list = []
           self.animation_cooldown = 50
           self.frame = 0
           self.action = 0
           self.type = 0 #0 = Basic Projectile, 1 = Milbradt Fass 640x640 x 24, 2 = Lightning Ball 640x640 x 8
           self.last_update = pygame.time.get_ticks()

     def load_animation(self):
         for x in range(self.animation_steps):
             self.animation_list.append(self.sprite.get_image(x, 640, 640, 0.09 / 4, (0,0,0)))

     def update_weapon(self):
         current_time = pygame.time.get_ticks()
         if current_time - self.last_update >= self.animation_cooldown:
             self.frame += 1
             self.last_update = current_time
             if self.frame >= len(self.animation_list)-1:
                 self.frame = 0
      


     def collide(self,panzer_x,panzer_y, panzer_width, panzer_height, panzer_health):
         self.hitbox = self.animation_list[self.frame].get_rect()
         if self.hitbox.colliderect(panzer_x, panzer_y, panzer_width, panzer_height):
             panzer_health -= 50
             print("HIT")
             
     def draw_weapon(self,screen,x,y):
         screen.blit(self.animation_list[self.frame], (x,y))