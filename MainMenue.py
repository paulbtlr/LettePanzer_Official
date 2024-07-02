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
        self.background_image = pygame.image.load('Assets/Bilder/Hintergrund/WinnerScreen/BattleTanks.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

        # Button-Bilder laden und skalieren
        self.start_button_image = pygame.image.load('Assets/Buttons/Start1.png')
        self.start_button_image = pygame.transform.scale(self.start_button_image, (400, 100))
        self.start_button_hover_image = pygame.image.load('Assets/Buttons/Start2.png')
        self.start_button_hover_image = pygame.transform.scale(self.start_button_hover_image, (400, 100))

        self.options_button_image = pygame.image.load('Assets/Buttons/Options1.png')
        self.options_button_image = pygame.transform.scale(self.options_button_image, (400, 100))
        self.options_button_hover_image = pygame.image.load('Assets/Buttons/Options2.png')
        self.options_button_hover_image = pygame.transform.scale(self.options_button_hover_image, (400, 100))

        self.quit_button_image = pygame.image.load('Assets/Buttons/Quit1.png')
        self.quit_button_image = pygame.transform.scale(self.quit_button_image, (400, 100))
        self.quit_button_hover_image = pygame.image.load('Assets/Buttons/Quit2.png')
        self.quit_button_hover_image = pygame.transform.scale(self.quit_button_hover_image, (400, 100))

        # Positionen der Buttons
        self.start_button_rect = self.start_button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 2))
        self.options_button_rect = self.options_button_image.get_rect(center=(WIDTH // 2, HEIGHT //  + 1.6))
        self.quit_button_rect = self.quit_button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 250))

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
                        self.show_options()
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

    def show_options(self):
        print("Optionen anzeigen...")  # Platzhalter für die Optionslogik

if __name__ == '__main__':
    main_menu = MainMenu()
    main_menu.run()
