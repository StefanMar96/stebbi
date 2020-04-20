import sys
import pygame
import numpy as np
from pygame.locals import *
import Uppsetning as U
import Hopur as H
import graphs as G

class KeyrslaOpidSvaedi():
    def keyrslaopidsvaedi(self, n, LikurByrja, LikurSmit):
        #Búum til hluti af klösunum
        h = H.Hopur()
        u = U.Uppsetning()
        g = G.graphs()

        #Búa til fylki fyrir talningu einstaklinga
        self.heilb_coord = []
        self.sykt_coord = []
        self.ein_coord = []
        self.batnad_coord = []
        self.latnir_coord = []
        self.t = []

        #Upphafsstillingar "leikborðs" og tíma
        FRAMES_PER_SECOND = 10
        fpsClock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption('Covid-19 hermir')

        #Gildin sem notandi velur send inn í forrit
        h.upphafsstilling(n, LikurByrja, LikurSmit)

        #Einstklingar búnir til
        h.einstaklingar()

        #-------------------------------------------------------
        #TEXTI Á SKJÁ
        fontTeljarar = pygame.font.Font('freesansbold.ttf', 14)
        fontFyrirsogn = pygame.font.Font('freesansbold.ttf', 24) 

        fjoldiH = fontTeljarar.render('Fjöldi heilbrigðra:', True, u.HEILBRIGDUR, u.HVITUR)
        fjoldiS = fontTeljarar.render('Fjöldi sýktra:', True, u.SYKTUR, u.HVITUR)
        fjoldiE = fontTeljarar.render('Fjöldi í einangrun:', True, u.EINANGRUN, u.HVITUR)
        fjoldiB = fontTeljarar.render('Fjöldi óvirkra smita:', True, u.BATNAD, u.HVITUR)
        fjoldiL = fontTeljarar.render('Fjöldi látinna:', True, u.LATNIR, u.HVITUR)

        textRect6 = fjoldiH.get_rect() 
        textRect6.center = (700,615)

        textRect7 = fjoldiS.get_rect() 
        textRect7.center = (700,645)

        textRect8 = fjoldiE.get_rect() 
        textRect8.center = (700,675)

        textRect9 = fjoldiB.get_rect() 
        textRect9.center = (700,705)

        textRect10 = fjoldiL.get_rect() 
        textRect10.center = (700,735)

        def lysing_display():
            name = fontFyrirsogn.render("Smit á opnu svæði", True, u.SYKTUR)
            s1 = fontTeljarar.render("Hermunin sýnir frá því þegar ekki hefur verið sett á", True, u.SYKTUR)
            s2 = fontTeljarar.render("samkomubann og allir einstaklingar eru frjálsir ferða", True, u.SYKTUR)
            s3 = fontTeljarar.render("sinna. Einstaklingar ferðast mishratt og sumir eru stopp,", True, u.SYKTUR)
            s4 = fontTeljarar.render("en það er einfaldlega gert til þess að hermunin", True, u.SYKTUR)
            s5 = fontTeljarar.render("endurspegli raunveruleikann sem best, sumir hanga", True, u.SYKTUR)
            s6 = fontTeljarar.render("mikið heima hjá sér á meðan aðrir eru mikið á ferðinni.", True, u.SYKTUR)
            s7 = fontTeljarar.render(" ", True, u.SYKTUR)
            s8 = fontTeljarar.render("Heilbrigðir einstaklingar eru táknaðir með bláu og", True, u.SYKTUR)
            s9 = fontTeljarar.render("þeir sem sýkjast af veirunni eru táknaðir með", True, u.SYKTUR)
            s10 = fontTeljarar.render("appelsínugulu. Ef einstaklingur greinist með veiruna", True, u.SYKTUR)
            s11 = fontTeljarar.render("er hann sendur í einangrun, en það gerist aldrei fyrr", True, u.SYKTUR)
            s12 = fontTeljarar.render("en hann hefur verið sýktur í einhvern tíma, og ekki er", True, u.SYKTUR)
            s13 = fontTeljarar.render("öruggt að einstaklingur greinist yfirhöfuð.", True, u.SYKTUR)
            s14 = fontTeljarar.render(" ", True, u.SYKTUR)
            s15 = fontTeljarar.render("Ef sýktur einstaklingur nær bata fær hann að fara", True, u.SYKTUR)
            s16 = fontTeljarar.render("aftur út í samfélagið, táknaður sem bleikur, en þá", True, u.SYKTUR)
            s17 = fontTeljarar.render("getur hann ekki smitast aftur. Ef svo ólíklega vill", True, u.SYKTUR)
            s18 = fontTeljarar.render("til að einstaklingur lætur lífið í baráttu sinni við", True, u.SYKTUR)
            s19 = fontTeljarar.render("veiruna litast hann svartur, stöðvast og aðrir", True, u.SYKTUR)
            s20 = fontTeljarar.render("einstaklingar komast ekki í snertingu við hann.", True, u.SYKTUR)

            u.windowSurface.blit(name,[605,15])
            u.windowSurface.blit(s1,[605,50])
            u.windowSurface.blit(s2,[605,70])
            u.windowSurface.blit(s3,[605,90])
            u.windowSurface.blit(s4,[605,110])
            u.windowSurface.blit(s5,[605,130])
            u.windowSurface.blit(s6,[605,150])
            u.windowSurface.blit(s7,[605,170])
            u.windowSurface.blit(s8,[605,190])
            u.windowSurface.blit(s9,[605,210])
            u.windowSurface.blit(s10,[605,230])
            u.windowSurface.blit(s11,[605,250])
            u.windowSurface.blit(s12,[605,270])
            u.windowSurface.blit(s13,[605,290])
            u.windowSurface.blit(s14,[605,310])
            u.windowSurface.blit(s15,[605,330])
            u.windowSurface.blit(s16,[605,350])
            u.windowSurface.blit(s17,[605,370])
            u.windowSurface.blit(s18,[605,390])
            u.windowSurface.blit(s19,[605,410])
            u.windowSurface.blit(s20,[605,430])

        #Setja upp til að birta talningar á skjá
        def talningar_display(gildi1,gildi2,gildi3,gildi4,gildi5):
            s1 = fontTeljarar.render(str(gildi1), True, u.HEILBRIGDUR)
            s2 = fontTeljarar.render(str(gildi2), True, u.SYKTUR)
            s3 = fontTeljarar.render(str(gildi3), True, u.EINANGRUN)
            s4 = fontTeljarar.render(str(gildi4), True, u.BATNAD)
            s5 = fontTeljarar.render(str(gildi5), True, u.LATNIR)
            u.windowSurface.blit(s1,[900,615])
            u.windowSurface.blit(s2,[900,645])
            u.windowSurface.blit(s3,[900,675])
            u.windowSurface.blit(s4,[900,705])
            u.windowSurface.blit(s5,[900,735])
        #-------------------------------------------------------    
        
        #Upphafsstilling á gildi fyrir graf
        t=0

        #Aðal loopan
        while True:

            #Hreinsa skjáinn
            u.windowSurface.fill(u.HVITUR)

            #Línur sem skilja hermun frá tölulegum upplýsingum
            pygame.draw.line(u.windowSurface, u.LATNIR, (600, 750), (600, 0), 1)
            pygame.draw.line(u.windowSurface, u.LATNIR, (0, 600), (1000, 600), 1)

            #Birta talningar á skjá
            u.windowSurface.blit(fjoldiH, textRect6)
            u.windowSurface.blit(fjoldiS, textRect7)
            u.windowSurface.blit(fjoldiE, textRect8)
            u.windowSurface.blit(fjoldiB, textRect9)
            u.windowSurface.blit(fjoldiL, textRect10)

            #Birta texta um hermun
            lysing_display()

            #Færa leikmenn á borði
            h.faera()

            #Teikna einstaklinga
            h.teikna()

            #Skoppa af vegg
            h.veggskopp()

            #Látum bolta skoppa af hvor öðrum
            h.arekstur()

            #Skoðum breytingu á tíma frá smiti
            h.breyting_timi()

            #Sækja talningar á ástandi einstaklinga
            h.talningar()

            #Birta talningarnar á skjánum
            talningar_display(h.teljaheilbrigda,h.teljasykta,h.teljaeinangrun,h.teljabatnad,h.teljalatna)

            #Sum smit eru greind og þeir einstaklingar eru sendir í einangrun
            h.greina_smit()

            #Bæti öllm gildum við í fylki sem plot() notar
            self.t.append(t)
            t+=1
            self.heilb_coord.append(h.teljaheilbrigda)
            self.sykt_coord.append(h.teljasykta)
            self.ein_coord.append(h.teljaeinangrun)
            self.batnad_coord.append(h.teljabatnad)
            self.latnir_coord.append(h.teljalatna)
            
            #Teikna graf
            surf = g.plot(self.t , np.array(self.heilb_coord), np.array(self.sykt_coord), np.array(self.ein_coord), np.array(self.batnad_coord), np.array(self.latnir_coord))
            u.windowSurface.blit(surf, (0, 602))
                
            #event handling
            for event in pygame.event.get():
                if event.type == QUIT:
                    import main
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            fpsClock.tick(FRAMES_PER_SECOND)
