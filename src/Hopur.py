import sys
import random
import pygame
from pygame.locals import *
import math
import Einstaklingur as E
import Uppsetning as U
import time

u = U.Uppsetning()

class Hopur():

    def __init__(self):
        self.n=100 #number of points

        #Listi af einstaklingum
        self.einstaklingur = []

        self.svaedi = []

        self.LikurByrja = 10

        self.LikurSmit = 10

        #Hæsta x gildi svæðis
        self.xmax = 0 
        #Hæsta y gildi svæðis
        self.ymax = 0 
        #Lægsta x gildi svæðis
        self.xmin = 0
        #Lægsta y gildi svæðis
        self.ymin = 0
        #x=250
        self.x200 = 0

        #Breyta sem telur fjölda sýktra 
        self.teljasykta = 0
        self.teljabatnad = 0
        self.teljaeinangrun = 0
        self.teljalatna = 0
        self.teljaheilbrigda = 0

    #Búum til svæði og teiknum hópa
    def fjogur_svaedi_hopar(self):
        #Fjöldi reita x
        l = 2
        #Fjöldi svæða y
        m = 2

        #Búum til svæði
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

    def svaedaskopp_fjogur_svaedi(self):
        for e in self.einstaklingur:
            if (e.x < self.xmin1+u.radius or e.x > self.xmax1-u.radius) and (e.x < self.xmin2+u.radius or e.x > self.xmax2-u.radius):
                e.vx = -1 * e.vx
            if (e.y < self.ymin1+u.radius or e.y > self.ymax1-u.radius) and (e.y < self.ymin2+u.radius or e.y > self.ymax2-u.radius):
                e.vy = -1 * e.vy

    def svaedaskopp_eitt_svaedi(self):
        for e in self.einstaklingur:
            number = u.random_tala()
            if number <= 95:  #Líkur að komast ekki í gegn
                if (e.x > self.x200-u.radius) and (e.x < self.x200+u.radius):
                    e.vx = -1 * e.vx

    #Búum til n marga einstaklinga á opnu svæði
    def einstaklingar(self):
        for i in range(self.n):
            e = E.Einstaklingur(u.xBORD, u.yBORD, u.radius, self.LikurByrja, self.LikurSmit)
            self.einstaklingur.append(e)

    #Boltar skoppa af veggjum
    def veggskopp(self):
        for e in self.einstaklingur:
            if e.x < u.radius or e.x > u.xBORD-u.radius:
                e.vx = -1 * e.vx
            if e.y < u.radius or e.y > u.yBORD-u.radius:
                e.vy = -1 * e.vy

    def arekstur(self):
        #UPDATE POSITIONS
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

    def syktir_location(self):
        for e in self.einstaklingur:
            self.x200 = self.xmin + 200
            if (e.litur==u.SYKTUR):
                e.x = random.randrange(0+u.radius, self.x200-u.radius)

    def faera(self):
        for e in self.einstaklingur:
            e.faera()

    def teikna(self):
        for e in self.einstaklingur:
            e.teikna()

    def breyting_timi(self):
        for e in self.einstaklingur:
            e.breyting_timi()

    def greina_smit(self):
        for e in self.einstaklingur:
            e.einangrun()

    def teikna(self):
        for e in self.einstaklingur:
            e.teikna()

    def breyting_timi(self):
        for e in self.einstaklingur:
            e.breyting_timi()

    def greina_smit(self):
        for e in self.einstaklingur:
            e.einangrun()

    def upphafsstilling(self, n, LikurByrja, LikurSmit):
        self.n = n
        self.LikurByrja = LikurByrja
        self.LikurSmit = LikurSmit

