import pygame
import sys

pygame.init()

# Bildschirmabmessungen
screen_width = 1920
screen_height = 1050

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)

# Spielfeld erstellen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('1v1 Spiel')

# Spielergrößen
player_speed = 10

# Zielposition
goal_width = 30
goal_height = 30
goal_x = screen_width // 2 - goal_width // 2
goal_y = screen_height // 2 - goal_height // 2

# Schriftart
font_path = "Assets/Schrift/Pixellari.ttf"  # Pfad zur heruntergeladenen Schriftart
font = pygame.font.Font(font_path, 65)
font_button = pygame.font.Font(font_path, 50)

button_width = 300
button_height = 100
button_spacing = 10  # Abstand zwischen den Buttons
button_y = screen_height // 2
button_menu_x = screen_width // 2 - (1.5 * button_width + button_spacing)
button_neustart_x = screen_width // 2 - (0.5 * button_width)
button_quit_x = screen_width // 2 + (0.5 * button_width + button_spacing)

# Spielerbilder laden und skalieren
player1_image = pygame.image.load('Assets/Bilder/Spieler/Fisch.png')  # Pfad zum Bild von Spieler 1
player2_image = pygame.image.load('Assets/Bilder/Spieler/Fisch2.png')  # Pfad zum Bild von Spieler 2

# Neue Größe für die Spielerbilder
new_player_width = 250
new_player_height = 250

player1_image = pygame.transform.scale(player1_image, (new_player_width, new_player_height))
player2_image = pygame.transform.scale(player2_image, (new_player_width, new_player_height))
player_width, player_height = player1_image.get_size()

# Funktion zur Anzeige der Gewinnnachricht und Buttons
def display_winner(winner):
    winner_text = font.render(f"{winner} hat gewonnen!", True, BLACK)
    screen.fill(WHITE)
    screen.blit(winner_text, (screen_width // 2 - winner_text.get_width() // 2, screen_height // 4 - winner_text.get_height() // 2))

    # Buttons
    draw_buttons()

    pygame.display.flip()
    wait_for_click()

# Funktion zum Zeichnen der Buttons
def draw_buttons():
    mouse_x, mouse_y = pygame.mouse.get_pos()

    draw_button("Startmenü", button_menu_x, button_y, mouse_x, mouse_y)
    draw_button("Neustarten", button_neustart_x, button_y, mouse_x, mouse_y)
    draw_button("Quit", button_quit_x, button_y, mouse_x, mouse_y)

# Funktion zum Zeichnen eines Buttons
def draw_button(text, x, y, mouse_x, mouse_y):
    if x <= mouse_x <= x + button_width and y <= mouse_y <= y + button_height:
        pygame.draw.rect(screen, BLACK, (x, y, button_width, button_height))
        button_text = font_button.render(text, True, WHITE)
    else:
        pygame.draw.rect(screen, GRAY, (x, y, button_width, button_height))
        button_text = font_button.render(text, True, BLACK)

    screen.blit(button_text, (x + (button_width - button_text.get_width()) // 2, y + (button_height - button_text.get_height()) // 2))

# Funktion zum Warten auf einen Mausklick
def wait_for_click():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button_menu_x <= mouse_x <= button_menu_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    # Startmenü-Button
                    waiting = False
                    return
                elif button_neustart_x <= mouse_x <= button_neustart_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    # Neustarten-Button
                    waiting = False
                    return
                elif button_quit_x <= mouse_x <= button_quit_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    pygame.quit()
                    sys.exit()

        # Aktualisiere die Buttons, um den Hover-Effekt zu zeigen
        draw_buttons()
        pygame.display.flip()

# Hauptspielschleife
while True:
    player1_x = 100
    player1_y = 300

    player2_x = 1700
    player2_y = 300

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Tastendrücke erfassen
        keys = pygame.key.get_pressed()

        # Spieler 1 Steuerung (Pfeiltasten)
        if keys[pygame.K_LEFT]:
            player1_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player1_x += player_speed
        if keys[pygame.K_UP]:
            player1_y -= player_speed
        if keys[pygame.K_DOWN]:
            player1_y += player_speed

        # Spieler 2 Steuerung (WASD)
        if keys[pygame.K_a]:
            player2_x -= player_speed
        if keys[pygame.K_d]:
            player2_x += player_speed
        if keys[pygame.K_w]:
            player2_y -= player_speed
        if keys[pygame.K_s]:
            player2_y += player_speed

        screen.fill(WHITE)

        # Spieler zeichnen
        player1_rect = player1_image.get_rect(topleft=(player1_x, player1_y))
        player2_rect = player2_image.get_rect(topleft=(player2_x, player2_y))
        goal = pygame.Rect(goal_x, goal_y, goal_width, goal_height)

        screen.blit(player1_image, player1_rect)
        screen.blit(player2_image, player2_rect)
        pygame.draw.rect(screen, GREEN, goal)

        # Überprüfen, ob ein Spieler das Ziel erreicht hat
        if player1_rect.colliderect(goal):
            display_winner("Spieler 1")
            running = False
        if player2_rect.colliderect(goal):
            display_winner("Spieler 2")
            running = False

        pygame.display.flip()
        pygame.time.Clock().tick(30)
