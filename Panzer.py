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
        self.speed = 5

    def draw(self, surface):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=self.position).center)
        surface.blit(rotated_image, new_rect.topleft)

    def move_left(self):
        self.position[0] -= self.speed

    def move_right(self):
        self.position[0] += self.speed

    def update_position(self, ground_height):
        self.position[1] = ground_height - self.image.get_height() / 2

    def update_angle(self, ground_slope):
        self.angle = -math.degrees(math.atan(ground_slope))
