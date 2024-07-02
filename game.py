import pygame
import sys
import math
import random
from UI import UI
from Panzer import Panzer
from Boden import Boden

def main():
    # Initialize Pygame
    pygame.init()

    # Set the dimensions of the window
    window_size = (1920, 1020)
    screen = pygame.display.set_mode(window_size)

    # Set the title of the window
    pygame.display.set_caption('BattleTanks')

    # Define colors
    LIGHT_BLUE = (50, 100, 255)
    PERU = (205, 133, 63)

    # Initialize Imports
    ui = UI(screen)
    boden = Boden()

    # Define parameters for multiple waves

    # Load Panzer Pictures for Blue Panzer
    panzer_imagelist_blue_v = [pygame.image.load("Assets/Bilder/Spieler/Panzer/Blau/BBV/BBV0.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Blau/BBV/BBV1.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Blau/BBV/BBV2.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Blau/BBV/BBV3.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Blau/BBV/BBV4.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Blau/BBV/BBV5.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Blau/BBV/BBV6.png")]

    panzer_imagelist_blue_r = [pygame.image.load("Assets/Bilder/Spieler/Panzer/Blau/BBR/BBR0.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Blau/BBR/BBR1.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Blau/BBR/BBR2.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Blau/BBR/BBR3.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Blau/BBR/BBR4.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Blau/BBR/BBR5.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Blau/BBR/BBR6.png")]

    panzer_blue_rohr = pygame.image.load("Assets/Bilder/Spieler/Panzer/Blau/BSR.png")

    # Load Panzer Pictures for Orange Panzer
    panzer_imagelist_orange_v = [pygame.image.load("Assets/Bilder/Spieler/Panzer/Orange/OBV/OBV0.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Orange/OBV/OBV1.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Orange/OBV/OBV2.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Orange/OBV/OBV3.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Orange/OBV/OBV4.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Orange/OBV/OBV5.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Orange/OBV/OBV6.png")]

    panzer_imagelist_orange_r = [pygame.image.load("Assets/Bilder/Spieler/Panzer/Orange/OBR/OBR0.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Orange/OBR/OBR1.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Orange/OBR/OBR2.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Orange/OBR/OBR3.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Orange/OBR/OBR4.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Orange/OBR/OBR5.png"),
                                pygame.image.load("Assets/Bilder/Spieler/Panzer/Orange/OBR/OBR6.png")]

    panzer_orange_rohr = pygame.image.load("Assets/Bilder/Spieler/Panzer/Orange/OSR.png")

    # Initialize Panzer with a scale factor to make it smaller
    panzer = Panzer("Assets/Bilder/Spieler/Panzer/Blau/BBR/BBR0.png", (95, boden.get_ground_height(95)), panzer_blue_rohr,panzer_imagelist_blue_v,scale_factor=0.08)

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
            y = boden.get_ground_height(x - 50)
            pygame.draw.line(screen, PERU, (x, y), (x, window_size[1]))



        # Update panzer position and angle, then draw
        panzer.move()
        panzer.update_position(boden.get_ground_height(panzer.position[0]))
        panzer.update_rohr_position(boden.get_ground_height(panzer.position[0]))
        panzer.update_angle(boden.get_ground_slope(panzer.position[0]))
        panzer.draw_rohr(screen)
        panzer.draw_panzer(screen)

        # Draw UI buttons
        ui.draw_tank(panzer.tank,200,150,screen,True)
        ui.draw_tank(panzer.tank,1620,150,screen,False)
        ui.draw_health(panzer.health,100,100,screen,True)
        ui.draw_health(panzer.health,1620,100,screen,False)
        ui.draw()

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
