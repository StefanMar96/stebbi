import sys
import pygame
from pygame.locals import *
import Uppsetning as U
import Hopur as H

#SET UP PYGAME
pygame.init()

#SET UP WINDOW
pygame.display.set_caption('Covid-19 hermir')
FRAMES_PER_SECOND = 30
fpsClock = pygame.time.Clock()

h = H.Hopur()
u = U.Uppsetning()

h.fjogur_svaedi_hopar()
h.einstaklingar()

#Aðal loopan
while True:

    #clear screen
    u.windowSurface.fill(u.HVITUR)
    pygame.draw.line(u.windowSurface, u.LATNIR, (400, 0), (400, 400), 1)
    pygame.draw.line(u.windowSurface, u.LATNIR, (0, 200), (800, 200), 1)

    #SKOPPA AF VEGG
    h.svaedaskopp_fjogur_svaedi()

    #Færa leikmenn á borði
    h.faera()

    #Teikna einstaklinga
    h.teikna()

    #breyting
    h.breyting_timi()

    #Látum bolta skoppa af hvor öðrum
    h.arekstur()
           
    #event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FRAMES_PER_SECOND)
