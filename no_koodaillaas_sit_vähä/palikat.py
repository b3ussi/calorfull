import pygame
import random




class Palikka(pygame.sprite.Sprite):
    def __init__(self, paikka, koko, menee_rikki):
        super().__init__()
        # Tämä on Sprite-kantaluokasta periytetty olio
        # sillä pitää olla .image ja .rect attribuutit
        self.image = pygame.Surface((koko, koko))
        self.image.fill("blue")
        self.rect = self.image.get_rect(topleft=paikka)
        self.menee_rikki = menee_rikki
        self.aktiivinen = True

    def anna_pisteet(self):
        if self.aktiivinen:
            self.aktiivinen = False
            return 1
        else:
            return 0






    def update(self, y_shiftaus):
            self.rect.y += y_shiftaus





