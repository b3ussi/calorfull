import pygame, sys
from no_koodaillaas_sit_vähä.asetukset import *
#from asetukset import tason_numero
from no_koodaillaas_sit_vähä.taso import *
import random
from pelaaja import Pelaaja




#yleinen alustus
kartta = Kartta()
screen = pygame.display.set_mode((LEVEYS, KORKEUS))
kello = pygame.time.Clock()
taso = Taso(screen)
pelaaja = Pelaaja((taso.x, taso.y))




class Partikkelit:
    def __init__(self):
        self.partkkelit = []

    def partikkelit_l_p(self):
        #liikuttaa + pirtää partikkelit
        if self.partkkelit:
            self.poista_partikkelit()
            for partikkeli in self.partkkelit:
                #siirrä
                partikkeli[0][1] += partikkeli[2][0]
                partikkeli[0][0] += partikkeli[2][1]
                # kutista
                partikkeli[1] -= 0.2
                #piirrä
                pygame.draw.circle(screen, pygame.Color(250, 250, 250), partikkeli[0], int(partikkeli[1]))

    def lisaa_partikkelit(self):
        pos_x = taso.pelaaja_sprite.rect.x + 50
        pos_y = taso.pelaaja_sprite.rect.y + 60
        radius = 7
        suunta_x = random.randint(-2, 2)
        suunta_y = random.randint(-1, 5)
        partikkeli_ympyra = [[pos_x, pos_y], radius, [suunta_y, suunta_x]]
        self.partkkelit.append(partikkeli_ympyra)

    def poista_partikkelit(self):
        partikkeli_kopio = [partikkeli for partikkeli in self.partkkelit if partikkeli[1] > 0]
        self.partkkelit = partikkeli_kopio


#partikkeli setup
partikkeli1 = Partikkelit()
PARTIKKELI_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTIKKELI_EVENT, 30)


#Pelissä näkyvän "ikkunan" määritys
class PeliStatus():
    def __init__(self):
        self.status = "intro"





    def status_manageri(self):
        if self.status == "intro":
            self.intro()
        if self.status == "paa_peli":
            self.paa_peli()

    def intro(self):
        self.status = "intro"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.status = "paa_peli"
            screen.fill("green")
            pygame.display.update()

    def paa_peli(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == PARTIKKELI_EVENT:
                partikkeli1.lisaa_partikkelit()






        screen.fill("black")
        partikkeli1.partikkelit_l_p()
        taso.run(screen)


        taso.elamien_piirto(screen)
        taso.pisteiden_tulostus(screen)
        taso.kuollut(screen, LEVEYS, KORKEUS)
        taso.parhaat_pisteet_tulostus(screen)


        pygame.display.update()









pygame.init()



#tason status
peli_satus = PeliStatus()






#otsikko
pygame.display.set_caption("calörful")

#pelilooppi
while True:
    peli_satus.status_manageri()
    kello.tick(60)

    #move_and_draw_all_game_objects()