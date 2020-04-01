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
BLACK = (0, 0, 0) #látnir 

#SET UP PYGAME
pygame.init()

#SET UP WINDOW
xmax = 800 
ymax = 400 
windowSurface = pygame.display.set_mode((xmax, ymax))
pygame.display.set_caption('Covid-19 hermir')

FRAMES_PER_SECOND = 30
fpsClock = pygame.time.Clock()

n=50 #number of points
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

einstaklingar = []
for i in range(n_total):
    einstaklingar.append(Einstaklingur(...))

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

    for i in range(n_total):
        einstaklingar[i].move()

    for i in range(n_total):
        for j in range(i+1,n_total):
            # ...

    for i in range(n_total):
        einstaklingar[i].draw()

    #UPDATE POSITIONS                
    for i in range(n_total):
        #SKOPPA AF VEGG
        if x[i] < radius_x or x[i] > 1-radius_x:
            vx[i] = -1 * vx[i]
        if y[i] < radius_y or y[i] > 1-radius_y:
            vy[i] = -1 * vy[i]

            
        #adrir_boltar = n_total-i-1
        #for j in range(adrir_boltar):
        for j in range(i+1, n_total):
            distance = math.hypot(int(xmax*(x[i] - x[j])), int(ymax*(y[i] - y[j])))
            if distance <= 2*radius:
                vx[j] = -1 * vx[j]
                vy[j] = -1 * vy[j]
                vx[i] = -1 * vx[i]
                vy[i] = -1 * vy[i]
                #if infected[i] == 1 and SmitOpnuSvaeði.roll_dice() == True:
                #    infected[j+i+1] = 1
                #if infected[j+i+1] == 1 and SmitOpnuSvaeði.roll_dice() == True:
                #    infected[i] = 1
                    
    for i in range(n_total):
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
