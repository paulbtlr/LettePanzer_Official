import pygame
import math
import os

class Panzer:
    def __init__(self, image_path, start_position, scale_factor=0.5):
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, 
                                            (int(self.original_image.get_width() * scale_factor), 
                                             int(self.original_image.get_height() * scale_factor)))
        self.position = list(start_position)
        self.angle = 0
        self.speed = 1
        self.tank = 200 #The Maximum Movement a Tank can move
        self.health = 100

    def load_images(self, image_path):
        """
        Loads all images in directory. The directory must only contain images.

        Args:
            path: The relative or absolute path to the directory to load images from.

        Returns:
            List of images.
        """
        images = []
        for file_name in os.listdir(image_path):
            image = pygame.image.load(image_path + os.sep + file_name).convert()
            images.append(image)
        return images




    def draw(self, surface):
        img = pygame.transform.flip(self.image, True, False)
        rotated_image = pygame.transform.rotate(img, self.angle)
        new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=self.position).center)
        surface.blit(rotated_image, new_rect.topleft)


    def move(self):
        key = pygame.key.get_pressed()

        #Left Movement: Drives until Self.Tank == 0
        if (key[pygame.K_LEFT]) and (self.tank >= 0):
         self.position[0] -= self.speed
         self.tank -= self.speed

         if self.tank < 0:
             self.tank == 0

        #Right Movement: Drives until Self.Tank == 0
        if (key[pygame.K_RIGHT]) and (self.tank >= 0):
         self.position[0] += self.speed
         self.tank -= self.speed
         if self.tank < 0:
             self.tank == 0


    def update_position(self, ground_height):
        self.position[1] = ground_height - self.image.get_height() + 14

    def update_angle(self, ground_slope):
        self.angle = -math.degrees(math.atan(ground_slope))
