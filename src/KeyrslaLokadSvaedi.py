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

h.einstaklingar()

#Staðsetning sýktra á lokuðu svæði
h.syktir_location()

#Aðal loopan
while True:

    #clear screen
    u.windowSurface.fill(u.HVITUR)
    pygame.draw.line(u.windowSurface, u.LATNIR, (250, 400), (250, 0), 1)
        
    #Færa leikmenn á borði
    h.faera()

    #Teikna einstaklinga
    h.teikna()

    #SKOPPA AF VEGG
    h.veggskopp()

    #Skoðum breytingu á tíma frá smiti
    h.breyting_timi()
            
    #Látum bolta skoppa af hvor öðrum
    h.arekstur()

    #SKOPPA AF SVÆÐI
    h.svaedaskopp_eitt_svaedi()

    #event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FRAMES_PER_SECOND)
