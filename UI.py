import pygame

class Button:
    def __init__(self, text, position):
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.color = (100, 100, 100)
        self.highlight_color = (150, 150, 150)
        self.position = position
        self.rect = pygame.Rect(self.position[0], self.position[1], 300, 50)
        self.highlighted = False

    def draw(self, surface):
        if self.highlighted:
            pygame.draw.rect(surface, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)
        
        text_render = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_render.get_rect(center=self.rect.center)
        surface.blit(text_render, text_rect)

    def update(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.highlighted = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                print(f"Button '{self.text}' clicked!")

class Button1:
    def __init__(self, text, position):
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.color = (100, 100, 100)
        self.highlight_color = (150, 150, 150)
        self.position = position
        self.rect = pygame.Rect(self.position[0], self.position[1], 200, 50)
        self.highlighted = False

    def draw(self, surface):
        if self.highlighted:
            pygame.draw.rect(surface, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)
        
        text_render = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_render.get_rect(center=self.rect.center)
        surface.blit(text_render, text_rect)

    def update(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.highlighted = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                print(f"Button '{self.text}' clicked!")

class UI:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        button_positions = [
            (800, 900),
            #(1000, 970),
            #(1750, 970),
        ]
        button_texts = ["WEAPONS", "FIRE", "LEAVE GAME", ]

        for i in range(len(button_positions)):
            button = Button(button_texts[i], button_positions[i])
            self.buttons.append(button)

    def update(self, event):
        for button in self.buttons:
            button.update(event)

    def draw(self):
        for button in self.buttons:
            button.draw(self.screen)
