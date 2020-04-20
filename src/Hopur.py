import sys
import random
import pygame
from pygame.locals import *
import math
import Einstaklingur as E
import Uppsetning as U
import time

#Búum til hlut af klasanum uppsetning
u = U.Uppsetning()

class Hopur():

    def __init__(self):
        #Fjöldi einstaklinga
        self.n=0

        #Listi af einstaklingum
        self.einstaklingur = []

        #Breytur sem notandi velur
        self.LikurByrja = 10
        self.LikurSmit = 10

        #Hnit fyrir hermun á fjórum svæðum
        #Hæsta x gildi svæðis
        self.xmax = 0 
        #Hæsta y gildi svæðis
        self.ymax = 0 
        #Lægsta x gildi svæðis
        self.xmin = 0
        #Lægsta y gildi svæðis
        self.ymin = 0

        #Hnit fyrir svæðið í hermun nr. 2
        #x=250
        self.x200 = 0

        #Breytur sem telja fjölda einstaklinga í hverju ástandi
        self.teljasykta = 0
        self.teljabatnad = 0
        self.teljaeinangrun = 0
        self.teljalatna = 0
        self.teljaheilbrigda = 0

    #Búum til fjögur svæði
    def fjogur_svaedi_hopar(self):
        #Fjöldi reita x
        l = 2
        #Fjöldi svæða y
        m = 2

        #Búum til svæði og geymum hnitin í breytum --1 og --2 (hermun 3)
        for i in range(l):
            self.xmax = u.xBORD - (l-1-i)*u.xBORD/l
            self.xmin = i*(u.xBORD/l)
            if i == 0:
                self.xmin1 = self.xmin
                self.xmax1 = self.xmax
            else:
                self.xmin2 = self.xmin
                self.xmax2 = self.xmax
            for j in range(m):
                self.ymax = u.yBORD - (m-1-j)*u.yBORD/m
                self.ymin = j*(u.yBORD/m)
                if j == 0:
                    self.ymin1 = self.ymin
                    self.ymax1 = self.ymax
                else:
                    self.ymin2 = self.ymin
                    self.ymax2 = self.ymax

    #Látum einstaklinga skoppa af veggjum þegar svæðin eru fjögur (hermun 3)
    def svaedaskopp_fjogur_svaedi(self):
        for e in self.einstaklingur:
            if (e.x < self.xmin1+u.radius or e.x > self.xmax1-u.radius) and (e.x < self.xmin2+u.radius or e.x > self.xmax2-u.radius):
                e.vx = -1 * e.vx
            if (e.y < self.ymin1+u.radius or e.y > self.ymax1-u.radius) and (e.y < self.ymin2+u.radius or e.y > self.ymax2-u.radius):
                e.vy = -1 * e.vy

    #Látum einstaklinga skoppa innan svæðis (hermun 2)
    def svaedaskopp_eitt_svaedi(self):
        for e in self.einstaklingur:
            number = u.random_tala()
            if number <= 95:  #Líkur að komast ekki í gegn
                if (e.x > self.x200-u.radius) and (e.x < self.x200+u.radius):
                    e.vx = -1 * e.vx

    #Búum til n marga einstaklinga á opnu svæði
    def einstaklingar(self):
        for i in range(self.n):
            e = E.Einstaklingur(0,0,u.xBORD, u.yBORD, u.radius, self.LikurByrja, self.LikurSmit)
            self.einstaklingur.append(e)

    #Búum til n marga einstaklinga, skipt niður á 4 svæði (hermun 3)
    def einstaklingar_fjogur_svaedi(self):
        vinstra_uppi = round(self.n/2)
        vinstra_nidri = round(self.n/5)
        haegra_uppi = round(self.n/5)
        haegra_nidri = round(self.n/10)

        #Ef talan deilist ekki heilt þá fyllum við upp í n og setjum í svæðið uppi til vinstri
        if(vinstra_uppi+vinstra_nidri+haegra_uppi+haegra_nidri != self.n):
            vinstra_uppi += self.n-(vinstra_uppi+vinstra_nidri+haegra_uppi+haegra_nidri)

        for i in range(vinstra_uppi):
            e = E.Einstaklingur(self.xmin1,self.ymin1,self.xmax1, self.ymax1, u.radius, self.LikurByrja, self.LikurSmit)
            self.einstaklingur.append(e)
        for i in range(vinstra_nidri):
            e = E.Einstaklingur(self.xmin1,self.ymin2,self.xmax1, self.ymax2, u.radius, self.LikurByrja, self.LikurSmit)
            self.einstaklingur.append(e)
        for i in range(haegra_uppi):
            e = E.Einstaklingur(self.xmin2,self.ymin1,self.xmax2, self.ymax1, u.radius, self.LikurByrja, self.LikurSmit)
            self.einstaklingur.append(e)
        for i in range(haegra_nidri):
            e = E.Einstaklingur(self.xmin2,self.ymin2,self.xmax2, self.ymax2, u.radius, self.LikurByrja, self.LikurSmit)
            self.einstaklingur.append(e)

    #Boltar skoppa af veggjum
    def veggskopp(self):
        for e in self.einstaklingur:
            if e.x < u.radius or e.x > u.xBORD-u.radius:
                e.vx = -1 * e.vx
            if e.y < u.radius or e.y > u.yBORD-u.radius:
                e.vy = -1 * e.vy

    #Boltar skoppa af hvor öðrum og lita stundum hvorn annan, fer eftir aðstæðum
    def arekstur(self):
        for i in range(self.n):
            if(self.einstaklingur[i].litur!=u.LATNIR and self.einstaklingur[i].litur!=u.EINANGRUN):
                for j in range(i+1,self.n):
                    if(self.einstaklingur[j].litur!=u.LATNIR and self.einstaklingur[j].litur!=u.EINANGRUN):
                        distance = math.hypot(self.einstaklingur[i].x - self.einstaklingur[j].x, self.einstaklingur[i].y - self.einstaklingur[j].y)
                        if distance <= 2*u.radius:
                            self.einstaklingur[j].vx = -1 * self.einstaklingur[j].vx
                            self.einstaklingur[j].vy = -1 * self.einstaklingur[j].vy
                            self.einstaklingur[i].vx = -1 * self.einstaklingur[i].vx
                            self.einstaklingur[i].vy = -1 * self.einstaklingur[i].vy
                            if(self.einstaklingur[j].litur==u.SYKTUR and self.einstaklingur[i].litur==u.HEILBRIGDUR):
                                self.einstaklingur[i].sykist()
                            if(self.einstaklingur[i].litur==u.SYKTUR and self.einstaklingur[j].litur==u.HEILBRIGDUR):
                                self.einstaklingur[j].sykist()

    #Fall sem heldur utanum talningar á ástandi einstaklinga
    def talningar(self):
        self.teljasykta = 0
        self.teljabatnad = 0
        self.teljalatna = 0
        self.teljaheilbrigda = 0
        self.teljaeinangrun = 0
        for e in self.einstaklingur:
            if(e.talning == 0):
                self.teljaheilbrigda += 1
            if (e.talning == 1):
                self.teljasykta += 1
            if(e.talning == 2):
                self.teljabatnad += 1
            if(e.talning == 3):
                self.teljalatna += 1
            if(e.talning == 4):
                self.teljaeinangrun +=1

    #Fall sem lætur sýkta eingöngu byrja innan sóttkví-svæðisins (hermun 2)
    def syktir_location(self):
        for e in self.einstaklingur:
            self.x200 = self.xmin + 200
            if (e.litur==u.SYKTUR):
                e.x = random.randrange(0+u.radius, self.x200-u.radius)
            
    #Fall sem færir einstaklinga
    def faera(self):
        for e in self.einstaklingur:
            e.faera()

    #Fall sem teiknar einstaklinga
    def teikna(self):
        for e in self.einstaklingur:
            e.teikna()

    #Fall sem heldur utanum tíma fyrir hvern einstakling, sem sér svo til þess að breyta ástandi sýktra
    def breyting_timi(self):
        for e in self.einstaklingur:
            e.breyting_timi()

    #Fall sem sendir einstaklinga í einangrun ef smit greinist
    def greina_smit(self):
        for e in self.einstaklingur:
            e.einangrun()

    #Fall sem teiknar einstaklingana á borðið
    def teikna(self):
        for e in self.einstaklingur:
            e.teikna()

    #Fall sem heldur utanum breyturnar sem notandi velur og sér til þess að þær komist til skila
    def upphafsstilling(self, n, LikurByrja, LikurSmit):
        self.n = n
        self.LikurByrja = LikurByrja
        self.LikurSmit = LikurSmit

