import sys
import math
import numpy as np
import pygame
#from SmitOpnuSvaeði import SmitOpnuSvaeði
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
    
    n=60 #number of points
    n_infected = 3 #number of infected
    n_total = n + n_infected
    speed = 0.005
    radius = 5
    radius_x = radius/xmax
    radius_y = radius/ymax
    r=4
    

    #allir byrja random
    x_infected = np.random.rand(n_infected)
    y_infected = np.random.rand(n_infected)

    #position of infected in the end
    
    x = np.random.rand(n)
    y = np.random.rand(n)

    #hraði er random?
    vx = speed * np.random.rand(n)
    vy = speed * np.random.rand(n)

    vx_infected = speed * np.random.rand(n_infected)
    vy_infected = speed * np.random.rand(n_infected)
    

    #tónlist
    #music = pygame.mixer.music.load("music.mp3")
    #pygame.mixer.music.play()
    
    #aðal loopan
    while True:
        #clear screen
        windowSurface.fill(WHITE)


        #UPDATE POSITIONS                
        for i in range(n):
            #SKOPPA AF VEGG
            if x[i] < radius_x or x[i] > 1-radius_x:
                vx[i] = -1 * vx[i]
            if y[i] < radius_y or y[i] > 1-radius_y:
                vy[i] = -1 * vy[i]
            for j in range(n_infected):
                
                distance = math.hypot(int(x[i] * xmax) - int(x_infected[j] * xmax), int(y[i] * ymax)- int(y_infected[j]* ymax))
                if distance <= 2*radius:
                    vx_infected[j] = -1 * vx_infected[j]
                    vy_infected[j] = -1 * vy_infected[j]
                    vx[i] = -1 * vx[i]
                    vy[i] = -1 * vy[i]
                    
                    if (r==4):
                        x_infected.append(x[i])
                        x.delete(i)
                        y_infected.append(y[i])
                        y.delete(i)
                        vx_infected.append(vx[i])
                        vx.delete(i)
                        vy_infected.append(vy[i])
                        vy.delete(i)
                        
                        
            x[i] += vx[i]
            y[i] += vy[i]

        for i in range(n_infected):
            if x_infected[i] < radius_x or x_infected[i] > 1-radius_x:
                vx_infected[i] = -1 * vx_infected[i]
            if y_infected[i] < radius_y or y_infected[i] > 1-radius_y:
                vy_infected[i] = -1 * vy_infected[i]
            x_infected[i] += vx_infected[i]
            y_infected[i] += vy_infected[i]
            

        
        #redraw
        for i in range(n):
            pygame.draw.circle(windowSurface, BLUE, \
                                (int(xmax * x[i]), int(ymax * y[i])), radius, 0)
            
        for i in range(n_infected):
            pygame.draw.circle(windowSurface, ORANGE, \
                                (int(xmax * x_infected[i]), int(ymax * y_infected[i])), radius, 0)
        
        #event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FRAMES_PER_SECOND)

