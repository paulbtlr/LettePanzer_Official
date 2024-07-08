import pygame
import sys
from UI import UI
from Panzer import Panzer
from Boden import Boden
from shoot import Shoot

def main():
    # Initialize Pygame
    pygame.init()

    # Set the dimensions of the window
    window_size = (1920, 1020)
    screen = pygame.display.set_mode(window_size)

    # Set the title of the window
    pygame.display.set_caption('BattleTanks')

    # Initialise Clock
    clock = pygame.time.Clock()
    FPS = 60

    # Define colors
    LIGHT_BLUE = (50, 100, 255)
    PERU = (0, 0, 0)

    # Initialize Imports
    ui = UI(screen)
    boden = Boden()
    #Load Background
    #background = pygame.image.load("Assets/Bilder/Hintergrund/Background/BGChopper.png")
    
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
    panzer_blu = Panzer("Assets/Bilder/Spieler/Panzer/Blau/BBR/BBR0.png", (95, boden.get_ground_height(95)), panzer_blue_rohr, panzer_imagelist_blue_v, panzer_imagelist_blue_r, True, scale_factor=0.09) #0.08
    panzer_or = Panzer("Assets/Bilder/Spieler/Panzer/Orange/OBR/OBR0.png", (1722, boden.get_ground_height(1722)), panzer_orange_rohr, panzer_imagelist_orange_v, panzer_imagelist_orange_r, False, scale_factor=0.09)
    shoot = Shoot(panzer_blu.position[0]+115, panzer_blu.position[1]-28)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Pass events to UI
            ui.update(event)

            
        clock.tick(FPS)

        # Fill the screen with a light blue color for the sky
        screen.fill(LIGHT_BLUE)
        #screen.blit(background,(0,0))

        # Draw the terrain with multiple waves
        for x in range(window_size[0]):
            y = boden.get_ground_height(x - 51)
            pygame.draw.line(screen, PERU, (x, y), (x, window_size[1]))

        # Update blue panzer position and angle, then draw
        panzer_or.move()
        panzer_or.update_animation(screen)
        panzer_or.update_position(boden.get_ground_height(panzer_or.position[0]))
        panzer_or.update_rohr_position(boden.get_ground_height(panzer_or.position[0]))
        panzer_or.update_angle(boden.get_ground_slope(panzer_or.position[0]))
        panzer_or.draw_rohr(screen)
        panzer_or.draw_panzer(screen)

        # Update blue panzer position and angle, then draw
        panzer_blu.move()
        panzer_blu.update_animation(screen)
        panzer_blu.update_position(boden.get_ground_height(panzer_blu.position[0]))
        panzer_blu.update_rohr_position(boden.get_ground_height(panzer_blu.position[0]))
        panzer_blu.update_angle(boden.get_ground_slope(panzer_blu.position[0]))
        panzer_blu.draw_rohr(screen)
        panzer_blu.rohr_setting(screen)
        panzer_blu.draw_panzer(screen)

        shoot.move()
        shoot.update_shoot()
        shoot.draw(screen)
    # Load the Interface image
        interface_image = pygame.image.load("Assets/Bilder/Interface/Interface.png")
        
        # Draw the Interface image on top
        screen.blit(interface_image, (0, -51))
        
        # Update the display again to show the Interface image
        pygame.display.flip()
        # Draw UI buttons
        ui.draw_tank(panzer_blu.tank,200,150,screen,True)
        ui.draw_tank(panzer_or.tank,1620,150,screen,False)
        ui.draw_health(panzer_blu.health,100,100,screen,True)
        ui.draw_health(panzer_or.health,1620,100,screen,False)
        ui.draw()

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
    
    

