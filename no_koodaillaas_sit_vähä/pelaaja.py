import pygame
from pygame_functions import *
from kirjanpito import Kirjanpito




class Pelaaja(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Pelaaja, self).__init__()
        self.image_get = pygame.image.load("lisatarvikkeet/pallo.png").convert_alpha()
        self.image = pygame.transform.scale(self.image_get, (100, 100))

        self.rect = self.image.get_rect(topleft=pos)
        self.elamat = 3
        self.elossa = True
        self.kp = Kirjanpito()
        self.kp.rivin_tulostus()









    def set_pos(self, x_pos, y_pos):
        self.rect.x = x_pos
        self.rect.y = y_pos




    def get_input(self):
        nappaimet = pygame.key.get_pressed()
        print(self.kp.laatan_posX, self.kp.laatan_posY)





        if nappaimet[pygame.K_d]:
            if self.kp.laatan_puoli == "oikea":
                self.set_pos(self.kp.laatan_posX, self.kp.laatan_posY)
                print(self.kp.laatan_posX, self.kp.laatan_posY)


        if nappaimet[pygame.K_a]:
            if self.kp.laatan_puoli == "vasen":
                print(self.kp.laatan_posX, self.kp.laatan_posY)
                self.set_pos(self.kp.laatan_posX, self.kp.laatan_posY)



    def update(self):
        self.get_input()








