import pygame, sys
from no_koodaillaas_sit_vähä.taso import *
import random
from pelaaja import Pelaaja
from pygame_functions import *









#--screen
screen = pygame.display.set_mode((LEVEYS, KORKEUS), pygame.RESIZABLE)
#--yleinen alustus
kello = pygame.time.Clock()
taso = Taso(screen)
pelaaja = Pelaaja((taso.x, taso.y))

#--kuvat ja videot
bg = pygame.image.load("lisatarvikkeet/bg.png").convert()
start_kuva = pygame.image.load("lisatarvikkeet/start_nappula.png").convert_alpha()
#ns = no scale
about_kuva_ns = pygame.image.load("lisatarvikkeet/readme_nappula.png").convert_alpha()
about_kuva = pygame.transform.scale(about_kuva_ns, (140, 90))
ui_bg = pygame.image.load("lisatarvikkeet/ui_bg.png")
teksti_luettu = False



def info_text():
    file = "lisatarvikkeet/info_text.txt"
    file_avaus = open(file)
    rivit = file_avaus.read()
    file_avaus.close()

    teksti_raw = "".join(rivit)




    font = pygame.font.Font('freesansbold.ttf', 15)
    teksti = font.render(teksti_raw, True, (255, 255, 255))
    tekstiRect = teksti.get_rect()
    tekstiRect.center = (600, 100)
    screen.blit(teksti, tekstiRect)



        




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
                pygame.draw.circle(screen, pygame.Color(100, 0, 42), partikkeli[0], int(partikkeli[1]))




    def lisaa_partikkelit(self):
        pos_x = taso.pelaaja_sprite.rect.x + 21
        pos_y = taso.pelaaja_sprite.rect.y + 30
        radius = 7


        suunta_x = random.randint(-2, 2)
        suunta_y = random.randint(-1, 5)



        partikkeli_ympyra = [[pos_x, pos_y], radius, [suunta_y, suunta_x]]
        self.partkkelit.append(partikkeli_ympyra)

    def poista_partikkelit(self):
        partikkeli_kopio = [partikkeli for partikkeli in self.partkkelit if partikkeli[1] > 0]
        self.partkkelit = partikkeli_kopio






#Pelissä näkyvän "ikkunan" määritys
class PeliStatus():
    def __init__(self):
        self.status = "intro"





    def status_manageri(self):
        if self.status == "intro":
            self.intro()
        if self.status == "paa_peli":
            self.paa_peli()
        if self.status == "info":
            self.info()

    def intro(self):
        screen.blit(ui_bg, (0, 0))

        start_btn.draw()
        read_me_btn.draw()


        self.status = "intro"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



            if start_btn.draw():
                self.status = "paa_peli"

            if read_me_btn.draw():
                self.status = "info"

        pygame.display.update()

    def paa_peli(self):


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == PARTIKKELI_EVENT:
                partikkeli1.lisaa_partikkelit()

        screen.blit(bg, (0, 0))

        partikkeli1.partikkelit_l_p()
        taso.run(screen)
        pygame.display.update()

    def info(self):
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        info_text()





        pygame.display.update()







status = PeliStatus()


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.klikattu = False

    def draw(self):
        self.action = False
        pos = pygame.mouse.get_pos()


        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.klikattu == False:
                self.klikattu = True
                self.action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.klikattu = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return self.action

start_btn = Button(900 , 760, start_kuva)
read_me_btn = Button(690, 80, about_kuva)













pygame.init()



#tason status
peli_satus = PeliStatus()




#partikkeli setup
partikkeli1 = Partikkelit()
PARTIKKELI_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTIKKELI_EVENT, 30)



#otsikko
pygame.display.set_caption("RTDWD")

#pelilooppi
while True:
    peli_satus.status_manageri()
    kello.tick(60)

