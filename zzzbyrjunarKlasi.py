import sys
import math
import numpy as np
import pygame
from SmitOpnuSvaeði import SmitOpnuSvaeði
from pygame.locals import *

#SET UP COLORS
WHITE = (255, 255, 255)#bakgrunnur
BLUE = (0, 0, 255)#heilbrigðir
ORANGE = (255, 153, 51)#veikir
PINK = (255, 0, 255)#ekki lengur veikir
BLACK = (0, 0, 0) #Látnir


class Einstaklingur:

    # breytur
    self.x = 0
    # ...
    
    # föll
    def __init(__self):
        self.x = np.random.rand()

    def draw(self):
    def move(self):
    def infect(self):


class Byrjun:
    def keyrsla(self):

        #SET UP PYGAME
        pygame.init()
        
        #SET UP WINDOW
        self.xmax = 800 
        self.ymax = 400 
        self.windowSurface = pygame.display.set_mode((self.xmax, self.ymax))
        pygame.display.set_caption('Covid-19 hermir')

        FRAMES_PER_SECOND = 30
        fpsClock = pygame.time.Clock()
        
        self.n=5 #number of points
        self.n_infected = 5 #number of infected
        self.n_total = n + n_infected
        speed = 0.01
        self.radius = 5
        self.radius_x = radius/xmax
        self.radius_y = radius/ymax
        

        #allir byrja random
        self.x = np.random.rand(n_total)
        self.y = np.random.rand(n_total)

        #hraði er random?
        self.vx = speed * np.random.rand(n_total)
        self.vy = speed * np.random.rand(n_total)

        #Hverjir eru sýktir
        self.infected  = []
        for i in range(n):
            infected.append(0)
        for i in range(n_infected):
            infected.append(1)
        

        #tónlist
        #music = pygame.mixer.music.load("music.mp3")
        #pygame.mixer.music.play()
        
        #aðal loopan
        while True:
            #clear screen
            windowSurface.fill(WHITE)
            UPDATE_POSITION(self)
            draw(self)


    def UPDATE_POSITIONS(self):                
        for i in range(self.n_total):
            #SKOPPA AF VEGG
            if self.x[i] < self.radius_x or self.x[i] > 1-self.radius_x:
                self.vx[i] = -1 * self.vx[i]
            if self.y[i] < self.radius_y or self.y[i] > 1-self.radius_y:
                self.vy[i] = -1 * self.vy[i]

                
            adrir_boltar = n_total-i-1
            for j in range(adrir_boltar):
                distance = math.hypot(int(self.x[i] * self.xmax) - int(self.x[j+i+1] * self.xmax), int(self.y[i] * self.ymax)- int(self.y[j+i+1]* self.ymax))
                if distance <= 2*self.radius:
                    self.vx[i+j+1] = -1 * self.vx[i+j+1]
                    self.vy[i+j+1] = -1 * self.vy[i+j+1]
                    self.vx[i] = -1 * self.vx[i]
                    self.vy[i] = -1 * self.vy[i]
                    if self.infected[i] == 1 and SmitOpnuSvaeði.roll_dice() == True:
                        self.infected[j+i+1] = 1
                    if self.infected[j+i+1] == 1 and SmitOpnuSvaeði.roll_dice() == True:
                        self.infected[i] = 1
            self.x[i] += self.vx[i]
            self.y[i] += self.vy[i]
            
        
        #redraw
    def draw(self):
        for i in range(n_total):
            if self.infected[i] == 0:
                pygame.draw.circle(self.windowSurface, self.BLUE, \
                                    (int(self.xmax * self.x[i]), int(self.ymax * self.y[i])), self.radius, 0)
            else:
                pygame.draw.circle(self.windowSurface, self.ORANGE, \
                                    (int(self.xmax * self.x[i]), int(self.ymax * self.y[i])), self.radius, 0)
            
        
        #event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FRAMES_PER_SECOND)
        
