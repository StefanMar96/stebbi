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
        self.n=50 #number of points

        #Listi af einstaklingum
        self.einstaklingur = []

        self.svaedi = []

        #Hæsta x gildi svæðis
        self.x = u.xmax
        #Hæsta y gildi svæðis
        self.y = u.ymax
        #Lægsta x gildi svæðis
        self.z = 0
        #Lægsta y gildi svæðis
        self.w = 0

    #Búum til svæði og teiknum hópa
    def svaedi(self):
        #Fjöldi reita x
        l = 4
        #Fjöldi svæða y
        m = 2

        #Fjöldi fólks í hóp
        self.n = 20

        #Búum til svæði
        for i in range(l):
            self.x = u.xmax - (m-1-i)*u.xmax/l
            self.z = i*(u.xmax/l)
            for j in range(m):
                self.y = u.ymax - (m-1-i)*u.ymax/m
                self.w = i*(u.ymax/m)
            s = self.Svaedi(self.x, self.y, self.z, self.w)
            self.svaedi.append(s)
            self.people()
            
    #Búum til n marga einstaklinga á opnu svæði
    def people(self):
        for i in range(self.n):
            e = E.Einstaklingur(self.x, self.y, self.z, self.w, u.radius)
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
                    einstaklingur[i].sykist()
