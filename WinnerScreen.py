import pygame
import sys

# Pygame initialisieren
pygame.init()

# Bildschirmabmessungen
screen_width = 1920
screen_height = 1050

# Farben definieren
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Spielfeld erstellen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('1v1 Spiel')

# Spielergrößen und -positionen
player_width = 50
player_height = 60
player_speed = 10

# Zielposition und -größe
goal_width = 30
goal_height = 30
goal_x = screen_width // 2 - goal_width // 2
goal_y = screen_height // 2 - goal_height // 2

# Schriftart für den Siegtext
font_path = "Assets\Schrift\Pixellari.ttf"  # Pfad zur heruntergeladenen Schriftart
font = pygame.font.Font(font_path, 65)

# Funktion zur Anzeige der Gewinnnachricht
def display_winner(winner):
    winner_text = font.render(f"{winner} hat gewonnen!", True, BLACK)
    screen.fill(WHITE)
    screen.blit(winner_text, (screen_width // 2 - winner_text.get_width() // 2, screen_height // 4 - winner_text.get_height() // 2))
    pygame.display.flip()
    wait_for_key()

# Funktion zum Warten auf eine Tasteneingabe
def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Hauptspielschleife
while True:
    player1_x = 100
    player1_y = 300

    player2_x = 650
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
        
        # Bildschirm mit weißem Hintergrund füllen
        screen.fill(WHITE)
        
        # Spieler zeichnen
        player1 = pygame.Rect(player1_x, player1_y, player_width, player_height)
        player2 = pygame.Rect(player2_x, player2_y, player_width, player_height)
        goal = pygame.Rect(goal_x, goal_y, goal_width, goal_height)
        
        pygame.draw.rect(screen, RED, player1)
        pygame.draw.rect(screen, BLUE, player2)
        pygame.draw.rect(screen, GREEN, goal)
        
        # Überprüfen, ob ein Spieler das Ziel erreicht hat
        if player1.colliderect(goal):
            display_winner("Spieler 1")
            running = False
        if player2.colliderect(goal):
            display_winner("Spieler 2")
            running = False
        
        # Bildschirm aktualisieren
        pygame.display.flip()
        
        # Framerate setzen
        pygame.time.Clock().tick(30)
