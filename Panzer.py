import pygame
import math

class Panzer:
    def __init__(self, image_path, start_position, scale_factor=0.5):
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, 
                                            (int(self.original_image.get_width() * scale_factor), 
                                             int(self.original_image.get_height() * scale_factor)))
        self.position = list(start_position)
        self.angle = 0
        self.speed = 1

    def draw(self, surface):
        img = pygame.transform.flip(self.image, True, False)
        rotated_image = pygame.transform.rotate(img, self.angle)
        new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=self.position).center)
        surface.blit(rotated_image, new_rect.topleft)


    def move(self):
        key = pygame.key.get_pressed()

        #l
        if key[pygame.K_LEFT]:
         self.position[0] -= self.speed
        #r
        if key[pygame.K_RIGHT]:
         self.position[0] += self.speed

    def update_position(self, ground_height):
        self.position[1] = ground_height - self.image.get_height() + 16

    def update_angle(self, ground_slope):
        self.angle = -math.degrees(math.atan(ground_slope))
