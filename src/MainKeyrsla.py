import sys
import pygame
from pygame.locals import *
import Uppsetning as U
import Hopur as H
import pygame
import pygame_gui

FRAMES_PER_SECOND = 30
fpsClock = pygame.time.Clock()

#Búum til hluti af klösum
h = H.Hopur()
u = U.Uppsetning()

#Upphafsstilling valkvæðra breyta
value=0
value1=0
value2=0

background = pygame.Surface((u.xSkjar, u.ySkjar))

#SET UP PYGAME
pygame.init()

h.einstaklingar()

#SET UP WINDOW
pygame.display.set_caption('Covid-19 hermir')

manager = pygame_gui.UIManager((u.xSkjar, u.ySkjar))

#Texti í svarta rammanum
titill = "Útfærðar hafa verið þrjár mismunandi hermanir fyrir útbreiðslu COVID-19 veirunnar. Veldu númer þeirrar hermunar sem þú vilt keyra."

#TAKKAR
opid_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 120), (100, 50)),
                                            text='1',
                                            manager=manager)

lokad_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((750, 120), (100, 50)),
                                            text='2',
                                            manager=manager)

fjogur_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((900, 120), (100, 50)),
                                            text='3',
                                            manager=manager)

byrja_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((750, 520), (100, 50)),
                                            text='BYRJA',
                                            manager=manager)

#SLIDERS
horiz_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((700, 225), (200, 50)),
                                                    start_value = 10, value_range=(0,100),
                                            manager=manager)
horiz_slider1 = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((700, 325), (200, 50)),
                                                    start_value = 10, value_range=(0,100),
                                            manager=manager)
horiz_slider2 = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((700, 425), (200, 50)),
                                                    start_value = 10, value_range=(0,100),
                                            manager=manager)

#Svartur rammi með texta
titilsida = pygame_gui.elements.UITextBox(titill, relative_rect=pygame.Rect((600, 40), (400, 75)), manager=manager)
#hermunUpplysingar = pygame_gui.elements.UITextBox(upplHermun, relative_rect=pygame.Rect((600, 135), (400, 75)), manager=manager)

#Ekki í notkun. Virkar ekki
def OpidSvaedi():

    #Teikna einstaklinga
    h.teikna()

    #Færa einstaklinga á borði
    h.faera()

    #SKOPPA AF VEGG
    h.veggskopp()

    #Látum bolta skoppa af hvor öðrum
    h.arekstur()

    #Skoðum breytingu á tíma frá smiti
    h.breyting_timi()

    #Talningar á ástandi einstaklinga
    h.talningar()

# create a font object. 
# 1st parameter is the font file 
# which is present in pygame. 
# 2nd parameter is size of the font 
fontFyrirsogn = pygame.font.Font('freesansbold.ttf', 24) 
fontAlmennt = pygame.font.Font('freesansbold.ttf', 16)
fontTeljarar = pygame.font.Font('freesansbold.ttf', 14)
  
# create a text suface object, 
# on which text is drawn on it. 
fyrirsogn = fontFyrirsogn.render('Hermun á útbreiðslu COVID-19', True, u.SYKTUR, u.HVITUR) 
val1 = fontAlmennt.render('Veldu fjölda einstaklinga:', True, u.SYKTUR, u.HVITUR) 
val2 = fontAlmennt.render('Veldu hve margir eru smitaðir í upphafi:', True, u.SYKTUR, u.HVITUR) 
val3 = fontAlmennt.render('Veldu smitlíkur veirunnar:', True, u.SYKTUR, u.HVITUR) 
byrja = fontAlmennt.render('Veldu BYRJA til að hefja hermun:', True, u.SYKTUR, u.HVITUR) 
fjoldiH = fontTeljarar.render('Fjöldi heilbrigðra:', True, u.HEILBRIGDUR, u.HVITUR)
fjoldiS = fontTeljarar.render('Fjöldi sýktra:', True, u.SYKTUR, u.HVITUR)
fjoldiB = fontTeljarar.render('Fjöldi óvirkra smita:', True, u.BATNAD, u.HVITUR)
fjoldiL = fontTeljarar.render('Fjöldi látinna:', True, u.LATNIR, u.HVITUR)
fjoldiL1 = fontTeljarar.render('0', True, u.LATNIR, u.HVITUR)
#gildi1 = fontTeljarar.render(gildi, True, u.SYKTUR, u.HVITUR)
  
