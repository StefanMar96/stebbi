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
        self.xmaxx = u.xmax
        #Hæsta y gildi svæðis
        self.ymaxx = u.ymax
        #Lægsta x gildi svæðis
        self.xmin = 0
        #Lægsta y gildi svæðis
        self.ymin = 0

    #Búum til svæði og teiknum hópa
    def svaedi_hopar(self):
        #Fjöldi reita x
        l = 4
        #Fjöldi svæða y
        m = 2
        #Heildarfjöldi svæða
        k = 8

        #Fjöldi fólks í hóp
        self.n = 20

        #Búum til svæði
        for i in range(l):
            self.xmaxx = u.xmax - (l-1-i)*u.xmax/l
            self.xmin = i*(u.xmax/l)
            for j in range(m):
                self.ymaxx = u.ymax - (m-1-j)*u.ymax/m
                self.ymin = j*(u.ymax/m)
                print(self.xmaxx,self.ymaxx,self.xmin,self.ymin)
                #pygame.draw.rect(u.windowSurface, u.BLACK, (self.z, self.w, self.x-self.z, self.y-self.w),0)
            self.people()
            
    def svaedaskopp(self,e):
        if e.x < self.xmin+u.radius or e.x > self.xmaxx-u.radius:
            e.vx = -1 * e.vx
        if e.y < self.ymin+u.radius or e.y > self.ymaxx-u.radius:
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
