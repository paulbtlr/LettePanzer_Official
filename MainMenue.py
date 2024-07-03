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
        options_window = OptionsWindow(self)
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

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            self.screen.blit(self.background_image, (0, 0))

            # Zeichnen des Start-Buttons mit Hover-Effekt
            mouse_pos = pygame.mouse.get_pos()
            self.draw_button(self.start_game_button_rect, self.start_game_button_image, self.start_game_button_hover_image, mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_game_button_rect.collidepoint(mouse_pos):
                        self.open_map_selection()
                        running = False

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()

    def draw_button(self, rect, image, hover_image, mouse_pos):
        if rect.collidepoint(mouse_pos):
            self.screen.blit(hover_image, rect.topleft)
        else:
            self.screen.blit(image, rect.topleft)

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

        button_gap = 150
        button_y = HEIGHT // 2 - 0.5 * button_gap

        self.map1_button_rect = self.map1_button_image.get_rect(center=(WIDTH // 2, button_y))
        self.map2_button_rect = self.map2_button_image.get_rect(center=(WIDTH // 2, button_y + button_gap))
        self.map3_button_rect = self.map3_button_image.get_rect(center=(WIDTH // 2, button_y + 2 * button_gap))

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

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.map1_button_rect.collidepoint(mouse_pos):
                        self.start_game()
                    elif self.map2_button_rect.collidepoint(mouse_pos):
                        self.start_game()
                    elif self.map3_button_rect.collidepoint(mouse_pos):
                        self.start_game()

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()

    def draw_button(self, rect, image, hover_image, mouse_pos):
        if rect.collidepoint(mouse_pos):
            self.screen.blit(hover_image, rect.topleft)
        else:
            self.screen.blit(image, rect.topleft)

    def start_game(self):
        subprocess.Popen([sys.executable, 'game.py'])

if __name__ == '__main__':
    main_menu = MainMenu()
    main_menu.run()
