import pygame

font_path = "Assets\Schrift\Pixellari.ttf"  # Pfad zur heruntergeladenen Schriftart

class Button:
    def __init__(self, text, position, width, height):
        self.text = text
        self.font = pygame.font.Font(font_path, 36)
        self.color = (100, 100, 100)
        self.highlight_color = (150, 150, 150)
        self.position = position
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        self.highlighted = False

    def draw(self, surface):
        if self.highlighted:
            pygame.draw.rect(surface, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)
        
        # Split text into lines if \n is present
        lines = self.text.split('\n')

        # Render each line of text
        for i, line in enumerate(lines):
            text_render = self.font.render(line, True, (255, 255, 255))
            text_rect = text_render.get_rect()
            text_rect.centerx = self.rect.centerx
            text_rect.y = self.rect.centery + (i * self.font.get_height())  # Vertical offset for multiple lines
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
        button_info = [
            {"text": "WEAPONS", "position": (800, 880), "width": 300, "height": 50},
            {"text": "FIRE", "position": (1150, 880), "width": 300, "height": 150},
            {"text": "LEAVE\nGAME", "position": (1740, 880), "width": 180, "height": 150}  # Updated text here
        ]

        for info in button_info:
            button = Button(info["text"], info["position"], info["width"], info["height"])
            self.buttons.append(button)

    def update(self, event):
        for button in self.buttons:
            button.update(event)

    def draw(self):
        for button in self.buttons:
            button.draw(self.screen)

    def set_button_text(self, index, text):
        if 0 <= index < len(self.buttons):
            self.buttons[index].text = text

    def set_button_position(self, index, position):
        if 0 <= index < len(self.buttons):
            self.buttons[index].position = position
            self.buttons[index].rect = pygame.Rect(self.buttons[index].position[0], self.buttons[index].position[1],
                                                   self.buttons[index].width, self.buttons[index].height)
