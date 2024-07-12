import pygame
import math
import shoot
"""
Definiert eine Panzer-Klasse, um Panzer-Objekte zu erstellen und zu verwalten
"""
class Panzer:
    def __init__(self, image_path, start_position, panzer_rohr, flip, scale_factor):
        self.original_image = pygame.image.load(image_path)  # Lädt das Bild des Panzers
        self.original_panzerrohr = panzer_rohr  # Speichert das Originalbild des Panzerrohrs
        # Skaliert das Panzerbild basierend auf dem Skalierungsfaktor
        self.image = pygame.transform.scale(self.original_image, 
                                            (int(self.original_image.get_width() * scale_factor), 
                                             int(self.original_image.get_height() * scale_factor)))
        # Skaliert das Panzerrohrbild basierend auf dem Skalierungsfaktor
        self.rohr_image = pygame.transform.scale(self.original_panzerrohr, 
                                            (int(self.original_panzerrohr.get_width() * scale_factor), 
                                             int(self.original_panzerrohr.get_height() * scale_factor)))      
        self.rotated_rohr = 0  # rotierte Panzerrohr
        self.position = list(start_position)  # Startposition des Panzers
        self.scale_factor = scale_factor  # Speichert den Skalierungsfaktor
        self.flip = flip  # Ausrichtung des Panzers (True für Player 1, False für Player 2)
        self.angle = 0  # Initialisiert den Winkel des Panzers
        self.speed = 2  # Geschwindigkeit des Panzers
        self.tank = 2000  # maximale Bewegungsdistanz des Panzers
        self.health = 100  # Gesundheit des Panzers
        self.armor = 50  # Panzerung des Panzers
        self.move_right = False  # Bewegung nach rechts
        self.move_left = False  # Bewegung nach links
        self.aiming = False  # Zielmodus
        self.descending_rohr = False  # Senken des Rohrs
        self.ascending_rohr = False  # Heben des Rohrs
        self.frame = 0  # Animationsframe
        #self.image_list_v = image_list_v
        #self.image_list_r = image_list_r
        self.rohr_degree = 0  # Winkel des Rohrs
        self.rohr_angle = 0  # Winkel des Rohrs

    """
    Zeichnet den Panzer auf der angegebenen Oberfläche
    """
    def draw_panzer(self, surface):
        # Spieler 1: Flipt das Bild, rotiert es und zeichnet es
        if self.flip == True:
            img = pygame.transform.flip(self.image, True, False)
            rotated_image = pygame.transform.rotate(img, self.angle)
            new_rect2 = rotated_image.get_rect(center=self.image.get_rect(topleft=self.position).center)
            surface.blit(rotated_image, new_rect2.topleft)
        # Spieler 2: Rotiert das Bild und zeichnet es
        else:
            rotated_image = pygame.transform.rotate(self.image, self.angle)
            new_rect2 = rotated_image.get_rect(center=self.image.get_rect(topleft=self.position).center)
            surface.blit(rotated_image, new_rect2.topleft)
    
    """
    Zeichnet das Panzerrohr auf der angegebenen Oberfläche
    """
    def draw_rohr(self, surface):
        if self.aiming == False:

            # Spieler 1: Flipt das Rohr, rotiert es und zeichnet es
            if self.flip == True:
                rohr = pygame.transform.flip(self.rohr_image, True, False)
                self.rotated_rohr = pygame.transform.rotate(rohr, self.angle)
                # new_rect = self.rotated_rohr.get_rect(center=self.rohr_image.get_rect(topleft=self.position).center)
                # surface.blit(self.rotated_rohr, new_rect.topleft)

            # Spieler 2: Rotiert das Rohr und zeichnet es
            else:
                self.rotated_rohr = pygame.transform.rotate(self.rohr_image, self.angle)
            new_rect = self.rotated_rohr.get_rect(center=self.rohr_image.get_rect(topleft=self.position).center)
            surface.blit(self.rotated_rohr, new_rect.topleft)

        else:

            # Spieler 1: Rohrsteuerung im Zielmodus
            if self.flip == True:
                rohr = pygame.transform.flip(self.rohr_image, True, False)
                if self.ascending_rohr == True:
                    # Flipt das Rohr, rotiert es und zeichnet es
                    self.rotated_rohr = pygame.transform.rotate(rohr, -(self.rohr_angle - self.angle))

                elif self.descending_rohr == True:
                    # Flipt das Rohr, rotiert es und zeichnet es
                    self.rotated_rohr = pygame.transform.rotate(rohr, (self.angle - self.rohr_angle))
                new_rect = self.rotated_rohr.get_rect(center=self.rohr_image.get_rect(topleft=self.position).center)
                surface.blit(self.rotated_rohr, new_rect.topleft)

            # Spieler 2: Rohrsteuerung im Zielmodus
            else:
                if self.ascending_rohr == True:
                    self.rotated_rohr = pygame.transform.rotate(self.rohr_image, -(self.rohr_angle - self.angle))

                elif self.descending_rohr == True:
                    self.rotated_rohr = pygame.transform.rotate(self.rohr_image, (self.angle - self.rohr_angle))

                new_rect = self.rotated_rohr.get_rect(center=self.rohr_image.get_rect(topleft=self.position).center)
                surface.blit(self.rotated_rohr, new_rect.topleft)

    """
    Bewegt den Panzer basierend auf den Tastatureingaben
    """
    def move(self):
        key = pygame.key.get_pressed()
        self.move_left = False
        self.move_right = False

        # Spieler 1: 
        if self.flip == True:

            # Bewegung nach links
            #Left Movement: Drives until Self.Tank == 0
            if (key[pygame.K_a]) and (self.tank >= 0):
                self.position[0] -= self.speed
                self.tank -= self.speed
                self.move_left = True
                self.move_right = False

                if self.tank < 0:
                    self.tank == 0

            # Bewegung nach rechts
            #Right Movement: Drives until Self.Tank == 0
            if (key[pygame.K_d]) and (self.tank >= 0):
                self.position[0] += self.speed
                self.tank -= self.speed
                self.move_left = False
                self.move_right = True

                if self.tank < 0:
                    self.tank == 0

        # Spieler 2:
        elif self.flip == False:

            # Bewegung nach links
            #Left Movement: Drives until Self.Tank == 0
            if (key[pygame.K_LEFT]) and (self.tank >= 0):
                self.position[0] -= self.speed
                self.tank -= self.speed
                self.move_left = True
                self.move_right = False

                if self.tank < 0:
                    self.tank == 0

            # Bewegung nach rechts
            #Right Movement: Drives until Self.Tank == 0
            if (key[pygame.K_RIGHT]) and (self.tank >= 0):
                self.position[0] += self.speed
                self.tank -= self.speed
                self.move_left = False
                self.move_right = True

                if self.tank < 0:
                    self.tank == 0

    # def update_animation(self, surface):
    #     #Player 1
    #     if self.flip == True:
    #         #Animation for driving forward
    #         if self.move_right == True:
    #             if self.frame <= 7:
    #                 self.current_image = self.image_list_v[self.frame]
    #                 self.image = pygame.transform.scale(self.current_image, 
    #                                                 (int(self.current_image.get_width() * self.scale_factor), 
    #                                                 int(self.current_image.get_height() * self.scale_factor)))
    #                 img = pygame.transform.flip(self.image, True, False)
    #                 rotated_image = pygame.transform.rotate(img, self.angle)
    #                 new_rect2 = rotated_image.get_rect(center=self.image.get_rect(topleft=self.position).center)
    #                 surface.blit(rotated_image, new_rect2.topleft)
    #             self.frame += 1
    #             if self.frame > 6:
    #                 self.frame = 0

    #         #Animation for driving backwards
    #         if self.move_left == True:
    #             if self.frame <= 7:
    #                 self.current_image = self.image_list_r[self.frame]
    #                 self.image = pygame.transform.scale(self.current_image, 
    #                                                 (int(self.current_image.get_width() * self.scale_factor), 
    #                                                 int(self.current_image.get_height() * self.scale_factor)))
    #                 img = pygame.transform.flip(self.image, True, False)
    #                 rotated_image = pygame.transform.rotate(img, self.angle)
    #                 new_rect2 = rotated_image.get_rect(center=self.image.get_rect(topleft=self.position).center)
    #                 surface.blit(rotated_image, new_rect2.topleft)
    #             self.frame += 1    
    #             if self.frame > 6:
    #                 self.frame = 0
    #     #Player 2
    #     else:
    #         #Animation for driving forward
    #         if self.move_right == True:
    #             if self.frame <= 7:
    #                 self.current_image = self.image_list_v[self.frame]
    #                 self.image = pygame.transform.scale(self.current_image, 
    #                                                 (int(self.current_image.get_width() * self.scale_factor), 
    #                                                 int(self.current_image.get_height() * self.scale_factor)))
    #                 rotated_image = pygame.transform.rotate(self.image, self.angle)
    #                 new_rect2 = rotated_image.get_rect(center=self.image.get_rect(topleft=self.position).center)
    #                 surface.blit(rotated_image, new_rect2.topleft)
    #             self.frame += 1
    #             if self.frame > 6:
    #                 self.frame = 0

    #         #Animation for driving backwards
    #         if self.move_left == True:
    #             if self.frame <= 7:
    #                 self.current_image = self.image_list_r[self.frame]
    #                 self.image = pygame.transform.scale(self.current_image, 
    #                                                 (int(self.current_image.get_width() * self.scale_factor), 
    #                                                 int(self.current_image.get_height() * self.scale_factor)))
    #                 rotated_image = pygame.transform.rotate(self.image, self.angle)
    #                 new_rect2 = rotated_image.get_rect(center=self.image.get_rect(topleft=self.position).center)
    #                 surface.blit(rotated_image, new_rect2.topleft)
    #             self.frame += 1    
    #             if self.frame > 6:
    #                 self.frame = 0

    """ 
    Update stuff
    """
    def update_position(self, ground_height):
        # Aktualisiert die Position des Panzers basierend auf der Bodenhöhe
        self.position[1] = ground_height - self.image.get_height() + 14

    def update_rohr_position(self, ground_height):
        # Aktualisiert die Position des Panzerrohrs basierend auf der Bodenhöhe
        self.position[1] = ground_height - self.rohr_image.get_height() + 14

    def update_angle(self, ground_slope):
        # Aktualisiert den Winkel des Panzers basierend auf der Bodenneigung
        self.angle = -math.degrees(math.atan(ground_slope))

    """ 
    Stellt den Winkel des Panzerrohrs basierend auf den Tastatureingaben ein
    """
    def rohr_setting(self, surface):
        key = pygame.key.get_pressed()
        ANGLE_SPEED = 1
        if self.flip == True:
            if key[pygame.K_w] == True:
                self.descending_rohr = False
                self.ascending_rohr = True
                self.aiming = True
                self.rohr_angle -= ANGLE_SPEED
                self.rohr_degree += ANGLE_SPEED
                if self.rohr_degree >= 45:
                    self.rohr_angle = -45
                    self.rohr_degree = 45

            if key[pygame.K_s]:
                self.ascending_rohr = False
                self.descending_rohr = True
                #Flips the Rohr, Rotates it and draws it
                self.aiming = True
                self.rohr_angle += ANGLE_SPEED
                self.rohr_degree -= ANGLE_SPEED
                if self.rohr_degree <= 0:
                    self.rohr_angle = 0
                    self.rohr_degree = 0
        #Player 2
        else:
            if key[pygame.K_UP] == True:
                self.descending_rohr = False
                self.ascending_rohr = True
                self.aiming = True
                self.rohr_angle += ANGLE_SPEED
                self.rohr_degree -= ANGLE_SPEED
                print(self.rohr_angle)
                print(self.rohr_degree)
                if self.rohr_degree <= -45:
                    self.rohr_angle = 45
                    self.rohr_degree = -45

                    #self.rotated_rohr = pygame.transform.rotate(rohr, (self.rohr_angle - self.angle))
                    #new_rect = self.rotated_rohr.get_rect(center=self.rohr_image.get_rect(topleft=self.position).center)
                    #surface.blit(self.rotated_rohr, new_rect.topleft)

            #Player 2
            if key[pygame.K_DOWN] == True:
                self.ascending_rohr = False
                self.descending_rohr = True
                self.aiming = True
                self.rohr_angle -= ANGLE_SPEED
                self.rohr_degree += ANGLE_SPEED
                print(self.rohr_angle)
                print(self.rohr_degree)
                if self.rohr_degree >= 0:
                    self.rohr_angle = 0
                    self.rohr_degree = 0

                #self.rotated_rohr = pygame.transform.rotate(rohr, (self.rohr_angle - self.angle))
                #new_rect = self.rotated_rohr.get_rect(center=self.rohr_image.get_rect(topleft=self.position).center)
                #surface.blit(self.rotated_rohr, new_rect.topleft)

    #def update_rohr_angle(self):
     #   self.rohr_angle = -math.degrees(math.atan(ground_slope))
