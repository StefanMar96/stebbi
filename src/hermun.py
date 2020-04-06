import sys
import random
import pygame
from pygame.locals import *
import math
import Einstaklingur as E
import Uppsetning as U

class Keyrsla:

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
        for i,j in einstaklingur:
            distance = math.hypot(int(i.x * u.xmax) - int(j.x * u.xmax), int(i.y * u.ymax)- int(j.y* u.ymax))
            if distance <= 2*e.radius:
                j.vx = -1 * j.vx        
                j.vy = -1 * j.vy
                i.vx = -1 * i.vx
                i.vy = -1 * i.vy
                #if i.litur == u.ORANGE:
                 #   j.litur == u.ORANGE
                
            
        #event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FRAMES_PER_SECOND)