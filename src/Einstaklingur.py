import sys
import random
import pygame
from pygame.locals import *
import math
import Uppsetning as U

#Búum til hlut af uppsetning klasanum
u = U.Uppsetning()

class Einstaklingur():

    def __init__(self,x,y,radius):
        self.x = random.randrange(radius, x-radius)
        self.y = random.randrange(radius, y-radius)
        self.vx = random.randrange(-3, 3)
        self.vy = random.randrange(-3, 3)
        self.litur = u.HEILBRIGDUR
        self.byrjar_syktur()
        self.timi = 0

    #Þetta fall ákvarðar hve margir byrja sýktir, breyta?
    def byrjar_syktur(self):
        number = u.random_tala()
        if number >= 95:
            self.litur = u.SYKTUR
            self.timi=pygame.time.get_ticks()


    #Fall sem ákvarðar hvort einstaklingur smitast við árekstur
    def sykist(self):
        number = u.random_tala()
        if number >= 50:
            self.litur = u.SYKTUR
            self.timi=pygame.time.get_ticks()
#            self.breyting()

    def breyting_timi(self):
        seconds=(pygame.time.get_ticks()-self.timi)/1000
        if(self.litur == u.SYKTUR):
            if seconds>20:
                number = u.random_tala()
                if number > 5:
                    self.litur = u.BATNAD
                else:
                    self.litur = u.LATNIR

    #Þetta fall teiknar kúlurnar
    def teikna(self):
        pygame.draw.circle(u.windowSurface, self.litur, (self.x,self.y), u.radius, 0)

    #Færa kúlur á borði
    def faera(self):
        if(self.litur!=u.LATNIR):
            self.x += self.vx
            self.y += self.vy




