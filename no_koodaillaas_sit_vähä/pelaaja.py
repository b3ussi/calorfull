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
        y = self.rect.y
        nappaimet = pygame.key.get_pressed()

        #tiedän, että on turha mutten jaksa poistaa :)
        if True:

            if y < 897 and y > 600:
                if nappaimet[pygame.K_d]:
                    self.set_pos(12, 300)

                if nappaimet[pygame.K_a]:
                    self.set_pos(12, 300)

            if y <= 896 and y >= 800:
                if nappaimet[pygame.K_d]:
                    self.set_pos(655, 785)

                if nappaimet[pygame.K_a]:
                    self.set_pos(450, 785)











    def update(self):
        self.get_input()

