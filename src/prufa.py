import sys
import numpy as np
import pygame
from pygame.locals import *

#SET UP COLORS
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

#SET UP PYGAME
pygame.init()

#SET UP WINDOW
xmax = 600
ymax = 400
windowSurface = pygame.display.set_mode((xmax, ymax))
pygame.display.set_caption('Covid-19 hermir')

FRAMES_PER_SECOND = 30
fpsClock = pygame.time.Clock()

n=50 #number of points
frozen = 0.5 #prósenta frosna
p_unfreeze = 0.01 #líkur að hætta vera frosinn
speed = 0.01
radius = 5

#allir byrja random
x = np.random.rand(n)
y = np.random.rand(n)

#hraði er random?
vx = speed * np.random.rand(n)
vy = speed * np.random.rand(n)
for i in range(int(frozen*n)):
    vx[i] = 0
    vy[i] = 0

#aðal loopan
while True:
    #clear screen
    windowSurface.fill(WHITE)


    #UPDATE POSITIONS
    for i in range(n):
        #SKOPPA AF VEGG
        if x[i] < 0 or x[i] > 1:
            vx[i] = -1 * vx[i]
        if y[i] < 0 or y[i] > 1:
            vy[i] = -1 * vy[i]
        x[i] += vx[i]
        y[i] += vy[i]

        #þegar frosnir fara að hreyfast
        if vx[i] == 0 and vy[i] == 0 and np.random.rand() < p_unfreeze:
            vx[i] = speed * np.random.rand()
            vy[i] = speed * np.random.rand()
    
    #redraw
    for i in range(n):
        pygame.draw.circle(windowSurface, BLUE, \
                            (int(xmax * x[i]), int(ymax * y[i])), radius, 0)
    
    #event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FRAMES_PER_SECOND)
    