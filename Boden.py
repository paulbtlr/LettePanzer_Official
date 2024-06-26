import pygame
import sys
import math
import random

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
wave_length = 200  # Wellenlänge der Welle
#min_amplitude = 10  # Minimale Amplitude
#max_amplitude = 80  # Maximale Amplitude
amplitude = 50
# Function to calculate amplitude based on x position
#def calculate_amplitude(x):
#    return random.randint(min_amplitude, max_amplitude)

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
        #amplitude = calculate_amplitude(x)
        y = int(window_size[1] / 2 + amplitude * math.sin(x / wave_length * 2 * math.pi))
        pygame.draw.line(screen, LIGHT_GRAY, (x, y), (x, window_size[1]))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
