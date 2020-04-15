import sys
import random
import pygame
from pygame.locals import *
import math

class Uppsetning():

    def __init__(self):
        self.HVITUR = (255, 255, 255)#bakgrunnur
        self.HEILBRIGDUR = (0, 0, 255)#heilbrigðir
        self.SYKTUR = (255, 153, 51)#veikir
        self.BATNAD = (255, 0, 255)#ekki lengur veikir
        self.LATNIR = (0, 0, 0) #látnir 

        self.radius = 5
        self.xBORD = 600 
        self.yBORD = 600 
        self.xSkjar = 1000
        self.ySkjar = 750
        self.windowSurface = pygame.display.set_mode((self.xSkjar, self.ySkjar))

    def random_tala(self):
        number = random.randint(1, 100)
        return number
