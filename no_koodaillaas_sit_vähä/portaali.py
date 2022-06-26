import pygame


class Portaali(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Portaali, self).__init__()
        self.image = pygame.image.load("portaali.png").convert()
        self.rect = self.image.get_rect(topleft=pos)
        self.aktiivinen = True

    def anna_kartta_numero(self):
        if self.aktiivinen:
            self.aktiivinen = False
            return 1
        else:
            return 0

    def update(self, y_shiftaus):
        self.rect.y += y_shiftaus

