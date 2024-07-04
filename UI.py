import pygame

font_path = "Assets\Schrift\Pixellari.ttf"  # Pfad zur heruntergeladenen Schriftart

class Button:
    def __init__(self, position, width, height):
        self.font = pygame.font.Font(font_path, 36)
        self.color = (100, 100, 100)
        self.highlight_color = (150, 150, 150)
        self.position = position
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        self.highlighted = False
        self.visible = True  # Neue Eigenschaft für die Sichtbarkeit

    def draw(self, surface):
        if self.visible:  # Nur zeichnen, wenn sichtbar
            if self.highlighted:
                pygame.draw.rect(surface, self.highlight_color, self.rect)
            else:
                pygame.draw.rect(surface, self.color, self.rect)
        
    def update(self, event):
        if self.visible:  # Nur bei sichtbaren Buttons Events bearbeiten
            if event.type == pygame.MOUSEMOTION:
                self.highlighted = self.rect.collidepoint(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    print(f"Button clicked!")

    def set_visible(self, visible):
        self.visible = visible

class UI:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        button_info = [
            {"position": (800, 880), "width": 300, "height": 50},
            {"position": (1150, 880), "width": 300, "height": 150},
            {"position": (1720, 880), "width": 160, "height": 150}  
        ]

        for info in button_info:
            button = Button(info["position"], info["width"], info["height"])
            self.buttons.append(button)

    def draw_health(self, health, x, y, surface, flip):
        ratio_m = health / 100
        if flip == False:
            pygame.draw.rect(surface, (0, 255, 0), (x, (y), 200 * ratio_m, 35 ))
        elif flip == True:
            pygame.draw.rect(surface, (0, 255, 0), (x + int(200 * (1-ratio_m)), y, int(200 * ratio_m), 35 ))

    def draw_tank(self, tank, x, y, surface, flip):
        ratio_m = tank / 100
        if flip == False:
            pygame.draw.rect(surface, (0, 255, 255), (x, (y), 100 * ratio_m, 35 ))
        elif flip == True:
            pygame.draw.rect(surface, (0, 255, 255), (x + int(100 * (1-ratio_m)), y, int(100 * ratio_m), 35 ))

    def update(self, event):
        for button in self.buttons:
            button.update(event)

    def draw(self):
        for button in self.buttons:
            button.draw(self.screen)

    def set_button_position(self, index, position):
        if 0 <= index < len(self.buttons):
            self.buttons[index].position = position
            self.buttons[index].rect = pygame.Rect(self.buttons[index].position[0], self.buttons[index].position[1],
                                                   self.buttons[index].width, self.buttons[index].height)

    def set_button_visible(self, index, visible):
        if 0 <= index < len(self.buttons):
            self.buttons[index].set_visible(visible)