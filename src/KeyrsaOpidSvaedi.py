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

    h.people()

    #Aðal loopan
    while True:

        #clear screen
        u.windowSurface.fill(u.WHITE)

        #Keyrum smit á opnu svæði
        for e in h.einstaklingur:

            #SKOPPA AF VEGG
            h.veggskopp(e)

            #Færa leikmenn á borði
            e.move(e)

            #Teikna einstaklinga
            e.teikna(e.x,e.y,u.radius)

            #breyting
            e.breyting(e)
            
        #Látum bolta skoppa af hvor öðrum
        h.arekstur(h.einstaklingur)
        
        #event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FRAMES_PER_SECOND)
