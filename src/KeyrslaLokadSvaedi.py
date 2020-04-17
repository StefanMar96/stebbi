import sys
import pygame
from pygame.locals import *
import Uppsetning as U
import Hopur as H

class KeyrslaLokadSvaedi():
    def keyrslalokadsvaedi(self, n, LikurByrja, LikurSmit):
    
        #SET UP PYGAME
        pygame.init()

        #SET UP WINDOW
        pygame.display.set_caption('Covid-19 hermir')
        FRAMES_PER_SECOND = 30
        fpsClock = pygame.time.Clock()

        h = H.Hopur()
        u = U.Uppsetning()
        h.upphafsstilling(n, LikurByrja, LikurSmit)
        h.einstaklingar()

        #Staðsetning sýktra á lokuðu svæði
        h.syktir_location()

        fontTeljarar = pygame.font.Font('freesansbold.ttf', 14)

        fjoldiH = fontTeljarar.render('Fjöldi heilbrigðra:', True, u.HEILBRIGDUR, u.HVITUR)
        fjoldiS = fontTeljarar.render('Fjöldi sýktra:', True, u.SYKTUR, u.HVITUR)
        fjoldiB = fontTeljarar.render('Fjöldi óvirkra smita:', True, u.BATNAD, u.HVITUR)
        fjoldiL = fontTeljarar.render('Fjöldi látinna:', True, u.LATNIR, u.HVITUR)

        textRect6 = fjoldiH.get_rect() 
        textRect6.center = (700,615)

        textRect7 = fjoldiS.get_rect() 
        textRect7.center = (700,655)

        textRect9 = fjoldiB.get_rect() 
        textRect9.center = (700,695)

        textRect10 = fjoldiL.get_rect() 
        textRect10.center = (700,735)

        def talningar_display(gildi1,gildi2,gildi3,gildi4,gildi5):
            s1 = fontTeljarar.render(str(gildi1), True, u.HEILBRIGDUR)
            s2 = fontTeljarar.render(str(gildi2), True, u.SYKTUR)
            s4 = fontTeljarar.render(str(gildi4), True, u.BATNAD)
            s5 = fontTeljarar.render(str(gildi5), True, u.LATNIR)
            u.windowSurface.blit(s1,[900,615])
            u.windowSurface.blit(s2,[900,655])
            u.windowSurface.blit(s4,[900,695])
            u.windowSurface.blit(s5,[900,735])

        #Aðal loopan
        while True:

            #clear screen
            u.windowSurface.fill(u.HVITUR)
            pygame.draw.line(u.windowSurface, u.LATNIR, (200, 600), (200, 0), 1)

            #Línur sem skilur hermun frá tölulegum upplýsingum
            pygame.draw.line(u.windowSurface, u.LATNIR, (600, 750), (600, 0), 1)
            pygame.draw.line(u.windowSurface, u.LATNIR, (0, 600), (1000, 600), 1)

            u.windowSurface.blit(fjoldiH, textRect6)
            u.windowSurface.blit(fjoldiS, textRect7)
            u.windowSurface.blit(fjoldiB, textRect9)
            u.windowSurface.blit(fjoldiL, textRect10)
                
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

            h.talningar()

            talningar_display(h.teljaheilbrigda,h.teljasykta,h.teljaeinangrun,h.teljabatnad,h.teljalatna)

            #event handling
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            fpsClock.tick(FRAMES_PER_SECOND)