# create a rectangular object for the 
# text surface object 
textRect1 = fyrirsogn.get_rect() 
textRect1.center = (800,20)

textRect2 = val1.get_rect() 
textRect2.center = (800,200)

textRect3 = val2.get_rect() 
textRect3.center = (800,300)

textRect4 = val3.get_rect() 
textRect4.center = (800,400)

textRect5 = byrja.get_rect() 
textRect5.center = (800,500)

textRect6 = fjoldiH.get_rect() 
textRect6.center = (700,615)

textRect7 = fjoldiS.get_rect() 
textRect7.center = (700,655)

textRect8 = fjoldiB.get_rect() 
textRect8.center = (700,695)

textRect9 = fjoldiL.get_rect() 
textRect9.center = (700,735)

textRect10 = fjoldiL1.get_rect() 
textRect10.center = (900,735)

#textRect11 = gildi1.get_rect() 
#textRect11.center = (950,250)

clock = pygame.time.Clock()

def score(gildi1,gildi2,gildi3):
    s1 = fontTeljarar.render(str(gildi1), True, u.SYKTUR)
    s2 = fontTeljarar.render(str(gildi2), True, u.SYKTUR)
    s3 = fontTeljarar.render(str(gildi3), True, u.SYKTUR)
    u.windowSurface.blit(s1,[900,240])
    u.windowSurface.blit(s2,[900,340])
    u.windowSurface.blit(s3,[900,440])

#Aðal loopan
while True:

    #clear screen
    u.windowSurface.fill(u.HVITUR)

    #Línur sem skilur hermun frá tölulegum upplýsingum
    pygame.draw.line(u.windowSurface, u.LATNIR, (600, 750), (600, 0), 1)
    pygame.draw.line(u.windowSurface, u.LATNIR, (0, 600), (1000, 600), 1)

    # copying the text surface object 
    # to the display surface object  
    # at the center coordinate. 
    u.windowSurface.blit(fyrirsogn, textRect1) 
    u.windowSurface.blit(val1, textRect2)
    u.windowSurface.blit(val2, textRect3)
    u.windowSurface.blit(val3, textRect4)
    u.windowSurface.blit(byrja, textRect5)
    u.windowSurface.blit(fjoldiH, textRect6)
    u.windowSurface.blit(fjoldiS, textRect7)
    u.windowSurface.blit(fjoldiB, textRect8)
    u.windowSurface.blit(fjoldiL, textRect9)
    u.windowSurface.blit(fjoldiL1, textRect10)

    time_delta = clock.tick(60)/1000.0

    #event handling
    for event in pygame.event.get():
        hermun_nr = 0
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                print("element:", event.ui_element)
                if event.ui_element == opid_button:
                    hermun_nr=1
                if event.ui_element == lokad_button:
                    hermun_nr=2
                if event.ui_element == fjogur_button:
                    hermun_nr=3
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == horiz_slider:
                    value = round(horiz_slider.get_current_value())
                    print(value)
                    #u.windowSurface.blit(gildi1, textRect11)
                if event.ui_element == horiz_slider1:
                    value1 = round(horiz_slider1.get_current_value())
                    print(value1)
                if event.ui_element == horiz_slider2:
                    value2 = round(horiz_slider2.get_current_value())
                    print(value2)
        
            score(value,value1,value2)

        manager.process_events(event)
    manager.update(time_delta)

    u.windowSurface.blit(background, (0, 0))
    manager.draw_ui(u.windowSurface)

    pygame.display.update()
    fpsClock.tick(FRAMES_PER_SECOND)
