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
        #Færa í sér klasann hópur, gera þar fall með árekstur, sá klasi höndlar 1 svæði
        #BREYTILEGT
        self.n=100 #number of points

        #Listi af einstaklingum
        self.einstaklingur = []

        self.svaedi = []

        #Hæsta x gildi svæðis
        self.xmax = 0 #u.xmax
        #Hæsta y gildi svæðis
        self.ymax = 0 #u.ymax
        #Lægsta x gildi svæðis
        self.xmin = 0
        #Lægsta y gildi svæðis
        self.ymin = 0
        #x=250
        self.x250 = 0

    #Búum til svæði og teiknum hópa
    def fjogur_svaedi_hopar(self):
        #Fjöldi reita x
        l = 2
        #Fjöldi svæða y
        m = 2
        #Heildarfjöldi svæða
        k = 4

        #Fjöldi fólks í hóp
        #self.n = 25

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
                if (e.x > self.x250-u.radius) and (e.x < self.x250+u.radius):
                    e.vx = -1 * e.vx

    #Búum til n marga einstaklinga á opnu svæði
    def einstaklingar(self):
        for i in range(self.n):
            e = E.Einstaklingur(u.xBORD, u.yBORD, u.radius)
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
            if(self.einstaklingur[i].litur!=u.LATNIR):
                for j in range(i+1,self.n):
                    if(self.einstaklingur[j].litur!=u.LATNIR):
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

    def syktir_location(self):
        for e in self.einstaklingur:
            self.x250 = self.xmin + 250
            if (e.litur==u.SYKTUR):
                e.x = random.randrange(0+u.radius, self.x250-u.radius)

    def faera(self):
        for e in self.einstaklingur:
            e.faera()

    def teikna(self):
        for e in self.einstaklingur:
            e.teikna()

    def breyting_timi(self):
        for e in self.einstaklingur:
            e.breyting_timi()




