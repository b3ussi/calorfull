import pygame
import random




class Palikka(pygame.sprite.Sprite):
    def __init__(self, paikka, koko, menee_rikki):
        super().__init__()
        # Tämä on Sprite-kantaluokasta periytetty olio
        # sillä pitää olla .image ja .rect attribuutit
        self.image = pygame.image.load("lisatarvikkeet/stop_palikka.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=paikka)
        self.menee_rikki = menee_rikki
        self.aktiivinen = True
        self.pos_x = self.rect.x
        self.pos_y = self.rect.y

    def anna_pisteet(self):
        if self.aktiivinen:
            self.aktiivinen = False
            return 1
        else:
            return 0












