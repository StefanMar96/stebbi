import sys
#import numpy as np
import random
import pygame
from pygame.locals import *
import math

class Uppsetning():

    def __init__(self):
        self.WHITE = (255, 255, 255)#bakgrunnur
        self.BLUE = (0, 0, 255)#heilbrigðir
        self.ORANGE = (255, 153, 51)#veikir
        self.PINK = (255, 0, 255)#ekki lengur veikir
        self.BLACK = (0, 0, 0) #látnir 

        self.radius = 5
        self.xmax = 800 
        self.ymax = 400 
        self.windowSurface = pygame.display.set_mode((self.xmax, self.ymax))