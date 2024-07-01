import pygame

class Panzer:
    def __init__(self, image_path, start_position, scale_size=(100, 60)):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, scale_size)  # Skalieren des Bildes
        self.position = list(start_position)
        self.velocity = 5  # Geschwindigkeit des Panzers

    def draw(self, surface):
        img = pygame.transform.flip(self.image, True, False)
        surface.blit(img, self.position)
        print(self.position[0])
        print(self.position[1])

    def move_left(self):
        self.position[0] -= self.velocity

    def move_right(self):
        self.position[0] += self.velocity

    def update_position(self, ground_height):
        # Ensure the panzer stays on the ground
        self.position[1] = ground_height - self.image.get_height() + 14  # Adjusted to keep panzer on the ground

    def get_rect(self):
        return self.image.get_rect(topleft=self.position)
