import pygame
import math
import shoot

class Panzer:
    def __init__(self, image_path, start_position, panzer_rohr,flip,scale_factor):
        self.original_image = pygame.image.load(image_path)
        self.original_panzerrohr = panzer_rohr
        self.image = pygame.transform.scale(self.original_image, 
                                            (int(self.original_image.get_width() * scale_factor), 
                                             int(self.original_image.get_height() * scale_factor)))

        self.rohr_image = pygame.transform.scale(self.original_panzerrohr, 
                                            (int(self.original_panzerrohr.get_width() * scale_factor), 
                                             int(self.original_panzerrohr.get_height() * scale_factor)))      
        self.rotated_rohr = 0
        self.position = list(start_position)
        self.scale_factor = scale_factor
        self.flip = flip
        self.angle = 0
        self.speed = 2
        self.tank = 2000 #The Maximum Movement a Tank can move
        self.health = 100 #The Health of a Tank
        self.armor = 50
        self.move_right = False
        self.move_left = False
        self.aiming = False
        self.descending_rohr = False
        self.ascending_rohr = False
        self.frame = 0
        #self.image_list_v = image_list_v
        #self.image_list_r = image_list_r
        self.rohr_degree = 0
        self.rohr_angle = 0

    def draw_panzer(self, surface):
        #Player 1
        if self.flip == True:
            
            #Flips the Rohr, Rotates it and draws it
            img = pygame.transform.flip(self.image, True, False)
            rotated_image = pygame.transform.rotate(img, self.angle)
            new_rect2 = rotated_image.get_rect(center=self.image.get_rect(topleft=self.position).center)
            surface.blit(rotated_image, new_rect2.topleft)
        #Player 2
        else:
            #Rotates it and draws it
            rotated_image = pygame.transform.rotate(self.image, self.angle)
            new_rect2 = rotated_image.get_rect(center=self.image.get_rect(topleft=self.position).center)
            surface.blit(rotated_image, new_rect2.topleft)

    def draw_rohr(self, surface):
        if self.aiming == False:
            #Player 1
            if self.flip == True:
                #Flips the Rohr, Rotates it and draws it
                rohr = pygame.transform.flip(self.rohr_image, True, False)
                self.rotated_rohr = pygame.transform.rotate(rohr, self.angle)
                # new_rect = self.rotated_rohr.get_rect(center=self.rohr_image.get_rect(topleft=self.position).center)
                # surface.blit(self.rotated_rohr, new_rect.topleft)
            #Player 2
            else:
                #Rotates it and draws it
                self.rotated_rohr = pygame.transform.rotate(self.rohr_image, self.angle)
            new_rect = self.rotated_rohr.get_rect(center=self.rohr_image.get_rect(topleft=self.position).center)
            surface.blit(self.rotated_rohr, new_rect.topleft)



        else:
            #Player 1
            if self.flip == True:
                rohr = pygame.transform.flip(self.rohr_image, True, False)
                if self.ascending_rohr == True:
                    #Flips the Rohr, Rotates it and draws it
                    self.rotated_rohr = pygame.transform.rotate(rohr, -(self.rohr_angle - self.angle))


                elif self.descending_rohr == True:
                    #Flips the Rohr, Rotates it and draws it
                    self.rotated_rohr = pygame.transform.rotate(rohr, (self.angle - self.rohr_angle))

                new_rect = self.rotated_rohr.get_rect(center=self.rohr_image.get_rect(topleft=self.position).center)
                surface.blit(self.rotated_rohr, new_rect.topleft)

                #Player 2
            else:
                if self.ascending_rohr == True:
                    self.rotated_rohr = pygame.transform.rotate(self.rohr_image, -(self.rohr_angle - self.angle))

                elif self.descending_rohr == True:
                    self.rotated_rohr = pygame.transform.rotate(self.rohr_image, (self.angle - self.rohr_angle))

                new_rect = self.rotated_rohr.get_rect(center=self.rohr_image.get_rect(topleft=self.position).center)
                surface.blit(self.rotated_rohr, new_rect.topleft)

    def move(self):
        key = pygame.key.get_pressed()
        self.move_left = False
        self.move_right = False

        #Player 1
        if self.flip == True:
            #Left Movement: Drives until Self.Tank == 0
            if (key[pygame.K_a]) and (self.tank >= 0):
                self.position[0] -= self.speed
                self.tank -= self.speed
                self.move_left = True
                self.move_right = False

                if self.tank < 0:
                    self.tank == 0

            #Right Movement: Drives until Self.Tank == 0
            if (key[pygame.K_d]) and (self.tank >= 0):
                self.position[0] += self.speed
                self.tank -= self.speed
                self.move_left = False
                self.move_right = True

                if self.tank < 0:
                    self.tank == 0
        #Player 2
        elif self.flip == False:
            #Left Movement: Drives until Self.Tank == 0
            if (key[pygame.K_LEFT]) and (self.tank >= 0):
                self.position[0] -= self.speed
                self.tank -= self.speed
                self.move_left = True
                self.move_right = False

                if self.tank < 0:
                    self.tank == 0

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

    def update_position(self, ground_height):
        #keeps the tank in place......
        self.position[1] = ground_height - self.image.get_height() + 14

    def update_rohr_position(self, ground_height):
        #keeps the rohr in place
        self.position[1] = ground_height - self.rohr_image.get_height() + 14

    def update_angle(self, ground_slope):
        #Angles the tank to drive slopes
        self.angle = -math.degrees(math.atan(ground_slope))

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
