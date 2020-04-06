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
    #Búum til hlut af klasanum
    u = U.Uppsetning()

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
        if e.x < e.radius or e.x > u.xmax-u.radius:
            e.vx = -1 * e.vx
        if e.y < e.radius or e.y > u.ymax-u.radius:
            e.vy = -1 * e.vy

    #def arekstur(self,e,einstaklingur):
        
            
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
    einstaklingur = []

    #Búum til hlut af klasanum Uppsetning
    u = U.Uppsetning()

    #Búum til n marga einstaklinga
    for i in range(n):
        e = E.Einstaklingur(u.xmax, u.ymax, u.radius)
        einstaklingur.append(e)

    #Aðal loopan
    while True:

        #clear screen
        u.windowSurface.fill(u.WHITE)

        telja = 0

        #UPDATE POSITIONS                
        for e in einstaklingur:

            telja +=1
            #Skoppa af boltum
            #e.arekstur(e,einstaklingur)
                #if i.litur == u.ORANGE:
                 #   j.litur == u.ORANGE
    
            for j in range(telja+1,n):
                e2 = einstaklingur[j]
                distance = math.hypot(int(e.x * u.xmax) - int(e2.x * u.xmax), int(e.y * u.ymax)- int(e2.y* u.ymax))
                if distance <= 2*u.radius:
                    e2.vx = -1 * e2.vx        
                    e2.vy = -1 * e2.vy
                    e.vx = -1 * e.vx
                    e.vy = -1 * e.vy

            #SKOPPA AF VEGG
            e.veggskopp(e)

            #Færa leikmenn á borði
            e.move(e)

            #Teikna einstaklinga
            e.teikna(e.x,e.y,e.radius)
            
        #event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FRAMES_PER_SECOND)