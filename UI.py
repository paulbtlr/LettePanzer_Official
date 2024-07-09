import pygame

# Pfad zur heruntergeladenen Schriftart
font_path = "Assets\Schrift\Pixellari.ttf"

class Button:
    def __init__(self, position, width, height):
        """
        Initialisierungsmethode für die Klasse Button.
        Parameter:
        position (tuple): Die (x, y) Position des Buttons.
        width (int): Die Breite des Buttons.
        height (int): Die Höhe des Buttons.
        """
        self.font = pygame.font.Font(font_path, 36)  # Schriftart und -größe für den Buttontext
        self.color = (100, 100, 100)  # Standardfarbe des Buttons
        self.highlight_color = (150, 150, 150)  # Farbe des Buttons, wenn er hervorgehoben ist
        self.position = position  # Position des Buttons
        self.width = width  # Breite des Buttons
        self.height = height  # Höhe des Buttons
        # Rechteck für den Button basierend auf Position, Breite und Höhe
        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        self.highlighted = False  # Initialisiert den Zustand des Hervorhebens
        self.visible = True  # Neue Eigenschaft für die Sichtbarkeit des Buttons

    def draw(self, surface):
        """
        Zeichnet den Button auf der angegebenen Oberfläche.
        Parameter:
        surface (pygame.Surface): Die Oberfläche, auf der der Button gezeichnet wird.
        """
        if self.visible:  # Nur zeichnen, wenn der Button sichtbar ist
            if self.highlighted:
                pygame.draw.rect(surface, self.highlight_color, self.rect)  # Zeichne hervorgehobenen Button
            else:
                pygame.draw.rect(surface, self.color, self.rect)  # Zeichne normalen Button
        
    def update(self, event):
        """
        Aktualisiert den Zustand des Buttons basierend auf Ereignissen.
        Parameter:
        event (pygame.event.Event): Das Ereignis, das verarbeitet wird.
        """
        if self.visible:  # Nur bei sichtbaren Buttons Events bearbeiten
            if event.type == pygame.MOUSEMOTION:
                # Überprüfen, ob die Maus über dem Button ist, um Hervorhebung zu steuern
                self.highlighted = self.rect.collidepoint(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Überprüfen, ob auf den Button geklickt wurde
                if self.rect.collidepoint(event.pos):
                    print(f"Button clicked!")

    def set_visible(self, visible):
        """
        Setzt die Sichtbarkeit des Buttons.
        Parameter:
        visible (bool): Die Sichtbarkeit des Buttons.
        """
        self.visible = visible

class UI:
    def __init__(self, screen):
        """
        Initialisierungsmethode für die Klasse UI.
        Parameter:
        screen (pygame.Surface): Die Oberfläche, auf der das UI gezeichnet wird.
        """
        self.screen = screen
        self.buttons = []  # Liste zur Speicherung der Buttons
        self.create_buttons()  # Erstellen der Buttons

    def create_buttons(self):
        """
        Erstellt die Buttons und fügt sie zur Liste hinzu.
        """
        button_info = [
            {"position": (800, 880), "width": 300, "height": 50},
            {"position": (1150, 880), "width": 300, "height": 150},
            {"position": (1720, 880), "width": 160, "height": 150}  
        ]

        for info in button_info:
            button = Button(info["position"], info["width"], info["height"])
            self.buttons.append(button)  # Hinzufügen des Buttons zur Liste

    def draw_health(self, health, x, y, surface, flip):
        """
        Zeichnet eine Gesundheitsanzeige auf der angegebenen Oberfläche.
        Parameter:
        health (float): Der aktuelle Gesundheitswert (0-100).
        x (int): Die x-Position der Gesundheitsanzeige.
        y (int): Die y-Position der Gesundheitsanzeige.
        surface (pygame.Surface): Die Oberfläche, auf der die Gesundheitsanzeige gezeichnet wird.
        flip (bool): Bestimmt die Richtung der Anzeige.
        """
        ratio_m = health / 100  # Verhältnis der Gesundheit zu 100
        if not flip:
            pygame.draw.rect(surface, (0, 255, 0), (x, y, 200 * ratio_m, 35))  # Zeichnen der Gesundheitsanzeige (links nach rechts)
        else:
            pygame.draw.rect(surface, (0, 255, 0), (x + int(200 * (1 - ratio_m)), y, int(200 * ratio_m), 35))  # Zeichnen der Gesundheitsanzeige (rechts nach links)

    def draw_tank(self, tank, x, y, surface, flip):
        """
        Zeichnet eine Tankanzeige auf der angegebenen Oberfläche.
        Parameter:
        tank (float): Der aktuelle Tankfüllstand (0-100).
        x (int): Die x-Position der Tankanzeige.
        y (int): Die y-Position der Tankanzeige.
        surface (pygame.Surface): Die Oberfläche, auf der die Tankanzeige gezeichnet wird.
        flip (bool): Bestimmt die Richtung der Anzeige.
        """
        ratio_m = tank / 100  # Verhältnis des Tankfüllstands zu 100
        if not flip:
            pygame.draw.rect(surface, (0, 255, 255), (x, y, 100 * ratio_m, 35))  # Zeichnen der Tankanzeige (links nach rechts)
        else:
            pygame.draw.rect(surface, (0, 255, 255), (x + int(100 * (1 - ratio_m)), y, int(100 * ratio_m), 35))  # Zeichnen der Tankanzeige (rechts nach links)

    def update(self, event):
        """
        Aktualisiert den Zustand der UI-Elemente basierend auf Ereignissen.
        Parameter:
        event (pygame.event.Event): Das Ereignis, das verarbeitet wird.
        """
        for button in self.buttons:
            button.update(event)  # Aktualisieren jedes Buttons

    def draw(self):
        """
        Zeichnet alle UI-Elemente auf der Oberfläche.
        """
        for button in self.buttons:
            button.draw(self.screen)  # Zeichnen jedes Buttons

    def set_button_position(self, index, position):
        """
        Setzt die Position eines Buttons.
        Parameter:
        index (int): Der Index des Buttons in der Liste.
        position (tuple): Die neue (x, y) Position des Buttons.
        """
        if 0 <= index < len(self.buttons):
            self.buttons[index].position = position
            self.buttons[index].rect = pygame.Rect(self.buttons[index].position[0], self.buttons[index].position[1],
                                                   self.buttons[index].width, self.buttons[index].height)

    def set_button_visible(self, index, visible):
        """
        Setzt die Sichtbarkeit eines Buttons.
        Parameter:
        index (int): Der Index des Buttons in der Liste.
        visible (bool): Die neue Sichtbarkeit des Buttons.
        """
        if 0 <= index < len(self.buttons):
            self.buttons[index].set_visible(visible)