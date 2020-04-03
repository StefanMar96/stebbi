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


class Einstaklingur():

    import Uppsetning as U
    u = U.Uppsetning()

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
            
class Keyrsla:

    import Einstaklingur as E
    import Uppsetning as U
    u = U.Uppsetning()

    #SET UP PYGAME
    pygame.init()

    #SET UP WINDOW
    pygame.display.set_caption('Covid-19 hermir')
    FRAMES_PER_SECOND = 30
    fpsClock = pygame.time.Clock()

    #BREYTILEGT
    n=50 #number of points

    #Listi af einstaklingum
    einstaklilngur = []

    #Búum til hlut af klasanum Uppsetning
    u = U.Uppsetning()

    #Búum til n marga einstaklinga
    for i in range(n):
        e = E.Einstaklingur(u.xmax, u.ymax, u.radius)
        einstaklilngur.append(e)

    #Aðal loopan
    while True:

        #clear screen
        u.windowSurface.fill(u.WHITE)

        #UPDATE POSITIONS                
        for e in einstaklilngur:

            #Færa leikmenn á borði
            e.move(e)

            #SKOPPA AF VEGG
            e.veggskopp(e)

            #Teikna einstaklinga
            e.teikna(e.x,e.y,e.radius)

            #SKOPPA AF ÖÐRUM
            #adrir_boltar = n_total-i-1
            #for j in range(e+1, n):
            #   distance = math.hypot(int(e.x * xmax) - int(j.x * xmax), int(e.y * ymax)- int(j.y* ymax))
            #  if distance <= 2*e.radius:
            #     j.vx = -1 * j.vx
                #    j.vy = -1 * j.vy
                #   e.vx = -1 * i.vx
                #  e.vy = -1 * i.vy
                    #if infected[i] == 1 and SmitOpnuSvaeði.roll_dice() == True:
                    #   infected[j] = 1
                    #if infected[j] == 1 and SmitOpnuSvaeði.roll_dice() == True:
                    #   infected[i] = 1
                
            
        #event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FRAMES_PER_SECOND)