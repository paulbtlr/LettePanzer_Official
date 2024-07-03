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
                        self.start_game()
                        running = False
                    elif self.options_button_rect.collidepoint(mouse_pos):
                        self.open_options()
                        running = False
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

    def start_game(self):
        subprocess.Popen([sys.executable, 'game.py'])

    def open_options(self):
        options_window = OptionsWindow(self)
        options_window.run()

class OptionsWindow:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.music_on = True  # Zustand des Musik-Buttons

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
            self.main_menu.screen.blit(self.background_image, (0, 0))

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

    def draw_button(self, rect, mouse_pos):
        if self.music_on:
            image = self.music_on_button_image
            hover_image = self.music_on_button_hover_image
        else:
            image = self.music_off_button_image
            hover_image = self.music_off_button_hover_image

        if rect.collidepoint(mouse_pos):
            self.main_menu.screen.blit(hover_image, rect.topleft)
        else:
            self.main_menu.screen.blit(image, rect.topleft)

    def draw_back_button(self, mouse_pos):
        if self.back_button_rect.collidepoint(mouse_pos):
            self.main_menu.screen.blit(self.back_button_hover_image, self.back_button_rect.topleft)
        else:
            self.main_menu.screen.blit(self.back_button_image, self.back_button_rect.topleft)

    def toggle_music(self):
        self.music_on = not self.music_on

if __name__ == '__main__':
    main_menu = MainMenu()
    main_menu.run()
