import sys
import math
import numpy as np
import pygame
from SmitOpnuSvaeði import SmitOpnuSvaeði
from pygame.locals import *

class Byrjun:
    #SET UP COLORS
    WHITE = (255, 255, 255)#bakgrunnur
    BLUE = (0, 0, 255)#heilbrigðir
    ORANGE = (255, 153, 51)#veikir
    PINK = (255, 0, 255)#ekki lengur veikir

    #SET UP PYGAME
    pygame.init()
    
    #SET UP WINDOW
    xmax = 800 
    ymax = 400 
    windowSurface = pygame.display.set_mode((xmax, ymax))
    pygame.display.set_caption('Covid-19 hermir')

    FRAMES_PER_SECOND = 30
    fpsClock = pygame.time.Clock()
    
    n=80 #number of points
    n_infected = 5 #number of infected
    n_total = n + n_infected
    speed = 0.01
    radius = 5
    radius_x = radius/xmax
    radius_y = radius/ymax
    

    #allir byrja random
    x = np.random.rand(n_total)
    y = np.random.rand(n_total)

    #hraði er random?
    vx = speed * np.random.rand(n_total)
    vy = speed * np.random.rand(n_total)

    #Hverjir eru sýktir
    infected  = []
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


        #UPDATE POSITIONS                
        for i in range(n_total):
            #SKOPPA AF VEGG
            if x[i] < radius_x or x[i] > 1-radius_x:
                vx[i] = -1 * vx[i]
            if y[i] < radius_y or y[i] > 1-radius_y:
                vy[i] = -1 * vy[i]

                
            adrir_boltar = n_total-i-1
            for j in range(adrir_boltar):
                distance = math.hypot(int(x[i] * xmax) - int(x[j+i+1] * xmax), int(y[i] * ymax)- int(y[j+i+1]* ymax))
                if distance <= 2*radius:
                    vx[i+j+1] = -1 * vx[i+j+1]
                    vy[i+j+1] = -1 * vy[i+j+1]
                    vx[i] = -1 * vx[i]
                    vy[i] = -1 * vy[i]
                    if infected[i] == 1: # and SmitOpnuSvaeði == True:
                        infected[j+i+1] = 1
                    if infected[j+i+1] == 1: # and SmitOpnuSvaeði == True:
                        infected[i] = 1
            x[i] += vx[i]
            y[i] += vy[i]
            
        
        #redraw
        for i in range(n_total):
            if infected[i] == 0:
                pygame.draw.circle(windowSurface, BLUE, \
                                    (int(xmax * x[i]), int(ymax * y[i])), radius, 0)
            else:
                pygame.draw.circle(windowSurface, ORANGE, \
                                    (int(xmax * x[i]), int(ymax * y[i])), radius, 0)
        
        #event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FRAMES_PER_SECOND)
