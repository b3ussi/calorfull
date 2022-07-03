import pygame




class Pelaaja(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Pelaaja, self).__init__()
        self.image = pygame.image.load("lisatarvikkeet/pallo.png").convert()
        # self.image = pygame.Surface((32, 32))
        # self.image.fill("green")
        self.rect = self.image.get_rect(topleft=pos)
        #vektori on pygamessa lista, joka koostuu x ja y
        self.suunta = pygame.math.Vector2(0, 0)
        self.nopeus1 = 0.25
        self.nopeus = 6
        self.elamat = 3
        self.elossa = True

    def set_pos(self, x_pos, y_pos):
        self.rect.x = x_pos
        self.rect.y = y_pos







    def get_input(self):
        nappaimet = pygame.key.get_pressed()

        if nappaimet[pygame.K_a]:
            self.suunta.x = -self.nopeus1
        elif nappaimet[pygame.K_d]:
            self.suunta.x = self.nopeus1
        elif nappaimet[pygame.K_w]:
            self.suunta.y = -self.nopeus1
        elif nappaimet[pygame.K_s]:
            self.suunta.y = self.nopeus1
        else:
            self.suunta.x = 0
            self.suunta.y = 0



    def update(self):
        self.get_input()

