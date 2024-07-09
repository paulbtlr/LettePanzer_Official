import pygame
import sys
from UI import UI
from Panzer import Panzer
from Boden import Boden
from shoot import Shoot
from MainMenue import MainMenu

def interpolate_color(start_color, end_color, factor):
    return (
        int(start_color[0] + (end_color[0] - start_color[0]) * factor),
        int(start_color[1] + (end_color[1] - start_color[1]) * factor),
        int(start_color[2] + (end_color[2] - start_color[2]) * factor)
    )


def main(map_selection, background_image_path):
    # Initialize Pygame
    pygame.init()

    # Set the dimensions of the window
    window_size = (1920, 1020)
    screen = pygame.display.set_mode(window_size)

    # Set the title of the window
    pygame.display.set_caption('BattleTanks')

    background = pygame.image.load(background_image_path)
    background = pygame.transform.scale(background, (window_size))
    # Initialise Clock
    clock = pygame.time.Clock()
    FPS = 60

    # Define colors
    clock = pygame.time.Clock()
    running = True
    LIGHT_BLUE = background_image_path
    TOP_COLOR = (255, 0, 255)
    BOTTOM_COLOR = (230, 230, 250)

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


    # Load All Panzers 
    # P1
    panzer_p1 = pygame.image.load("Assets/Bilder/Spieler/Panzer/P1.png")
    panzer_p1_rohr = pygame.image.load("Assets/Bilder/Spieler/Rohr/PR1.png")
    # P2
    panzer_p2 = pygame.image.load("Assets/Bilder/Spieler/Panzer/P2.png")
    panzer_p2_rohr = pygame.image.load("Assets/Bilder/Spieler/Rohr/PR2.png")
    # P3
    panzer_p3 = pygame.image.load("Assets/Bilder/Spieler/Panzer/P3.png")
    panzer_p3_rohr = pygame.image.load("Assets/Bilder/Spieler/Rohr/PR3.png")
    # P4
    panzer_p4 = pygame.image.load("Assets/Bilder/Spieler/Panzer/P4.png")
    panzer_p4_rohr = pygame.image.load("Assets/Bilder/Spieler/Rohr/PR4.png")
    # P5
    panzer_p5 = pygame.image.load("Assets/Bilder/Spieler/Panzer/P5.png")
    panzer_p5_rohr = pygame.image.load("Assets/Bilder/Spieler/Rohr/PR5.png")
    # P6
    panzer_p6 = pygame.image.load("Assets/Bilder/Spieler/Panzer/P6.png")
    panzer_p6_rohr = pygame.image.load("Assets/Bilder/Spieler/Rohr/PR6.png")

    # Initialize Panzer with a scale factor to make it smaller
    panzer_left = Panzer("Assets/Bilder/Spieler/Panzer/P1.png", (95, boden.get_ground_height(95)), panzer_p1_rohr, panzer_imagelist_blue_v, panzer_imagelist_blue_r, True, scale_factor=0.09) #0.08
    panzer_right = Panzer("Assets/Bilder/Spieler/Panzer/P6.png", (1722, boden.get_ground_height(1722)), panzer_p6_rohr, panzer_imagelist_orange_v, panzer_imagelist_orange_r, False, scale_factor=0.09)
    shoot = Shoot(panzer_left.position[0]+115, panzer_left.position[1]-28)

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
        screen.blit(background, (0,0))
        #screen.blit(background,(0,0))

        # Draw the terrain with multiple waves
        for x in range(window_size[0]):
            y = boden.get_ground_height(x - 51)
            factor = y / window_size[1]  # Calculate the factor based on y position
            color = interpolate_color(TOP_COLOR, BOTTOM_COLOR, factor)
            pygame.draw.line(screen, color, (x, y), (x, window_size[1]))

        # Update blue panzer position and angle, then draw
        panzer_right.move()
        #panzer_right.update_animation(screen)
        panzer_right.update_position(boden.get_ground_height(panzer_right.position[0]))
        panzer_right.update_rohr_position(boden.get_ground_height(panzer_right.position[0]))
        panzer_right.update_angle(boden.get_ground_slope(panzer_right.position[0]))
        panzer_right.draw_rohr(screen)
        panzer_right.rohr_setting(screen)
        panzer_right.draw_panzer(screen)

        # Update blue panzer position and angle, then draw
        panzer_left.move()
        #panzer_blu.update_animation(screen)
        panzer_left.update_position(boden.get_ground_height(panzer_left.position[0]))
        panzer_left.update_rohr_position(boden.get_ground_height(panzer_left.position[0]))
        panzer_left.update_angle(boden.get_ground_slope(panzer_left.position[0]))
        panzer_left.draw_rohr(screen)
        panzer_left.rohr_setting(screen)
        panzer_left.draw_panzer(screen)

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
        ui.draw_tank(panzer_left.tank,200,150,screen,True)
        ui.draw_tank(panzer_right.tank,1620,150,screen,False)
        ui.draw_health(panzer_left.health,100,100,screen,True)
        ui.draw_health(panzer_right.health,1620,100,screen,False)
        ui.draw()

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python game.py <map_selection> <background_image_path>")
        sys.exit(1)

    map_selection = sys.argv[1]
    background_image_path = sys.argv[2]
    main(map_selection, background_image_path)