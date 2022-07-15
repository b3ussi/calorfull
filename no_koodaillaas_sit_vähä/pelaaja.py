import pygame
from pygame_functions import *




class Pelaaja(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Pelaaja, self).__init__()
        self.image_get = pygame.image.load("lisatarvikkeet/pallo.png").convert_alpha()
        self.image = pygame.transform.scale(self.image_get, (100, 100))

        self.rect = self.image.get_rect(topleft=pos)
        self.elamat = 3
        self.elossa = True



    def set_pos(self, x_pos, y_pos):
        self.rect.x = x_pos
        self.rect.y = y_pos


    def get_input(self):
        nappaimet = pygame.key.get_pressed()
        if self.rect.y < 1000:
            if nappaimet[pygame.K_d]:
                self.set_pos(655, 785)
            if nappaimet[pygame.K_a]:
                self.set_pos(450, 785)
#muuta arvoja, kesken
        elif self.rect.y < 985:
            pass









    def update(self):
        self.get_input()

