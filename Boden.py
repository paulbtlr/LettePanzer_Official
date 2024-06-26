import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_size = (1200, 800)
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('Lette Panzer')

# Define colors
GRAY = (128, 128, 128)
BLUE = (50, 100, 255)

# Define terrain
terrain_points = [
    (0, 600), (150, 550), (300, 570), (450, 560), 
    (600, 600), (750, 580), (900, 560), (1050, 570), 
    (1200, 550), (1200, 800), (0, 800)
]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a gray color
    screen.fill(BLUE)

    # Draw the terrain in light gray
    pygame.draw.polygon(screen, GRAY, terrain_points)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
