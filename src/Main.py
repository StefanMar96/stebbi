import sys
import pygame
from pygame.locals import *
import Uppsetning as U
import Einstaklingur as E
import Hopur as H
import pygame
import pygame_gui
import KeyrslaOpidSvaedi as K1
import KeyrslaLokadSvaedi as K2
import KeyrslaFjogurSvaedi as K3

FRAMES_PER_SECOND = 30
fpsClock = pygame.time.Clock()

#Búum til hluti af klösum
h = H.Hopur()
u = U.Uppsetning()
k1 = K1.KeyrslaOpidSvaedi()
k2 = K2.KeyrslaLokadSvaedi()
k3 = K3.KeyrslaFjogurSvaedi()

#Upphafsstilling valkvæðra breyta
n=10
LikurByrja=10
LikurSmit=10

background = pygame.Surface((u.xSkjar, u.ySkjar))

#SET UP PYGAME
pygame.init()

#SET UP WINDOW
pygame.display.set_caption('Covid-19 hermir')

manager = pygame_gui.UIManager((u.xSkjar, u.ySkjar))


#TAKKAR
opid_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 545), (100, 50)),
                                            text='1',
                                            manager=manager)

lokad_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((750, 545), (100, 50)),
                                            text='2',
                                            manager=manager)

fjogur_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((900, 545), (100, 50)),
                                            text='3',
                                            manager=manager)

#SLIDERS
horiz_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((700, 255), (200, 50)),
                                                    start_value = 10, value_range=(10,100),
                                            manager=manager)
horiz_slider1 = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((700, 355), (200, 50)),
                                                    start_value = 10, value_range=(5,95),
                                            manager=manager)
horiz_slider2 = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((700, 455), (200, 50)),
                                                    start_value = 10, value_range=(10,100),
                                            manager=manager)

#Texti í svarta rammanum
titill = "Útfærðar hafa verið þrjár mismunandi hermanir fyrir útbreiðslu COVID-19 veirunnar"
opidsvaedi = "1: Óhindruð útbreiðsla veirunnar"
lokadsvaedi = "2: Valinn hópur er í sóttkví en einhverjir svindla"
fjogursvaedi = "3: Óhindruð útbreiðsla á fjórum svæðum samhliða"

#Svartur rammi með texta
titilsida = pygame_gui.elements.UITextBox(titill, relative_rect=pygame.Rect((600, 40), (400, 55)), manager=manager)
lysing1 = pygame_gui.elements.UITextBox(opidsvaedi, relative_rect=pygame.Rect((600, 90), (400, 35)), manager=manager)
lysing2 = pygame_gui.elements.UITextBox(lokadsvaedi, relative_rect=pygame.Rect((600, 120), (400, 55)), manager=manager)
lysing3 = pygame_gui.elements.UITextBox(fjogursvaedi, relative_rect=pygame.Rect((600, 170), (400, 35)), manager=manager)
titilsida.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_IN)
lysing1.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_IN)
lysing2.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_IN)
lysing3.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_IN)

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
val2 = fontAlmennt.render('Veldu líkur á að byrja smitaður:', True, u.SYKTUR, u.HVITUR) 
val3 = fontAlmennt.render('Veldu smitlíkur veirunnar:', True, u.SYKTUR, u.HVITUR) 
byrja = fontAlmennt.render('Veldu númer hermunar sem þú vilt keyra:', True, u.SYKTUR, u.HVITUR) 
  
# create a rectangular object for the 
# text surface object 
textRect1 = fyrirsogn.get_rect() 
textRect1.center = (800,20)

textRect2 = val1.get_rect() 
textRect2.center = (800,230)

textRect3 = val2.get_rect() 
textRect3.center = (800,330)

textRect4 = val3.get_rect() 
textRect4.center = (800,430)

textRect5 = byrja.get_rect() 
textRect5.center = (800,530)

clock = pygame.time.Clock()

def score(gildi1,gildi2,gildi3):
    s1 = fontTeljarar.render(str(gildi1), True, u.SYKTUR)
    s2 = fontTeljarar.render(str(gildi2), True, u.SYKTUR)
    s3 = fontTeljarar.render(str(gildi3), True, u.SYKTUR)
    u.windowSurface.blit(s1,[900,270])
    u.windowSurface.blit(s2,[900,370])
    u.windowSurface.blit(s3,[900,470])

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

    time_delta = clock.tick(60)/1000.0

    #event handling
    for event in pygame.event.get():
        byrjahermun = False
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                print("element:", event.ui_element)
                if event.ui_element == opid_button:
                    k1.keyrslaopidsvaedi(n, LikurByrja, LikurSmit)
                    pygame.quit()
                    sys.exit()
                if event.ui_element == lokad_button:
                    k2.keyrslalokadsvaedi(n, LikurByrja, LikurSmit)
                    pygame.quit()
                    sys.exit()
                if event.ui_element == fjogur_button:
                    k3.keyrslafjogursvaedi(n, LikurByrja, LikurSmit)
                    pygame.quit()
                    sys.exit()
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == horiz_slider:
                    n = round(horiz_slider.get_current_value())
                if event.ui_element == horiz_slider1:
                    LikurByrja = round(horiz_slider1.get_current_value())
                if event.ui_element == horiz_slider2:
                    LikurSmit = round(horiz_slider2.get_current_value())

        manager.process_events(event)
    score(n,LikurByrja,LikurSmit)
    manager.update(time_delta)

    manager.draw_ui(u.windowSurface)

    pygame.display.update()
    fpsClock.tick(FRAMES_PER_SECOND)

    
