import pygame
import sys
import math
import random
from UI import UI

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_size = (1920, 1020)
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('Lette Panzer')

# Define colors
LIGHT_BLUE = (50, 100, 255)
LIGHT_GRAY = (200, 200, 200)

# Initialize UI
ui = UI(screen)

# Define parameters for multiple waves
num_waves = 3
waves = []

for _ in range(num_waves):
    wave_length = random.randint(100, 400)
    amplitude = random.randint(10, 80)
    phase_shift = random.uniform(0, 2 * math.pi)
    waves.append((wave_length, amplitude, phase_shift))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Pass events to UI
        ui.update(event)

    # Fill the screen with a light blue color for the sky
    screen.fill(LIGHT_BLUE)

    # Draw the terrain with multiple waves
    for x in range(window_size[0]):
        y = 0
        for wave in waves:
            wave_length, amplitude, phase_shift = wave
            y += amplitude * math.sin(x / wave_length * 2 * math.pi + phase_shift)
        y = int(window_size[1] / 1.5 + y)
        pygame.draw.line(screen, LIGHT_GRAY, (x, y), (x, window_size[1]))

    # Draw UI buttons
    ui.draw()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
