import pygame
import sys
import subprocess

# Konstanten
WIDTH, HEIGHT = 1920, 1030
FPS = 60

class MainMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('PanzerGame')

        # Eigene Schriftart laden
        self.font = pygame.font.Font("Assets/Schrift/Pixellari.ttf", 74)

        # Hintergrundbild laden
        self.background_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/BattleTanks.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

        # Button-Bilder laden und skalieren
        button_width, button_height = 400, 100
        button_gap = 150
        button_y = HEIGHT // 2 - 1.5 * button_height + 50  # Adjusted position

        self.start_button_image = pygame.image.load('Assets/Buttons/Start1.png')
        self.start_button_image = pygame.transform.scale(self.start_button_image, (button_width, button_height))
        self.start_button_hover_image = pygame.image.load('Assets/Buttons/Start2.png')
        self.start_button_hover_image = pygame.transform.scale(self.start_button_hover_image, (button_width, button_height))
        self.start_button_rect = self.start_button_image.get_rect(center=(WIDTH // 2, button_y))

        self.options_button_image = pygame.image.load('Assets/Buttons/Options1.png')
        self.options_button_image = pygame.transform.scale(self.options_button_image, (button_width, button_height))
        self.options_button_hover_image = pygame.image.load('Assets/Buttons/Options2.png')
        self.options_button_hover_image = pygame.transform.scale(self.options_button_hover_image, (button_width, button_height))
        self.options_button_rect = self.options_button_image.get_rect(center=(WIDTH // 2, button_y + button_gap))

        self.quit_button_image = pygame.image.load('Assets/Buttons/Quit1.png')
        self.quit_button_image = pygame.transform.scale(self.quit_button_image, (button_width, button_height))
        self.quit_button_hover_image = pygame.image.load('Assets/Buttons/Quit2.png')
        self.quit_button_hover_image = pygame.transform.scale(self.quit_button_hover_image, (button_width, button_height))
        self.quit_button_rect = self.quit_button_image.get_rect(center=(WIDTH // 2, button_y + 2 * button_gap))

        # Musik laden und abspielen
        pygame.mixer.music.load("Assets/Audio/Clash of Clans Main Theme 1.mp3")
        pygame.mixer.music.play(-1)  # -1 für Endlosschleife

        # Zustand der Musik (AN/AUS)
        self.music_on = True

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            self.screen.blit(self.background_image, (0, 0))

            # Zeichnen der Buttons mit Hover-Effekt
            mouse_pos = pygame.mouse.get_pos()
            self.draw_button(self.start_button_rect, self.start_button_image, self.start_button_hover_image, mouse_pos)
            self.draw_button(self.options_button_rect, self.options_button_image, self.options_button_hover_image, mouse_pos)
            self.draw_button(self.quit_button_rect, self.quit_button_image, self.quit_button_hover_image, mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button_rect.collidepoint(mouse_pos):
                        self.open_start_window()
                        running = False
                    elif self.options_button_rect.collidepoint(mouse_pos):
                        self.open_options()
                    elif self.quit_button_rect.collidepoint(mouse_pos):
                        running = False

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()
        sys.exit()

    def draw_button(self, rect, image, hover_image, mouse_pos):
        if rect.collidepoint(mouse_pos):
            self.screen.blit(hover_image, rect.topleft)
        else:
            self.screen.blit(image, rect.topleft)

    def open_start_window(self):
        start_window = StartWindow(self)
        start_window.run()

    def open_options(self):
        options_window = OptionsWindow(self, self.music_on)
        options_window.run()

class StartWindow:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Start Window')

        # Hintergrundbild für das Startfenster laden
        self.background_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/SpielmodusBackground.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

        # Button-Bilder für Start-Button laden und skalieren
        self.start_game_button_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/1vs1_1.png')
        self.start_game_button_image = pygame.transform.scale(self.start_game_button_image, (400, 100))
        self.start_game_button_hover_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/1vs1_2.png')
        self.start_game_button_hover_image = pygame.transform.scale(self.start_game_button_hover_image, (400, 100))
        self.start_game_button_rect = self.start_game_button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # Zurück-Button Bild laden und skalieren
        self.back_button_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Zurück1.png')
        self.back_button_image = pygame.transform.scale(self.back_button_image, (400, 100))
        self.back_button_hover_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Zurück2.png')
        self.back_button_hover_image = pygame.transform.scale(self.back_button_hover_image, (400, 100))
        self.back_button_rect = self.back_button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            self.screen.blit(self.background_image, (0, 0))

            # Zeichnen des Start-Buttons mit Hover-Effekt
            mouse_pos = pygame.mouse.get_pos()
            self.draw_button(self.start_game_button_rect, self.start_game_button_image, self.start_game_button_hover_image, mouse_pos)
            self.draw_back_button(mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.main_menu.run()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_game_button_rect.collidepoint(mouse_pos):
                        self.open_map_selection()
                        running = False
                    elif self.back_button_rect.collidepoint(mouse_pos):
                        running = False
                        self.main_menu.run()

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()

    def draw_button(self, rect, image, hover_image, mouse_pos):
        if rect.collidepoint(mouse_pos):
            self.screen.blit(hover_image, rect.topleft)
        else:
            self.screen.blit(image, rect.topleft)

    def draw_back_button(self, mouse_pos):
        if self.back_button_rect.collidepoint(mouse_pos):
            self.screen.blit(self.back_button_hover_image, self.back_button_rect.topleft)
        else:
            self.screen.blit(self.back_button_image, self.back_button_rect.topleft)

    def open_map_selection(self):
        map_selection_window = MapSelectionWindow(self.main_menu)
        map_selection_window.run()

class MapSelectionWindow:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Map Selection Window')

        # Hintergrundbild für das Karten-Auswahl-Fenster laden
        self.background_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/MapsBackground.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

        # Button-Bilder für Karten-Auswahl-Buttons laden und skalieren
        self.map1_button_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Schnee1.png')
        self.map1_button_image = pygame.transform.scale(self.map1_button_image, (400, 100))
        self.map1_button_hover_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Schnee2.png')
        self.map1_button_hover_image = pygame.transform.scale(self.map1_button_hover_image, (400, 100))

        self.map2_button_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Vulkan1.png')
        self.map2_button_image = pygame.transform.scale(self.map2_button_image, (400, 100))
        self.map2_button_hover_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Vulkan2.png')
        self.map2_button_hover_image = pygame.transform.scale(self.map2_button_hover_image, (400, 100))

        self.map3_button_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Space1.png')
        self.map3_button_image = pygame.transform.scale(self.map3_button_image, (400, 100))
        self.map3_button_hover_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Space2.png')
        self.map3_button_hover_image = pygame.transform.scale(self.map3_button_hover_image, (400, 100))

        # Zurück-Button Bild laden und skalieren
        self.back_button_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Zurück1.png')
        self.back_button_image = pygame.transform.scale(self.back_button_image, (400, 100))
        self.back_button_hover_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Zurück2.png')
        self.back_button_hover_image = pygame.transform.scale(self.back_button_hover_image, (400, 100))

        # Positionen der Buttons
        button_gap = 150
        button_y = HEIGHT // 2 - 1.5 * button_gap + 50  # Adjusted position

        self.map1_button_rect = self.map1_button_image.get_rect(center=(WIDTH // 2, button_y))
        self.map2_button_rect = self.map2_button_image.get_rect(center=(WIDTH // 2, button_y + button_gap))
        self.map3_button_rect = self.map3_button_image.get_rect(center=(WIDTH // 2, button_y + 2 * button_gap))
        self.back_button_rect = self.back_button_image.get_rect(center=(WIDTH // 2, button_y + 3 * button_gap))

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            self.screen.blit(self.background_image, (0, 0))

            # Zeichnen der Buttons mit Hover-Effekt
            mouse_pos = pygame.mouse.get_pos()
            self.draw_button(self.map1_button_rect, self.map1_button_image, self.map1_button_hover_image, mouse_pos)
            self.draw_button(self.map2_button_rect, self.map2_button_image, self.map2_button_hover_image, mouse_pos)
            self.draw_button(self.map3_button_rect, self.map3_button_image, self.map3_button_hover_image, mouse_pos)
            self.draw_button(self.back_button_rect, self.back_button_image, self.back_button_hover_image, mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.map1_button_rect.collidepoint(mouse_pos):
                        self.start_game('map1')  # Hier könnte der Name der Karte übergeben werden
                        running = False
                    elif self.map2_button_rect.collidepoint(mouse_pos):
                        self.start_game('map2')  # Hier könnte der Name der Karte übergeben werden
                        running = False
                    elif self.map3_button_rect.collidepoint(mouse_pos):
                        self.start_game('map3')  # Hier könnte der Name der Karte übergeben werden
                        running = False
                    elif self.back_button_rect.collidepoint(mouse_pos):
                        running = False
                        self.open_start_window()

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()

    def draw_button(self, rect, image, hover_image, mouse_pos):
        if rect.collidepoint(mouse_pos):
            self.screen.blit(hover_image, rect.topleft)
        else:
            self.screen.blit(image, rect.topleft)

    def start_game(self, map_name):
        # Hier könnte die Logik für den Spielstart eingefügt werden
        print(f'Starting game on map: {map_name}')
        subprocess.Popen([sys.executable, 'game.py'])  # Starten des Spiels
        pygame.quit()  # Pygame beenden

    def open_start_window(self):
        start_window = StartWindow(self.main_menu)
        start_window.run()

class OptionsWindow:
    def __init__(self, main_menu, music_on):
        self.main_menu = main_menu
        self.music_on = music_on  # Zustand des Musik-Buttons
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Options Window')

        # Hintergrundbild für das Optionsfenster laden
        self.background_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/OptionsBackground.png')
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

        # Button-Bilder für Musik-Button laden und skalieren
        self.music_on_button_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/MusikAN1.png')
        self.music_on_button_image = pygame.transform.scale(self.music_on_button_image, (400, 100))
        self.music_on_button_hover_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/MusikAN2.png')
        self.music_on_button_hover_image = pygame.transform.scale(self.music_on_button_hover_image, (400, 100))

        self.music_off_button_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/MusikAUS1.png')
        self.music_off_button_image = pygame.transform.scale(self.music_off_button_image, (400, 100))
        self.music_off_button_hover_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/MusikAUS2.png')
        self.music_off_button_hover_image = pygame.transform.scale(self.music_off_button_hover_image, (400, 100))

        self.music_button_rect = self.music_on_button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # Button-Bilder für Zurück-Button laden und skalieren
        self.back_button_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Zurück1.png')
        self.back_button_image = pygame.transform.scale(self.back_button_image, (400, 100))
        self.back_button_hover_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Zurück2.png')
        self.back_button_hover_image = pygame.transform.scale(self.back_button_hover_image, (400, 100))
        self.back_button_rect = self.back_button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            self.screen.blit(self.background_image, (0, 0))

            # Zeichnen der Buttons mit Hover-Effekt
            mouse_pos = pygame.mouse.get_pos()
            self.draw_button(self.music_button_rect, mouse_pos)
            self.draw_back_button(mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.main_menu.run()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.music_button_rect.collidepoint(mouse_pos):
                        self.toggle_music()
                    elif self.back_button_rect.collidepoint(mouse_pos):
                        running = False
                        self.main_menu.run()

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()

    def draw_button(self, rect, mouse_pos):
        if self.music_on:
            image = self.music_on_button_image
            hover_image = self.music_on_button_hover_image
        else:
            image = self.music_off_button_image
            hover_image = self.music_off_button_hover_image

        if rect.collidepoint(mouse_pos):
            self.screen.blit(hover_image, rect.topleft)
        else:
            self.screen.blit(image, rect.topleft)

    def draw_back_button(self, mouse_pos):
        if self.back_button_rect.collidepoint(mouse_pos):
            self.screen.blit(self.back_button_hover_image, self.back_button_rect.topleft)
        else:
            self.screen.blit(self.back_button_image, self.back_button_rect.topleft)

    def toggle_music(self):
        if self.music_on:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        self.music_on = not self.music_on
        self.main_menu.music_on = self.music_on  # Aktualisieren des Musik-Zustands im Hauptmenü

if __name__ == '__main__':
    main_menu = MainMenu()
    main_menu.run()
