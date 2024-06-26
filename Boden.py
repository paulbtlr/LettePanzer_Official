import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('ShellShock Live Style')

# Define colors
GREY = (128, 128, 128)
BLUE = (0, 0, 255)

# Define terrain
terrain_points = [(0, 400), (100, 350), (200, 370), (300, 360), (400, 400), (500, 380), (600, 360), (700, 370), (800, 350), (800, 600), (0, 600)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a sky blue color
    screen.fill(BLUE)

    # Draw the terrain
    pygame.draw.polygon(screen, GREY, terrain_points)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
