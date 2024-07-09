import pygame
import sys
import subprocess

# Constants
WIDTH, HEIGHT = 1920, 1030
FPS = 60

class MainMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('PanzerGame')

        # Load custom font
        self.font = pygame.font.Font("Assets/Schrift/Pixellari.ttf", 74)

        # Load background image
        self.background_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/BattleTanks.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

        # Load and scale button images
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

        # Load and play music
        pygame.mixer.music.load("Assets/Audio/Clash of Clans Main Theme 1.mp3")
        pygame.mixer.music.play(-1)  # -1 for infinite loop

        # Music state (ON/OFF)
        self.music_on = True

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            self.screen.blit(self.background_image, (0, 0))

            # Draw buttons with hover effect
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

        # Load background image for the start window
        self.background_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/SpielmodusBackground.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

        # Load and scale button images for start button
        self.start_game_button_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/1vs1_1.png')
        self.start_game_button_image = pygame.transform.scale(self.start_game_button_image, (400, 100))
        self.start_game_button_hover_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/1vs1_2.png')
        self.start_game_button_hover_image = pygame.transform.scale(self.start_game_button_hover_image, (400, 100))
        self.start_game_button_rect = self.start_game_button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # Load and scale back button image
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

            # Draw start button with hover effect
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

        # Load background image for the map selection window
        self.background_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/MapsBackground.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

        # Load and scale button images for map selection buttons
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
        button_y = HEIGHT // 2 - 1.5 * 100 + 50  # Adjusted position

        self.map1_button_rect = self.map1_button_image.get_rect(center=(WIDTH // 2, button_y))
        self.map2_button_rect = self.map2_button_image.get_rect(center=(WIDTH // 2, button_y + button_gap))
        self.map3_button_rect = self.map3_button_image.get_rect(center=(WIDTH // 2, button_y + 2 * button_gap))

        # Load and scale back button image
        self.back_button_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Zurück1.png')
        self.back_button_image = pygame.transform.scale(self.back_button_image, (400, 100))
        self.back_button_hover_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Zurück2.png')
        self.back_button_hover_image = pygame.transform.scale(self.back_button_hover_image, (400, 100))
        self.back_button_rect = self.back_button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 300))

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            self.screen.blit(self.background_image, (0, 0))

            # Draw map selection buttons with hover effect
            mouse_pos = pygame.mouse.get_pos()
            self.draw_button(self.map1_button_rect, self.map1_button_image, self.map1_button_hover_image, mouse_pos)
            self.draw_button(self.map2_button_rect, self.map2_button_image, self.map2_button_hover_image, mouse_pos)
            self.draw_button(self.map3_button_rect, self.map3_button_image, self.map3_button_hover_image, mouse_pos)
            self.draw_back_button(mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.main_menu.run()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.map1_button_rect.collidepoint(mouse_pos):
                        self.start_game('map1')
                        running = False
                    elif self.map2_button_rect.collidepoint(mouse_pos):
                        self.start_game('map2')
                        running = False
                    elif self.map3_button_rect.collidepoint(mouse_pos):
                        self.start_game('map3')
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

    def start_game(self, map_name):
        if map_name == 'map1':
            background_image_path = 'Assets/Bilder/Hintergrund/Background/BGSchnee.png'
        elif map_name == 'map2':
            background_image_path = 'Assets/Bilder/Hintergrund/Background/BGVulkan.png'
        elif map_name == 'map3':
            background_image_path = 'Assets/Bilder/Hintergrund/Background/BGSpace.png'
        else:
            background_image_path = 'Assets/Bilder/Hintergrund/Background/BGSchnee.png'  # Default

        # Launch the game with the selected map
        
        subprocess.Popen([sys.executable, 'game.py', map_name, background_image_path])
        pygame.quit()

class OptionsWindow:
    def __init__(self, main_menu, music_on):
        self.main_menu = main_menu
        self.music_on = music_on
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Options Window')

        # Load background image for options window
        self.background_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/OptionsBackground.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

        # Load and scale button images for music toggle and back button
        self.music_on_button_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/MusikAn.png')
        self.music_on_button_image = pygame.transform.scale(self.music_on_button_image, (400, 100))
        self.music_off_button_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/MusikAus.png')
        self.music_off_button_image = pygame.transform.scale(self.music_off_button_image, (400, 100))
        self.music_button_rect = self.music_on_button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

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

            # Draw music toggle button with appropriate image based on music state
            if self.music_on:
                self.screen.blit(self.music_on_button_image, self.music_button_rect.topleft)
            else:
                self.screen.blit(self.music_off_button_image, self.music_button_rect.topleft)

            # Draw back button with hover effect
            mouse_pos = pygame.mouse.get_pos()
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

    def draw_back_button(self, mouse_pos):
        if self.back_button_rect.collidepoint(mouse_pos):
            self.screen.blit(self.back_button_hover_image, self.back_button_rect.topleft)
        else:
            self.screen.blit(self.back_button_image, self.back_button_rect.topleft)

    def toggle_music(self):
        self.music_on = not self.music_on
        if self.music_on:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

if __name__ == '__main__':
    main_menu = MainMenu()
    main_menu.run()
