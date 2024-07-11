import pygame

# Pfad zur heruntergeladenen Schriftart
font_path = "Assets\Schrift\Pixellari.ttf"

class UI:
    def __init__(self, screen):
        """
        Initialisierungsmethode für die Klasse UI.
        Parameter:
        screen (pygame.Surface): Die Oberfläche, auf der das UI gezeichnet wird.
        """
        self.screen = screen
        self.buttons = []  # Liste zur Speicherung der Buttons
        

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

    def draw_armor(self, armor, x, y , surface, flip):
        """
        Zeichnet eine Rüstungsanzeige auf der angegebenen Oberfläche.
        Parameter:
        tank (float): Der aktuelle Rüstung (0-50).
        x (int): Die x-Position der Rüstungsanzeige.
        y (int): Die y-Position der Rüstungsanzeige.
        surface (pygame.Surface): Die Oberfläche, auf der die Rüstungsanzeige gezeichnet wird.
        flip (bool): Bestimmt die Richtung der Anzeige.
        """
        ratio_m = armor / 50  # Verhältnis der Rüstung zu 50
        if not flip:
            pygame.draw.rect(surface, (0, 0, 255), (x, y, 200 * ratio_m, 17.5))  # Zeichnen der Rüstungsanzeige (links nach rechts)
        else:
            pygame.draw.rect(surface, (0, 0, 255), (x + int(200 * (1 - ratio_m)), y, int(200 * ratio_m), 17.5))  # Zeichnen der Rüstungsanzeige (rechts nach links)

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