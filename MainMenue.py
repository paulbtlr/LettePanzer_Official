import pygame
import sys
import subprocess

# Konstanten für Bildschirmgröße und Bildwiederholrate
WIDTH, HEIGHT = 1920, 1080
FPS = 60

class MainMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Erstellt das Hauptfenster
        pygame.display.set_caption('PanzerGame')  # Setzt den Fenstertitel

        # Benutzerdefinierte Schriftart laden
        self.font = pygame.font.Font("Assets/Schrift/Pixellari.ttf", 74)

        # Hintergrundbild laden und skalieren
        self.background_image = pygame.image.load('Assets/Screens/Menü/BattleTanks.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

       # Schaltflächenbilder laden und skalieren
        button_width, button_height = 400, 100
        button_gap = 150
        button_y = HEIGHT // 2 - 1.5 * button_height + 50  # Position der Schaltflächen anpassen

        self.start_button_image = pygame.image.load('Assets/Screens/Buttons/Start1.png')
        self.start_button_image = pygame.transform.scale(self.start_button_image, (button_width, button_height))
        self.start_button_hover_image = pygame.image.load('Assets/Screens/Buttons/Start2.png')
        self.start_button_hover_image = pygame.transform.scale(self.start_button_hover_image, (button_width, button_height))
        self.start_button_rect = self.start_button_image.get_rect(center=(WIDTH // 2, button_y))

        self.options_button_image = pygame.image.load('Assets/Screens/Buttons/Options1.png')
        self.options_button_image = pygame.transform.scale(self.options_button_image, (button_width, button_height))
        self.options_button_hover_image = pygame.image.load('Assets/Screens/Buttons/Options2.png')
        self.options_button_hover_image = pygame.transform.scale(self.options_button_hover_image, (button_width, button_height))
        self.options_button_rect = self.options_button_image.get_rect(center=(WIDTH // 2, button_y + button_gap))

        self.quit_button_image = pygame.image.load('Assets/Screens/Buttons/Quit1.png')
        self.quit_button_image = pygame.transform.scale(self.quit_button_image, (button_width, button_height))
        self.quit_button_hover_image = pygame.image.load('Assets/Screens/Buttons/Quit2.png')
        self.quit_button_hover_image = pygame.transform.scale(self.quit_button_hover_image, (button_width, button_height))
        self.quit_button_rect = self.quit_button_image.get_rect(center=(WIDTH // 2, button_y + 2 * button_gap))

        # Musik laden und abspielen
        pygame.mixer.music.load("Assets/Audio/Clash of Clans Main Theme 1.mp3")
        pygame.mixer.music.play(-1)  # -1 für Endlosschleife

        # Musikstatus (AN/AUS)
        self.music_on = True

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            self.screen.blit(self.background_image, (0, 0))

            # Schaltflächen mit Hover-Effekt zeichnen
            mouse_pos = pygame.mouse.get_pos()
            self.draw_button(self.start_button_rect, self.start_button_image, self.start_button_hover_image, mouse_pos)
            self.draw_button(self.options_button_rect, self.options_button_image, self.options_button_hover_image, mouse_pos)
            self.draw_button(self.quit_button_rect, self.quit_button_image, self.quit_button_hover_image, mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button_rect.collidepoint(mouse_pos):
                        self.open_start_window()  # Öffnet das Startfenster
                        running = False
                    elif self.options_button_rect.collidepoint(mouse_pos):
                        self.open_options()  # Öffnet das Optionsfenster
                    elif self.quit_button_rect.collidepoint(mouse_pos):
                        running = False  # Beendet das Programm

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()
        sys.exit()

    def draw_button(self, rect, image, hover_image, mouse_pos):
        """Zeichnet eine Schaltfläche mit oder ohne Hover-Effekt."""
        if rect.collidepoint(mouse_pos):
            self.screen.blit(hover_image, rect.topleft)
        else:
            self.screen.blit(image, rect.topleft)

    def open_start_window(self):
        """Öffnet das Startfenster für die Spielmodusauswahl."""
        start_window = StartWindow(self)
        start_window.run()

    def open_options(self):
        """Öffnet das Optionsfenster für Einstellungen."""
        options_window = OptionsWindow(self, self.music_on)
        options_window.run()

class StartWindow:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Start Window')

        # Hintergrundbild für das Startfenster laden
        self.background_image = pygame.image.load('Assets/Screens/Menü/SpielmodusBackground.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

        # Schaltflächenbilder für Start- und Zurück-Schaltflächen laden und skalieren
        self.start_game_button_image = pygame.image.load('Assets/Screens/Buttons/1vs1_1.png')
        self.start_game_button_image = pygame.transform.scale(self.start_game_button_image, (400, 100))
        self.start_game_button_hover_image = pygame.image.load('Assets/Screens/Buttons/1vs1_2.png')
        self.start_game_button_hover_image = pygame.transform.scale(self.start_game_button_hover_image, (400, 100))
        self.start_game_button_rect = self.start_game_button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        self.back_button_image = pygame.image.load('Assets/Screens/Buttons/Zurück1.png')
        self.back_button_image = pygame.transform.scale(self.back_button_image, (400, 100))
        self.back_button_hover_image = pygame.image.load('Assets/Screens/Buttons/Zurück2.png')
        self.back_button_hover_image = pygame.transform.scale(self.back_button_hover_image, (400, 100))
        self.back_button_rect = self.back_button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            self.screen.blit(self.background_image, (0, 0))

            # Start-Schaltfläche mit Hover-Effekt zeichnen
            mouse_pos = pygame.mouse.get_pos()
            self.draw_button(self.start_game_button_rect, self.start_game_button_image, self.start_game_button_hover_image, mouse_pos)
            self.draw_back_button(mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.main_menu.run()    # Zurück zum Hauptmenü
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_game_button_rect.collidepoint(mouse_pos):
                        self.open_map_selection()   # Öffnet die Kartenwahl
                        running = False
                    elif self.back_button_rect.collidepoint(mouse_pos):
                        running = False
                        self.main_menu.run()    # Zurück zum Hauptmenü

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()

    def draw_button(self, rect, image, hover_image, mouse_pos):
        """Zeichnet eine Schaltfläche mit oder ohne Hover-Effekt."""
        if rect.collidepoint(mouse_pos):
            self.screen.blit(hover_image, rect.topleft)
        else:
            self.screen.blit(image, rect.topleft)

    def draw_back_button(self, mouse_pos):
        """Zeichnet die Zurück-Schaltfläche mit oder ohne Hover-Effekt."""
        if self.back_button_rect.collidepoint(mouse_pos):
            self.screen.blit(self.back_button_hover_image, self.back_button_rect.topleft)
        else:
            self.screen.blit(self.back_button_image, self.back_button_rect.topleft)

    def open_map_selection(self):
        """Öffnet das Fenster zur Auswahl der Karte."""
        map_selection_window = MapSelectionWindow(self.main_menu)
        map_selection_window.run()

class MapSelectionWindow:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Map Selection Window')

        # Hintergrundbild für das Kartenwahl-Fenster laden
        self.background_image = pygame.image.load('Assets/Screens/Menü/MapsBackground.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

        # Schaltflächenbilder für Kartenwahl laden und skalieren
        self.map1_button_image = pygame.image.load('Assets/Screens/Buttons/Schnee1.png')
        self.map1_button_image = pygame.transform.scale(self.map1_button_image, (400, 100))
        self.map1_button_hover_image = pygame.image.load('Assets/Screens/Buttons/Schnee2.png')
        self.map1_button_hover_image = pygame.transform.scale(self.map1_button_hover_image, (400, 100))

        self.map2_button_image = pygame.image.load('Assets/Screens/Buttons/Vulkan1.png')
        self.map2_button_image = pygame.transform.scale(self.map2_button_image, (400, 100))
        self.map2_button_hover_image = pygame.image.load('Assets/Screens/Buttons/Vulkan2.png')
        self.map2_button_hover_image = pygame.transform.scale(self.map2_button_hover_image, (400, 100))

        self.map3_button_image = pygame.image.load('Assets/Screens/Buttons/Space1.png')
        self.map3_button_image = pygame.transform.scale(self.map3_button_image, (400, 100))
        self.map3_button_hover_image = pygame.image.load('Assets/Screens/Buttons/Space2.png')
        self.map3_button_hover_image = pygame.transform.scale(self.map3_button_hover_image, (400, 100))

        button_gap = 150
        button_y = HEIGHT // 2 - 1.5 * 100 + 50  # Adjusted position

        self.map1_button_rect = self.map1_button_image.get_rect(center=(WIDTH // 2, button_y))
        self.map2_button_rect = self.map2_button_image.get_rect(center=(WIDTH // 2, button_y + button_gap))
        self.map3_button_rect = self.map3_button_image.get_rect(center=(WIDTH // 2, button_y + 2 * button_gap))

        # Load and scale back button image
        self.back_button_image = pygame.image.load('Assets/Screens/Buttons/Zurück1.png')
        self.back_button_image = pygame.transform.scale(self.back_button_image, (400, 100))
        self.back_button_hover_image = pygame.image.load('Assets/Screens/Buttons/Zurück2.png')
        self.back_button_hover_image = pygame.transform.scale(self.back_button_hover_image, (400, 100))
        self.back_button_rect = self.back_button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 300))

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            self.screen.blit(self.background_image, (0, 0))

            # Kartenwahl-Schaltfläche mit Hover-Effekt zeichnen
            mouse_pos = pygame.mouse.get_pos()
            self.draw_button(self.map1_button_rect, self.map1_button_image, self.map1_button_hover_image, mouse_pos)
            self.draw_button(self.map2_button_rect, self.map2_button_image, self.map2_button_hover_image, mouse_pos)
            self.draw_button(self.map3_button_rect, self.map3_button_image, self.map3_button_hover_image, mouse_pos)
            self.draw_back_button(mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.main_menu.run()    # Zurück zum Hauptmenü
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.map1_button_rect.collidepoint(mouse_pos):
                        self.start_game('map1') # Startet das Spiel mit ausgewählter Karte
                        running = False
                    elif self.map2_button_rect.collidepoint(mouse_pos):
                        self.start_game('map2') # Startet das Spiel mit ausgewählter Karte
                        running = False
                    elif self.map3_button_rect.collidepoint(mouse_pos):
                        self.start_game('map3') # Startet das Spiel mit ausgewählter Karte
                        running = False
                    elif self.back_button_rect.collidepoint(mouse_pos):
                        running = False
                        self.main_menu.run()    # Zurück zum Hauptmenü

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()

    def draw_button(self, rect, image, hover_image, mouse_pos):
        """Zeichnet eine Schaltfläche mit oder ohne Hover-Effekt."""
        if rect.collidepoint(mouse_pos):
            self.screen.blit(hover_image, rect.topleft)
        else:
            self.screen.blit(image, rect.topleft)

    def draw_back_button(self, mouse_pos):
        """Zeichnet die Zurück-Schaltfläche mit oder ohne Hover-Effekt."""
        if self.back_button_rect.collidepoint(mouse_pos):
            self.screen.blit(self.back_button_hover_image, self.back_button_rect.topleft)
        else:
            self.screen.blit(self.back_button_image, self.back_button_rect.topleft)

    def start_game(self, map_name):
        """Startet das Spiel mit der ausgewählten Karte."""
        if map_name == 'map1':
            background_image_path = 'Assets/Game/Background/BGSchnee.png'
        elif map_name == 'map2':
            background_image_path = 'Assets/Game/Background/BGVulkan.png'
        elif map_name == 'map3':
            background_image_path = 'Assets/Game/Background/BGSpace.png'
        else:
            background_image_path = 'Assets/Game/Background/BGSchnee.png'  # Default

        # Launch the game with the selected map
        subprocess.Popen([sys.executable, 'game.py', map_name, background_image_path])
        pygame.quit()

class OptionsWindow:
    def __init__(self, main_menu, music_on):
        self.main_menu = main_menu
        # Musikstatus (AN/AUS)
        self.music_on = music_on
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Options Window')

        # Hintergrundbild für das Options-Fenster laden
        self.background_image = pygame.image.load('Assets/Screens/Menü/OptionsBackground.png')
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

        # Schaltflächenbilder für Musik und Zurück laden und skalieren
        self.music_on_button_image = pygame.image.load('Assets/Screens/Buttons/MusikAn1.png')
        self.music_on_button_image = pygame.transform.scale(self.music_on_button_image, (400, 100))
        self.music_off_button_image = pygame.image.load('Assets/Screens/Buttons/MusikAus1.png')
        self.music_off_button_image = pygame.transform.scale(self.music_off_button_image, (400, 100))
        self.music_button_rect = self.music_on_button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        self.back_button_image = pygame.image.load('Assets/Screens/Buttons/Zurück1.png')
        self.back_button_image = pygame.transform.scale(self.back_button_image, (400, 100))
        self.back_button_hover_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Zurück2.png')
        self.back_button_hover_image = pygame.transform.scale(self.back_button_hover_image, (400, 100))
        self.back_button_rect = self.back_button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            self.screen.blit(self.background_image, (0, 0))

            # Musik-Schaltfläche zeichnen
            if self.music_on:
                self.screen.blit(self.music_on_button_image, self.music_button_rect.topleft)
            else:
                self.screen.blit(self.music_off_button_image, self.music_button_rect.topleft)

            # Zurück-Schaltfläche mit Hover-Effekt zeichnen
            mouse_pos = pygame.mouse.get_pos()
            self.draw_back_button(mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.main_menu.run()    # Zurück zum Hauptmenü
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.music_button_rect.collidepoint(mouse_pos):
                        self.toggle_music() # Musik AN/AUS schalten
                    elif self.back_button_rect.collidepoint(mouse_pos):
                        running = False
                        self.main_menu.run()    # Zurück zum Hauptmenü

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()

    def draw_back_button(self, mouse_pos):
        """Zeichnet die Zurück-Schaltfläche mit oder ohne Hover-Effekt."""
        if self.back_button_rect.collidepoint(mouse_pos):
            self.screen.blit(self.back_button_hover_image, self.back_button_rect.topleft)
        else:
            self.screen.blit(self.back_button_image, self.back_button_rect.topleft)

    def toggle_music(self):
        """Schaltet die Musik AN oder AUS."""
        self.music_on = not self.music_on
        if self.music_on:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

if __name__ == '__main__':
    main_menu = MainMenu()
    main_menu.run()
