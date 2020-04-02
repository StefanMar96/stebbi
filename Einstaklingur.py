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
        self.y = random.randint(radius, y-radius)
        self.radius = radius
        self.vx = random.randrange(-2, 3)
        self.vy = random.randrange(-2, 3)
        self.litur = u.BLUE
        self.syktur()
        #self.teikna(self.x,self.y,self.radius)

    def syktur(self):
        number = random.randint(1, 100)
        if number >= 95:
            self.litur = u.ORANGE

    def teikna(self,x,y,radius):
        pygame.draw.circle(u.windowSurface, self.litur, (x,y), radius, 0)

    def move(self, e):
        e.x += e.vx
        e.y += e.vy

    def veggskopp(self, e):
        if e.x < e.radius or e.x > u.xmax-e.radius:
            e.vx = -1 * e.vx
        if e.y < e.radius or e.y > u.ymax-e.radius:
            e.vy = -1 * e.vy