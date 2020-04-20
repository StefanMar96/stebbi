import sys
import random
import pygame
from pygame.locals import *
import math

class Uppsetning():

    def __init__(self):
        self.HVITUR = (255, 255, 255) #bakgrunnur
        self.HEILBRIGDUR = (0, 0, 255) #heilbrigðir
        self.SYKTUR = (255, 153, 51) #veikir
        self.BATNAD = (255, 0, 255) #ekki lengur veikir
        self.LATNIR = (0, 0, 0) #látnir 
        self.EINANGRUN = (255,0,0) #Einstaklingar í einangrun

        self.radius = 5 #Radíus kúlanna sem tákna einstaklinga

        #Hnit borðsins sem hermunin er inná
        self.xBORD = 600 
        self.yBORD = 600 

        #Hnit alls skjásins
        self.xSkjar = 1000
        self.ySkjar = 750

        #Birting á rammanum
        self.windowSurface = pygame.display.set_mode((self.xSkjar, self.ySkjar))

    #Fall sem skilar random tölu
    def random_tala(self):
        number = random.randint(1, 100)
        return number
