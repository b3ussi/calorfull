# import random
from asetukset import kartta
import pygame
# lives = 3
# score = 0
# k = ["a", "b"]
#
#
#
#
# poop = True
# while poop:
#     o = random.choice(k)
#     b = input("a or b?: ")
#     if o == b:
#         score += 1
#         continue
#
#     else:
#         lives -= 1
#         print("u lost one heart")
#     if lives == 0:
#         print("U died lol")
#         break
# print(f"ur score was: {score}")



# class KameraRyhma(pygame.sprite.Group):
#     def __init__(self):
#         super(KameraRyhma, self).__init__()
#     # def custom_pirrustus_metodi(self):
#     #     for sprite in self.sprites():
#     #         screen.blit()
#     #     self.display_surface = pygame.display.get_surface()
#     #     self.offset = pygame.math.Vector2()
#     #     self.half_w = self.display_surface.get_size()[0] // 2
#     #     self.half_h = self.display_surface.get_size()[1] // 2
#     #     self.zoom_scale = 1
#     #
#     #     self.internal_surface_koko = (2500, 2500)
#     #     self.internal_surface = pygame.Surface(self.internal_surface_koko, pygame.SRCALPHA)
#     #     self.internal_rect = self.internal_surface.get_rect(center=(self.half_w, self.half_h))
#     #     self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surface_koko)
#     #
#     #     skaalattu_surface = pygame.transform.scale(self.internal_surface,self.internal_surface_size_vector * self.zoom_scale)
#             skaalattu_rect = skaalattu_surface.get_rect(center=(self.half_w, self.half_h))
#             self.display_surface.blit(skaalattu_surface, skaalattu_rect)
#
# kamera_ryhmä = KameraRyhma
# jaetut_palikat1 = pygame.sprite.Group()
# jaetut_palikat2 = pygame.sprite.Group()
#
#
# o=len(kartta)

# import random
#
#
# class Olio:
#     def __init__(self, menee_rikki):
#         self.menee_rikki = menee_rikki
#
#
# hajoaa = bool(random.getrandbits(1))
#
# olio_lista = []
# for i in range(5):
#     print(f"hajoaako? {hajoaa}")
#     oma_olio = Olio(hajoaa)
#     olio_lista.append(oma_olio)
#     hajoaa = not hajoaa
#
# for i, o in enumerate(olio_lista):
#     print(f"#{i} {o.menee_rikki}")



# import random
#
# class Kantaluokka:
#     def __init__(self, nimi):
#         print("Terveisiä kantaluokan rakentajasta")
#         self.nimi = nimi
#
#     def kerro_nimesi(self):
#         print(f"nimeni on {self.nimi}")
#
# class Olio(Kantaluokka):
#     def __init__(self, nimi, sukunimi, menee_rikki):
#         super().__init__(nimi)
#         print("Terveisiä Olio-luokan rakentajasta")
#         self.menee_rikki = menee_rikki
#         self.sukunimi = sukunimi
#
#     def kerro_nimesi(self):
#         self.nimi = f"{self.nimi} {self.sukunimi}"
#         super().kerro_nimesi()
#
#
# o = Olio('pertti', 'pertinpoika', True)
# o.kerro_nimesi()


#
# # instanssi
#
# class Ihminen:
#     # ihminen on luokka (class)
#     def __init__(self, nimi):
#         self.nimi = nimi
#
# # tässä luodaan olio joka tallennetaan otto-nimiseen muuttujaan
# # mutta yhtä hyvin voitaisiin sanoa, että otto on Ihminen-luokan instanssi
# otto = Ihminen('otto')
#
#
# class merkkijono(str):
#     def __new__(cls, value):
#         obj = str.__new__(cls, value)
#         obj.value = value
#         # obj.meta = meta
#         return obj
#     def __str__(self):
#         return f"hähää {self.value}"
#
#     def lower(self):
#         return f"enhän anna sulle pientä tekstiä"
#
#
# # periminen sisäänrakennetuista (builtin) tyypeistä
# class luku(float):
#     def __new__(self, value):
#         return float.__new__(self, value)
#
#     def __add__(self, other):
#         # tämä on Pythonin summa funktio. Eli summaa nykyisen arvon toisen luvun kanssa
#         return self.real + other + 1
#
#     def __sub__(self, other):
#         # tämä on Pythonin erotus funktio. Eli summaa nykyisen arvon toisen luvun kanssa
#         return self.real - other - 1
#
#
# # a = luku(10.0)
# # b = 7.0
# # print(a+b) # a.__add__(b)
# # print(a-b) # a.__sub__(b)
#
#
# def rekursiivinen_funktio(sallittu_maara, lukumaara=0):
#     if lukumaara < sallittu_maara:
#         print("kutsun itseäni")
#         rekursiivinen_funktio(sallittu_maara, lukumaara + 1)
#
# rekursiivinen_funktio(10)
#
# # teksti = merkkijono("minun tekstini")
# # print(teksti)
# # print(teksti.upper())
# # print(teksti.lower())
# # print(isinstance(teksti, str))
# # print(isinstance(teksti, merkkijono))
# # print(isinstance(teksti, int))
# # teksti = teksti + "moi"
# # print(teksti)