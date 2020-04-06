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

    #Þetta fall ákvarðar hve margir byrja sýktir, breyta?
    def byrjar_syktur(self):
        number = random.randint(1, 100)
        if number >= 60:
            self.litur = u.ORANGE

    #Fall sem ákvarðar hvort einstaklingur smitast við árekstur
    def sykist(self):
        number = random.randint(1, 100)
        if number >= 50:
            self.litur = u.ORANGE

    #Þetta fall teiknar kúlurnar
    def teikna(self,x,y,radius):
        pygame.draw.circle(u.windowSurface, self.litur, (x,y), u.radius, 0)

    #Færa kúlur á borði
    def move(self, e):
        e.x += e.vx
        e.y += e.vy



