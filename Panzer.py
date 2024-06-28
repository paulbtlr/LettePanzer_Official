import pygame

class Panzer:
    def __init__(self, image_path, start_position, scale_size=(50, 30)):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, scale_size)  # Skalieren des Bildes
        self.position = list(start_position)
        self.velocity = 5  # Geschwindigkeit des Panzers

    def draw(self, surface):
        surface.blit(self.image, self.position)

    def move_left(self):
        self.position[0] -= self.velocity

    def move_right(self):
        self.position[0] += self.velocity

    def update_position(self, ground_height):
        # Ensure the panzer stays on the ground
        self.position[1] = ground_height - self.image.get_height()

    def get_rect(self):
        return self.image.get_rect(topleft=self.position)
