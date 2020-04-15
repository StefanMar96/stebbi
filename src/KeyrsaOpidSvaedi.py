import sys
import pygame
from pygame.locals import *
import Uppsetning as U
import Hopur as H

h = H.Hopur()
u = U.Uppsetning()

FRAMES_PER_SECOND = 30
fpsClock = pygame.time.Clock()

#SET UP PYGAME
pygame.init()

#SET UP WINDOW
pygame.display.set_caption('Covid-19 hermir')

h.einstaklingar()

#Aðal loopan
while True:

    #clear screen
    u.windowSurface.fill(u.HVITUR)

    #Lína sem skilur hermun frá tölulegum upplýsingum
    pygame.draw.line(u.windowSurface, u.LATNIR, (600, 600), (600, 0), 1)

    #Færa leikmenn á borði
    h.faera()

    #Teikna einstaklinga
    h.teikna()

    #SKOPPA AF VEGG
    h.veggskopp()

    #Látum bolta skoppa af hvor öðrum
    h.arekstur()

    #Skoðum breytingu á tíma frá smiti
    h.breyting_timi()

    #Talningar á ástandi einstaklinga
    h.talningar()
        
    #event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FRAMES_PER_SECOND)
    
