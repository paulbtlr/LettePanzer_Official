import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_size = (1200, 800)
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('Lette Panzer')

# Define colors
LIGHT_BLUE = (50, 100, 255)
LIGHT_GRAY = (200, 200, 200)

# Define wave parameters
wave_length = 100  # Wellenlänge der Welle
amplitude = 50     # Amplitude der Welle
speed = 0.1        # Geschwindigkeit der Welle

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a light blue color for the sky
    screen.fill(LIGHT_BLUE)

    # Draw the terrain with waves
    for x in range(window_size[0]):
        # Berechne die y-Position auf Basis einer Sinus-Funktion für eine Welle
        y = int(window_size[1] / 2 + amplitude * math.sin(x / wave_length * 2 * math.pi ))

        # Zeichne von der berechneten y-Position bis zum unteren Rand des Fensters in LIGHT_GRAY
        pygame.draw.line(screen, LIGHT_GRAY, (x, y), (x, window_size[1]))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
