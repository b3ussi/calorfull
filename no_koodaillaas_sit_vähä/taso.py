import pygame
from no_koodaillaas_sit_vähä.palikat import Palikka
from no_koodaillaas_sit_vähä.asetukset import *
from no_koodaillaas_sit_vähä.pelaaja import Pelaaja
from os import path
import random















class Taso:
    def __init__(self, surface):




        self.display_surface = surface
        self.tason_alustus(kartta_1)
        self.paras_score = 0
        self.pisteet = 0
        self.aktiivinen = True











    # def load_data(self, win):
    #     #lataa high score
    #     self.dir = path.dirname(__file__)
    #     with open(path.join(self.dir, kartta.hs_file), "w") as f:
    #         try:
    #             self.paras_score = int(f.read())
    #         except:
    #             self.paras_score = 0
    #
    #         with open(path.join(self.dir, kartta.hs_file), "w") as f:
    #             f.write(str(self.paras_score))

    def tason_alustus(self, layout):
        self.palikat = pygame.sprite.Group()
        self.pelaaja = pygame.sprite.GroupSingle()
        self.portaali = pygame.sprite.GroupSingle()
        self.pelaajan_status = True


        for rivi_indeksi, rivi in enumerate(kartta_1):
            # tämä looppi ajaa kaikki rivit

            # arvotaan meneekö rivin ensimmäinen palikka rikki (totta (True) tai valetta (False))
            menee_rikki = bool(random.getrandbits(1))



            for solu_indeksi, sarake in enumerate(rivi):
                # tämä looppi ajaa rivin kaikki merkit
                # yhdellä rivillä voi olla vain kaksi palikkaa
                self.x = solu_indeksi * PALIKKAKOKO
                self.y = rivi_indeksi * PALIKKAKOKO



                if sarake == "X":



                    self.palikka_sprite = Palikka((self.x, self.y), PALIKKAKOKO, menee_rikki)
                    self.palikat.add(self.palikka_sprite)

                    # käännetään arvottu totuusarvo (boolean) toisin päin eli todesta tulee vale tai päinvastoin

                    menee_rikki = not menee_rikki

                    if menee_rikki:
                        self.palikka = 1
                    else:
                        self.palikka = 2
                        print("!noi")

                if sarake == "P":
                    self.pelaaja_sprite = Pelaaja((self.x, self.y))
                    self.pelaaja.add(self.pelaaja_sprite)






    def tuho(self):
        pygame.sprite.spritecollide(self.pelaaja_sprite, self.palikat, True)



    def elamien_piirto(self, win):
        self.elamat = self.pelaaja_sprite.elamat
        self.fontti = pygame.font.Font("freesansbold.ttf", 32)
        self.teksti = self.fontti.render(f"Elämät: {self.elamat}", True, (255, 255, 255))
        win.blit(self.teksti, (60, 60))



    def tormaykset_palikka(self):
        pelaaja = self.pelaaja.sprite

        # self.pelaaja_sprite.rect.x += self.pelaaja_sprite.suunta.x * self.pelaaja_sprite.nopeus
        # self.pelaaja_sprite.rect.y += self.pelaaja_sprite.suunta.y * self.pelaaja_sprite.nopeus

        for sprite in self.palikat.sprites():
            if sprite.rect.colliderect(pelaaja.rect):
                if isinstance(sprite, Palikka):
                    # isinstance tarkastaa että sprite on Palikka-tyyppiä

                    if sprite.menee_rikki == False:
                            self.pisteet += sprite.anna_pisteet()

                    if sprite.menee_rikki:
                        print("tämä laattaa hajoaa!")
                        self.tuho()

                        if self.pelaaja_sprite.elamat > 0:
                            self.pelaaja_sprite.elamat -= 1
                            # self.pelaaja_sprite.set_pos(self.x, self.y)
                            self.pelaajan_status = False
                            if self.pelaaja_sprite.elamat == 0:
                                print("Kuolit lopullisesti")
                                self.pelaaja_sprite.elossa = False



    def pisteiden_tulostus(self, win):
        self.fontti = pygame.font.Font("freesansbold.ttf", 32)
        self.teksti = self.fontti.render(f"Score: {self.pisteet}", True, (255, 255, 255))
        self.tekstiRect = self.teksti.get_rect()
        self.tekstiRect.center = (120, 120)
        win.blit(self.teksti, self.tekstiRect)







    def kuollut(self, win):
        if self.pelaaja_sprite.elossa == False:
            self.game_over = True
            win.fill((0, 0, 0))

            self.fontti = pygame.font.Font("freesansbold.ttf", 32)
            self.teksti = self.fontti.render("You died! Press r to restart", True, (255, 255, 255))
            self.tekstiRect = self.teksti.get_rect()
            self.tekstiRect.center = (KORKEUS // 2, LEVEYS // 2)
            win.blit(self.teksti, self.tekstiRect)

            self.nappaimet = pygame.key.get_pressed()

            if self.nappaimet[pygame.K_r]:

                if self.pisteet > self.paras_score:
                    self.paras_score = self.pisteet
                self.pisteet = 0
                self.pelaaja_sprite.elossa = True
                self.pelaaja_sprite.elamat = 3
                self.tason_alustus(kartta_1)








    def get_highest_score(self):
        with open("lisatarvikkeet/highscore.txt", "r") as f:
            return f.read()



    def parhaat_pisteet_tulostus(self, win):

        with open("lisatarvikkeet/highscore.txt", "w") as f:
            f.write(str(self.paras_score))

        self.fontti = pygame.font.Font("freesansbold.ttf", 32)
        self.teksti = self.fontti.render(f"Your high score is: {self.paras_score}", True, (255, 255, 255))
        self.tekstiRect = self.teksti.get_rect()
        self.tekstiRect.center = (600, 100)
        win.blit(self.teksti, self.tekstiRect)

    def scroll_y(self):
        pelaaja = self.pelaaja.sprite
        pelaaja_y = self.pelaaja_sprite.rect.centery
        suunta_y = self.pelaaja_sprite.suunta.y

        if pelaaja_y < KORKEUS/4 and suunta_y < 0:
            self.world_shift = 4
            self.pelaaja_sprite.nopeus = 0
        elif pelaaja_y > KORKEUS-(KORKEUS/4) and suunta_y > 0:
            self.world_shift = -4
            self.pelaaja_sprite.nopeus = 0
        else:
            self.world_shift = 0
            self.pelaaja_sprite.nopeus = 6

    def pelaajan_liikkumisen_rajoitus(self):
        x = self.pelaaja_sprite.rect.x
        y = self.pelaaja_sprite.rect.y

        if x < 225:
            self.pelaaja_sprite.set_pos(225, y)

        if x > 320:
            self.pelaaja_sprite.set_pos(320, y)





    def run(self, win):
        #palikat
        self.palikat.draw(self.display_surface)
        self.palikat.update()

        #pelaaja
        self.pelaaja.draw(self.display_surface)
        self.pelaaja.update()
        # self.scroll_y()
        self.tormaykset_palikka()
        # self.pelaajan_liikkumisen_rajoitus()
        self.elamien_piirto(win)
        self.parhaat_pisteet_tulostus(win)
        self.pisteiden_tulostus(win)
        self.kuollut(win)

















