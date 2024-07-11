import pygame

class Button:
    def __init__(self, x, y, off_image, on_image):
        self.x = x
        self.y = y
        self.off_image = off_image
        self.on_image = on_image
        self.image = off_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_hovered = False

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.image = self.on_image
            self.is_hovered = True
        else:
            self.image = self.off_image
            self.is_hovered = False

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
