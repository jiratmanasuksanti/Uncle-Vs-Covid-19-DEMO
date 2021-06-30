import pygame
import random
pygame.init()
#############
Width = 800
Height = 600
screen = pygame.display.set_mode((Width, Height), pygame.RESIZABLE)
title = pygame.display.set_caption("คุณลุงสู้โควิด-๑๙","โควิด-๑๙")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
#Uncle#
FPS = 60
FRAME = 60
clock = pygame.time.Clock()
unclex = 0
uncley = Height - 128
unclexchange = 0
uncleimage = pygame.image.load("lib/assets/images/uncle.png")
def UpdateUncle(x,y):
    screen.blit(uncleimage,(x,y))
#Covid-19#
covid19x = random.randint(30,Width-30)
covid19y = 0
covidychange = 0
covid19image = pygame.image.load("lib/assets/images/covid-19.png")
def UpdateVirus(x,y):
    screen.blit(covid19image,(x,y))
#mainloop#
mainloop = True
while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                unclexchange = -2.5
            if event.key == pygame.K_RIGHT:
                unclexchange = 2.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and pygame.K_LEFT:
                unclexchange = 0
    if unclex > 900:
        unclex = -125
    if unclex < -150:
        unclex = 900
    unclex = unclex + unclexchange
    UpdateUncle(unclex,uncley)
    pygame.display.update()
    clock.tick(FPS)