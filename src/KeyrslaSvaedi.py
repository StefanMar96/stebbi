import sys
import random
import pygame
from pygame.locals import *
import math
import Einstaklingur as E
import Uppsetning as U
import Hopur as H

class Keyrsla:

    #SET UP PYGAME
    pygame.init()

    #SET UP WINDOW
    pygame.display.set_caption('Covid-19 hermir')
    FRAMES_PER_SECOND = 30
    fpsClock = pygame.time.Clock()

    h = H.Hopur()
    u = U.Uppsetning()

    h.svaedi_hopar()

    #Aðal loopan
    while True:

        #clear screen
        u.windowSurface.fill(u.WHITE)
        pygame.draw.line(u.windowSurface, u.BLACK, (400, 0), (400, 400), 5)
        pygame.draw.line(u.windowSurface, u.BLACK, (0, 200), (800, 200), 5)
        print(h.xmaxx)

        #Keyrum smit á opnu svæði
        for e in h.einstaklingur:

            #SKOPPA AF VEGG
            h.svaedaskopp(e)

            #Færa leikmenn á borði
            e.move(e)

            #Teikna einstaklinga
            e.teikna(e.x,e.y,u.radius)

        #Látum bolta skoppa af hvor öðrum
        h.arekstur(h.einstaklingur)
           
        #event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FRAMES_PER_SECOND)
