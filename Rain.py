# github.com/JDBLambert
# 4/18/2021
#basic rain simulation
# written for python2

import random
import pygame
import math
pygame.init()

#Sim Config
winWidth = 1080 #screen Width
winHeight = 720 #screen Height

density = 5 #population density of drops
velMult = 10 #velocity Multiplier
accMult = .01 #This number is later /100
#mult + offset < 255
colorMult = 150 #color Multiplier
colorOffset = 100 #color Offset

widthMin = 5
widthMax = 8
heightMin = 8
heightMax = 20
#, pygame.FULLSCREEN  | pygame.DOUBLEBUF
win = pygame.display.set_mode((winWidth, winHeight))
# for end of previous line
pygame.display.set_caption("It's Raining")

class rain:
    def __init__(self, posX, posY):
        #color, X position, Y position
        width = random.randint(widthMin,widthMax)
        height = random.randint(heightMin, heightMax)
        self.color = (0, 0, colorMult* (width*height)/(widthMax*heightMax)+colorOffset)
        self.rect = pygame.Rect(posX, posY, width, height)
        self.vel = (((width*height)/float((widthMax*heightMax))*1.5)**5*velMult)

    def update(self, sway):
        self.vel += (self.rect.width*self.rect.height)* accMult/100
        self.rect.y += self.vel
        #self.rect.x += sway

    def CheckOffScreen(self):
        if self.rect.top > winHeight:
           rainDrops.remove(self)

    def getColor(self):
        return self.color

    def getSize(self):
        return self.rect

def updateScreen():
    win.fill((10,10,30))

    if(random.randint(0,1) == 1):
        sway = random.gauss(-.1, .2)
    else:
        sway = random.gauss(.1,.2)
    for raindrop in rainDrops:
        raindrop.update(sway)
        raindrop.CheckOffScreen()
        pygame.draw.ellipse(win, raindrop.getColor(), raindrop.getSize())
    pygame.display.update()

rainDrops = []
run = True
while run:
    pygame.time.delay(1)
    if len(rainDrops) < 10000:
        for i in range(density):
            rainDrops.append(rain(random.randint(0,winWidth), (i*-10)-100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            run = False

    updateScreen()
pygame.quit()
