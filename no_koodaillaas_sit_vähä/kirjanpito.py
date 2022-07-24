from asetukset import *

class Kirjanpito:
    def __init__(self):
        full_scr = [1920, 1080]
        self.naytto_puolix = full_scr[0] / 2
        # ajaa kaikki rivit

    def rivin_tulostus(self):
        #ajaa kaikki rivit
        for rivi_indeksi, rivi in enumerate(kartta_1):
            # print(f"tämä on rivinumero {rivi_indeksi}")

            for solu_indeksi, solu in enumerate(rivi):
                self.x = solu_indeksi * PALIKKAKOKO
                self.y = rivi_indeksi * PALIKKAKOKO

                if solu == "X":
                    self.laatan_posX, self.laatan_posY = self.x, self.y



                    if self.laatan_posX < self.naytto_puolix:
                        self.laatan_puoli = "vasen"

                    if self.laatan_posX > self.naytto_puolix:
                        self.laatan_puoli = "oikea"











# millä rivillä pelaaja on?
# Tämä luokka kertoo pelaaja- oliolle mille laatalle sen kuuluisi mennä

k = Kirjanpito()


