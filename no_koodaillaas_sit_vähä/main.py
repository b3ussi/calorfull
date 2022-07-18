import pygame, sys
from pygame import BLEND_RGB_ADD

from no_koodaillaas_sit_vähä.taso import *
import random
from pelaaja import Pelaaja
from pygame_functions import *
from lisatarvikkeet.info_text import *









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
fontti = "freesansbold.ttf"
fontSize = 15
fontColour = (255, 255, 255)
glow_color = (255, 255, 255)
inf_1 = info_teksti1
inf_2 = info_teksti2
inf_3 = info_teksti3
inf_4 = info_teksti4
inf_5 = info_teksti5
inf_6 = info_teksti6
inf_7 = info_teksti7
inf_8 = info_teksti8
inf_9 = info_teksti9
inf_10 = info_teksti10






def info_text():

    for t in range(10):
        x = 60
        y = 60

        font = pygame.font.Font(fontti, fontSize)
        teksti1 = font.render(inf_1, True, fontColour)
        teksti2 = font.render(inf_2, True, fontColour)
        teksti3 = font.render(inf_3, True, fontColour)
        teksti4 = font.render(inf_4, True, fontColour)
        teksti5 = font.render(inf_5, True, fontColour)
        teksti6 = font.render(inf_6, True, fontColour)
        teksti7 = font.render(inf_7, True, fontColour)
        teksti8 = font.render(inf_8, True, fontColour)
        teksti9 = font.render(inf_9, True, fontColour)
        teksti10 = font.render(inf_10, True, fontColour)
        screen.blit(teksti1, (x, y))
        screen.blit(teksti2, (x, y + 20))
        screen.blit(teksti3, (x, y + 40))
        screen.blit(teksti4, (x, y + 60))
        screen.blit(teksti5, (x, y + 80))
        screen.blit(teksti6, (x, y + 100))
        screen.blit(teksti7, (x, y + 120))
        screen.blit(teksti8, (x, y + 140))
        screen.blit(teksti9, (x, y + 160))
        screen.blit(teksti10,(x, y + 180))



        




particles = []



def circle_surf(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf










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

        # screen.blit(bg, (0, 0))
        screen.fill((0, 0, 0))

        taso.run(screen)
        x = taso.pelaaja_sprite.rect.x + 40
        y = taso.pelaaja_sprite.rect.y + 30

        particles.append([[x, y], [random.randint(0, 20) / 10 - 1, 5], random.randint(0, 15)])

        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            #painovoima
            # particle[1][1] += 0.15
            pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))

            radius = particle[2] * 2
            screen.blit(circle_surf(radius, (20, 20, 60)), (int(particle[0][0] - radius), int(particle[0][1] - radius)),
                        special_flags=BLEND_RGB_ADD)

            if particle[2] <= 0:
                particles.remove(particle)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



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
# partikkeli1 = Partikkelit()
PARTIKKELI_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTIKKELI_EVENT, 20)



#otsikko
pygame.display.set_caption("RTDWD")

#pelilooppi
while True:
    peli_satus.status_manageri()
    kello.tick(60)

