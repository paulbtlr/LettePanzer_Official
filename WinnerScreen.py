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

# Spielergröße
player_speed = 10

# Zielposition
goal_width = 30
goal_height = 30
goal_x = screen_width // 2 - goal_width // 2
goal_y = screen_height // 2 - goal_height // 2

# Schriftart
font_path = "Assets/Schrift/Pixellari.ttf"
font = pygame.font.Font(font_path, 65)
font_button = pygame.font.Font(font_path, 50)

# Neue Button-Größe
button_width = 300
button_height = 75
button_spacing = 20
button_y = screen_height // 1.2
button_menu_x = screen_width // 2 - (1.5 * button_width + button_spacing)
button_neustart_x = screen_width // 2 - (0.5 * button_width)
button_quit_x = screen_width // 2 + (0.5 * button_width + button_spacing)

# Spielerbilder
player1_image = pygame.image.load('Assets/Bilder/Spieler/Panzer/Blau/BWS.png')
player2_image = pygame.image.load('Assets/Bilder/Spieler/Panzer/Orange/OWS.png')

new_player_width = 640
new_player_height = 360

player1_image = pygame.transform.scale(player1_image, (new_player_width, new_player_height))
player2_image = pygame.transform.scale(player2_image, (new_player_width, new_player_height))
player_width, player_height = player1_image.get_size()

# Hintergrundbilder für den Winner Screen laden
background_player1_win = pygame.image.load('Assets/Bilder/Hintergrund/WinnerScreen/Spieler1.jpg')
background_player2_win = pygame.image.load('Assets/Bilder/Hintergrund/WinnerScreen/Spieler2.jpg')

# Bilder für den Winner Screen laden
winner_screen_image_player1 = pygame.image.load('Assets/Bilder/Spieler/Panzer/Blau/BWS_Sieg.png')
winner_screen_image_player2 = pygame.image.load('Assets/Bilder/Spieler/Panzer/Orange/OWS_Sieg.png')

winner_screen_image_player1 = pygame.transform.scale(winner_screen_image_player1, (new_player_width, new_player_height))
winner_screen_image_player2 = pygame.transform.scale(winner_screen_image_player2, (new_player_width, new_player_height))

# Button-Bilder laden und skalieren
startmenu_button_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Startmenü1.png')
startmenu_button_hover_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Startmenü2.png')
neustarten_button_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Neustarten1.png')
neustarten_button_hover_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Neustarten2.png')
quit_button_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Quit1.png')
quit_button_hover_image = pygame.image.load('Assets/Bilder/Hintergrund/Menü/Quit2.png')

startmenu_button_image = pygame.transform.scale(startmenu_button_image, (button_width, button_height))
startmenu_button_hover_image = pygame.transform.scale(startmenu_button_hover_image, (button_width, button_height))
neustarten_button_image = pygame.transform.scale(neustarten_button_image, (button_width, button_height))
neustarten_button_hover_image = pygame.transform.scale(neustarten_button_hover_image, (button_width, button_height))
quit_button_image = pygame.transform.scale(quit_button_image, (button_width, button_height))
quit_button_hover_image = pygame.transform.scale(quit_button_hover_image, (button_width, button_height))

# Funktion zur Anzeige des Winner Screens
def display_winner(winner, winner_image, background_image):
    screen.blit(background_image, (0, 0))  # Hintergrundbild zeichnen
    screen.blit(winner_image, (screen_width // 2 - winner_image.get_width() // 2, screen_height // 2 - winner_image.get_height() // 2))  # Gewinnerbild zeichnen

    # Buttons
    draw_buttons()

    pygame.display.flip()
    wait_for_click()

# Funktion zum Zeichnen der Buttons
def draw_buttons(selected_button=None):
    mouse_x, mouse_y = pygame.mouse.get_pos()

    draw_button(startmenu_button_image, startmenu_button_hover_image, button_menu_x, button_y, mouse_x, mouse_y, selected_button == 0)
    draw_button(neustarten_button_image, neustarten_button_hover_image, button_neustart_x, button_y, mouse_x, mouse_y, selected_button == 1)
    draw_button(quit_button_image, quit_button_hover_image, button_quit_x, button_y, mouse_x, mouse_y, selected_button == 2)

# Funktion zum Zeichnen eines Buttons
def draw_button(image, hover_image, x, y, mouse_x, mouse_y, selected):
    if selected or (x <= mouse_x <= x + button_width and y <= mouse_y <= y + button_height):
        screen.blit(hover_image, (x, y))
    else:
        screen.blit(image, (x, y))

# Funktion zum Warten auf einen Mausklick oder Tastendruck
def wait_for_click():
    selected_button = 0
    button_count = 3
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if selected_button == 0:
                        # Startmenü-Button
                        waiting = False
                        return
                    elif selected_button == 1:
                        # Neustarten-Button
                        waiting = False
                        return
                    elif selected_button == 2:
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_RIGHT:
                    selected_button = (selected_button + 1) % button_count
                elif event.key == pygame.K_LEFT:
                    selected_button = (selected_button - 1) % button_count

        # Aktualisiere die Buttons, um den Hover-Effekt und die Tastennavigation zu zeigen
        draw_buttons(selected_button)
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
            display_winner("Spieler 1", winner_screen_image_player1, background_player1_win)
            running = False
        if player2_rect.colliderect(goal):
            display_winner("Spieler 2", winner_screen_image_player2, background_player2_win)
            running = False

        pygame.display.flip()
        pygame.time.Clock().tick(30)
