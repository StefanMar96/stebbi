import sys
#import numpy as np
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
        self.litur = u.BLUE
        self.byrjar_syktur()
        self.timi = 0

    #Þetta fall ákvarðar hve margir byrja sýktir, breyta?
    def byrjar_syktur(self):
        number = random.randint(1, 100)
        if number >= 95:
            self.litur = u.ORANGE
            self.timi=pygame.time.get_ticks()


    #Fall sem ákvarðar hvort einstaklingur smitast við árekstur
    def sykist(self):
        number = random.randint(1, 100)
        if number >= 50:
            self.litur = u.ORANGE
            self.timi=pygame.time.get_ticks()
#            self.breyting()

    def breyting(self, e):
        seconds=(pygame.time.get_ticks()-self.timi)/1000
        if(self.litur == u.ORANGE):
            if seconds>20:
                number = random.randint(1, 100)
                if number > 5:
                    self.litur = u.PINK
                else:
                    self.litur = u.BLACK

    #Þetta fall teiknar kúlurnar
    def teikna(self,x,y,radius):
        pygame.draw.circle(u.windowSurface, self.litur, (x,y), u.radius, 0)

    #Færa kúlur á borði
    def move(self, e):
        if(self.litur!=u.BLACK):
            e.x += e.vx
            e.y += e.vy




