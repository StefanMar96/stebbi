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

    #Færa í sér klasa, gera þar fall með árekstur, sá klasi höndlar 1 svæði
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

    ###Hingað

    ##Kalla á föllin fyrir hópana, í hópunum kalla á einstakling
    #Aðal loopan
    while True:

        #clear screen
        u.windowSurface.fill(u.WHITE)

        telja = 0

        #UPDATE POSITIONS
        for i in range(n):
            for j in range(i+1,n):
                distance = math.hypot(einstaklingur[i].x - einstaklingur[j].x, einstaklingur[i].y - einstaklingur[j].y)
                if distance <= 2*u.radius:
                    einstaklingur[j].vx = -1 * einstaklingur[j].vx        
                    einstaklingur[j].vy = -1 * einstaklingur[j].vy
                    einstaklingur[i].vx = -1 * einstaklingur[i].vx
                    einstaklingur[i].vy = -1 * einstaklingur[i].vy


            #SKOPPA AF VEGG
            e = einstaklingur[i]
            e.veggskopp(e)

            #Færa leikmenn á borði
            e.move(e)

            #Teikna einstaklinga
            e.teikna(e.x,e.y,u.radius)
            
        #event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FRAMES_PER_SECOND)