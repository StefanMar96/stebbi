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
        self.x = random.randint(radius, x-radius)
        self.y = random.randint(radius, y-radius)
        self.vx = random.randrange(-2, 3)
        self.vy = random.randrange(-2, 3)
        self.litur = u.BLUE
        self.syktur()

    #Þetta fall ákvarðar hve margir byrja sýktir, breyta?
    def syktur(self):
        number = random.randint(1, 100)
        if number >= 95:
            self.litur = u.ORANGE

    #Þetta fall teiknar kúlurnar
    def teikna(self,x,y,radius):
        pygame.draw.circle(u.windowSurface, self.litur, (x,y), u.radius, 0)

    #Færa kúlur á borði
    def move(self, e):
        e.x += e.vx
        e.y += e.vy

    #Boltar skoppa af veggjum
    def veggskopp(self, e):
        if e.x < u.radius or e.x > u.xmax-u.radius:
            e.vx = -1 * e.vx
        if e.y < u.radius or e.y > u.ymax-u.radius:
            e.vy = -1 * e.vy


