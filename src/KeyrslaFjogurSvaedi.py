import sys
import pygame
import numpy as np
from pygame.locals import *
import Uppsetning as U
import Hopur as H
import graphs as G

class KeyrslaFjogurSvaedi():
    def keyrslafjogursvaedi(self, n, LikurByrja, LikurSmit):

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

        t=0 #til þess að telja
        
        #SET UP PYGAME
        pygame.init()

        #SET UP WINDOW
        pygame.display.set_caption('Covid-19 hermir')
        FRAMES_PER_SECOND = 30
        fpsClock = pygame.time.Clock()

        h.upphafsstilling(n, LikurByrja, LikurSmit)
        h.fjogur_svaedi_hopar()
        h.einstaklingar_fjogur_svaedi()

        fontTeljarar = pygame.font.Font('freesansbold.ttf', 14)
        fontFyrirsogn = pygame.font.Font('freesansbold.ttf', 24) 

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

        def lysing_display():
            name = fontFyrirsogn.render("Smit á fjórum svæðum", True, u.SYKTUR)
            s1 = fontTeljarar.render("Hermun á opnu svæði á fjórum svæðum samhliða. Allir ", True, u.SYKTUR)
            s2 = fontTeljarar.render("einstaklingar eru frjálsir ferða sinna innan svæðanna", True, u.SYKTUR)
            s3 = fontTeljarar.render("en geta ekki ferðast á milli þeirra. Mis margir byrja", True, u.SYKTUR)
            s4 = fontTeljarar.render("smitaðir á hverju svæði fyrir sig og er það markmiðið", True, u.SYKTUR)
            s5 = fontTeljarar.render("með hermuninni að sýna hve mismunandi smitáhrif", True, u.SYKTUR)
            s6 = fontTeljarar.render("veirunnar eru eftir því hve þéttbýlt er á hverju svæði", True, u.SYKTUR)
            s7 = fontTeljarar.render("fyrir sig. Sýktir einstaklingar halda ferðum", True, u.SYKTUR)
            s8 = fontTeljarar.render("sínum áfram þrátt fyrir smit því þeir vita ekki endilega", True, u.SYKTUR)
            s9 = fontTeljarar.render("að þeir séu sýktir.", True, u.SYKTUR)
            s10 = fontTeljarar.render(" ", True, u.SYKTUR)
            s11 = fontTeljarar.render("Allir sýnatökupinnar á Íslandi eru búnir og þar af", True, u.SYKTUR)
            s12 = fontTeljarar.render("leiðandi fer engin skimun fram og enginn er greindur", True, u.SYKTUR)
            s13 = fontTeljarar.render("með veiruna. Einnig hafa allir starfsmenn almannavarna", True, u.SYKTUR)
            s14 = fontTeljarar.render("sýkst og því er fólk ekki einu sinni sent í sóttkví ef", True, u.SYKTUR)
            s15 = fontTeljarar.render("grunur er um smit.", True, u.SYKTUR)
            s16 = fontTeljarar.render("Með öðrum orðum: hermunin lætur í ljós versta ástand", True, u.SYKTUR)
            s17 = fontTeljarar.render("sem hugsast getur.", True, u.SYKTUR)
            s18 = fontTeljarar.render(" ", True, u.SYKTUR)
            s19 = fontTeljarar.render("Heilbrigðir einstaklingar eru táknaðir með bláu og", True, u.SYKTUR)
            s20 = fontTeljarar.render("þeir sem sýkjast af veirunni eru táknaðir með", True, u.SYKTUR)
            s21 = fontTeljarar.render("appelsínugulu. Ef sýktur einstaklingur nær bata fær", True, u.SYKTUR)
            s22 = fontTeljarar.render("hann að fara aftur út í samfélagið, táknaður sem bleikur,", True, u.SYKTUR)
            s23 = fontTeljarar.render("en þá getur hann ekki smitast aftur. Ef svo ólíklega vill", True, u.SYKTUR)
            s24 = fontTeljarar.render("til að einstaklingur lætur lífið í baráttu sinni við", True, u.SYKTUR)
            s25 = fontTeljarar.render("veiruna litast hann svartur, stöðvast og aðrir", True, u.SYKTUR)
            s26 = fontTeljarar.render("einstaklingar komast ekki í snertingu við hann.", True, u.SYKTUR)

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
            u.windowSurface.blit(s21,[605,450])
            u.windowSurface.blit(s22,[605,470])
            u.windowSurface.blit(s23,[605,490])
            u.windowSurface.blit(s24,[605,510])
            u.windowSurface.blit(s25,[605,530])
            u.windowSurface.blit(s26,[605,550])

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
            
            pygame.draw.line(u.windowSurface, u.LATNIR, (300, 0), (300, 600), 1)
            pygame.draw.line(u.windowSurface, u.LATNIR, (0, 300), (600, 300), 1)

            #Línur sem skilur hermun frá tölulegum upplýsingum
            pygame.draw.line(u.windowSurface, u.LATNIR, (600, 750), (600, 0), 1)
            pygame.draw.line(u.windowSurface, u.LATNIR, (0, 600), (1000, 600), 1)

            #Birta talningartitla
            u.windowSurface.blit(fjoldiH, textRect6)
            u.windowSurface.blit(fjoldiS, textRect7)
            u.windowSurface.blit(fjoldiB, textRect9)
            u.windowSurface.blit(fjoldiL, textRect10)

            #Birtum lýsingu um hermun á spássíðu
            lysing_display()

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

            h.talningar()

            talningar_display(h.teljaheilbrigda,h.teljasykta,h.teljaeinangrun,h.teljabatnad,h.teljalatna)

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
