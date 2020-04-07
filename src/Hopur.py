import sys
import random
import pygame
from pygame.locals import *
import math
import Einstaklingur as E
import Uppsetning as U

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
        self.xmaxx = 0 #u.xmax
        #Hæsta y gildi svæðis
        self.ymaxx = 0 #u.ymax
        #Lægsta x gildi svæðis
        self.xmin = 0
        #Lægsta y gildi svæðis
        self.ymin = 0

    #Búum til svæði og teiknum hópa
    def svaedi_hopar(self):
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
            self.xmaxx = u.xmax - (l-1-i)*u.xmax/l
            self.xmin = i*(u.xmax/l)
            if i == 0:
                self.xmin1 = self.xmin
                self.xmaxx1 = self.xmaxx
            else:
                self.xmin2 = self.xmin
                self.xmaxx2 = self.xmaxx
            for j in range(m):
                self.ymaxx = u.ymax - (m-1-j)*u.ymax/m
                self.ymin = j*(u.ymax/m)
                if j == 0:
                    self.ymin1 = self.ymin
                    self.ymaxx1 = self.ymaxx
                else:
                    self.ymin2 = self.ymin
                    self.ymaxx2 = self.ymaxx

                #print(self.xmin,self.xmaxx,self.ymin,self.ymaxx)
                #self.lina1 = pygame.draw.line(u.windowSurface, u.BLACK, (self.xmin, self.ymin), (self.xmaxx, self.ymin), 50)
                #self.lina2 = pygame.draw.line(u.windowSurface, u.BLACK, (self.xmin, self.ymin), (self.xmin, self.ymaxx), 50)
                #self.people()

    def svaedaskopp(self,e):
        if (e.x < self.xmin1+u.radius or e.x > self.xmaxx1-u.radius) and (e.x < self.xmin2+u.radius or e.x > self.xmaxx2-u.radius):
            e.vx = -1 * e.vx
        if (e.y < self.ymin1+u.radius or e.y > self.ymaxx1-u.radius) and (e.y < self.ymin2+u.radius or e.y > self.ymaxx2-u.radius):
            e.vy = -1 * e.vy

    #Búum til n marga einstaklinga á opnu svæði
    def people(self):
        for i in range(self.n):
            e = E.Einstaklingur(u.xmax, u.ymax, u.radius)
            self.einstaklingur.append(e)

    #Boltar skoppa af veggjum
    def veggskopp(self, e):
        if e.x < u.radius or e.x > u.xmax-u.radius:
            e.vx = -1 * e.vx
        if e.y < u.radius or e.y > u.ymax-u.radius:
            e.vy = -1 * e.vy

    def arekstur(self,einstaklingur):
        #UPDATE POSITIONS
        for i in range(self.n):
            for j in range(i+1,self.n):
                distance = math.hypot(einstaklingur[i].x - einstaklingur[j].x, einstaklingur[i].y - einstaklingur[j].y)
                if distance <= 2*u.radius:
                    einstaklingur[j].vx = -1 * einstaklingur[j].vx
                    einstaklingur[j].vy = -1 * einstaklingur[j].vy
                    einstaklingur[i].vx = -1 * einstaklingur[i].vx
                    einstaklingur[i].vy = -1 * einstaklingur[i].vy
                    if(einstaklingur[j].litur==u.ORANGE):
                        einstaklingur[i].sykist()
                    if(einstaklingur[i].litur==u.ORANGE):
                        einstaklingur[j].sykist()
