import pygame
import sys
import subprocess

# Konstanten
WIDTH, HEIGHT = 2400, 1200
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BUTTON_WIDTH, BUTTON_HEIGHT = 400, 100

class MainMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('PanzerGame')
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)

        # Positionen der Schaltflächen
        self.start_button_rect = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - 1.5 * BUTTON_HEIGHT), (BUTTON_WIDTH, BUTTON_HEIGHT))
        self.options_button_rect = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 - 0.5 * BUTTON_HEIGHT + 20), (BUTTON_WIDTH, BUTTON_HEIGHT))
        self.quit_button_rect = pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 + 0.5 * BUTTON_HEIGHT + 40), (BUTTON_WIDTH, BUTTON_HEIGHT))

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            self.screen.fill(GRAY)
            self.draw_text('PanzerGame', self.font, BLACK, WIDTH // 2, HEIGHT // 4)

            # Zeichnen der Schaltflächen
            self.draw_button(self.start_button_rect, 'Start')
            self.draw_button(self.options_button_rect, 'Optionen')
            self.draw_button(self.quit_button_rect, 'Beenden')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
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
        
    def draw_text(self, text, font, color, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        self.screen.blit(text_obj, text_rect)

    def draw_button(self, rect, text):
        pygame.draw.rect(self.screen, WHITE, rect)
        self.draw_text(text, self.small_font, BLACK, rect.centerx, rect.centery)

    def start_game(self):
        subprocess.Popen([sys.executable, 'game.py'])

    def show_options(self):
        print("Optionen anzeigen...")  # Platzhalter für die Optionslogik


if __name__ == '__main__':
    main_menu = MainMenu()
    main_menu.run()
