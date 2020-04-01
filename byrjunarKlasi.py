
import sys
import math
import numpy as np
import pygame
from SmitOpnuSvaeði import SmitOpnuSvaeði
from pygame.locals import *

#tónlist
#music = pygame.mixer.music.load("music.mp3")
#pygame.mixer.music.play()

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

#um kúlur
radius = 5
radius_x = radius/xmax
radius_y = radius/ymax


#BREYTILEGT
n=50 #number of points
n_infected = 5 #number of infected
n_total = n + n_infected
speed = 0.01

einstaklilngar = []
for i in range(n_total):
    einstaklilngar.append(Einstaklingur(x, y, vx, vy))


class Einstaklingur:
    self.x = 0
    self.y = 0
    self.vx = 0
    self.vy = 0
    self.infected  = 0

    def __init__(self):
        self.x = np.random.rand()
        self.y = np.random.rand()
        self.vx = speed * np.random.rand()
        self.vy = speed * np.random.rand()
    

    def draw(self):
        if infected[i] == 0:
            pygame.draw.circle(windowSurface, BLUE, \
                                (int(xmax * x[i]), int(ymax * y[i])), radius, 0)
        else:
            pygame.draw.circle(windowSurface, ORANGE, \
                                (int(xmax * x[i]), int(ymax * y[i])), radius, 0)


    def move(self):
        #Skoppa af vegg
        if x[i] < radius_x or x[i] > 1-radius_x:
            vx[i] = -1 * vx[i]
        if y[i] < radius_y or y[i] > 1-radius_y:
            vy[i] = -1 * vy[i]


    def infect(self):




#aðal loopan
while True:
    #clear screen
    windowSurface.fill(WHITE)

    for i in range(n_total):
        einstaklilngar[i].move()

    for i in range(n_total):
        for j in range(i+1,n_total):
            #...skoppa saman

    for i in range(n_total):
        einstaklilngar[i].draw()







    #UPDATE POSITIONS                
    for i in range(n_total):
        #SKOPPA AF VEGG


            
        for j in range(i+1, n_total):
            distance = math.hypot(int(x[i] * xmax) - int(x[j] * xmax), int(y[i] * ymax)- int(y[j]* ymax))
            if distance <= 2*radius:
                vx[j] = -1 * vx[j]
                vy[j] = -1 * vy[j]
                vx[i] = -1 * vx[i]
                vy[i] = -1 * vy[i]
                if infected[i] == 1 and SmitOpnuSvaeði.roll_dice() == True:
                    infected[j] = 1
                if infected[j] == 1 and SmitOpnuSvaeði.roll_dice() == True:
                    infected[i] = 1
                    
                    
        x[i] += vx[i]
        y[i] += vy[i]
        
    
    #redraw
    for i in range(n_total):
        #teikna

    
    #event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FRAMES_PER_SECOND)