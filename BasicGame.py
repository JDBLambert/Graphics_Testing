# github.com/JDBLambert
# 4/18/2021
# testing basics game stuff
# written for python2


import pygame

pygame.init()

#screen config
winWidth = 600
winHeight = 400

win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Basic Game")



class Player():
    def __init__(self, posX, posY):
       width = 5
       height = 5
       self.yVel = 0
       self.color = (255, 255, 255)
       self.rect = pygame.Rect(posX, posY, width, height)

    def updatePosition(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                self.rect.x += 1
            if keys[pygame.K_a]:
                self.rect.x -= 1
            if keys[pygame.K_w] and self.rect.collidelist(ground) == -1:
                self.rect.y -= 1
            if keys[pygame.K_s] and self.rect.collidelist(ground) == -1:
                self.rect.y += 1


    def getColor(self):
        return self.color

    def getSize():
        return self.rect

def updateScreen():
    win.fill((0,0,0))
    pygame.draw.rect(win, player.getColor(), player.rect)
    for rect in ground:
        pygame.draw.rect(win, (255,0,0), rect)
    pygame.display.update()


run = True
player = Player(winWidth/2, winHeight/2)
ground = []
ground.append(pygame.Rect(winWidth/4, (winHeight/2)+8, winWidth/2, 4))
while run:
    #built in delay
    pygame.time.delay(10)

    #check for exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #update the player
    player.updatePosition()

    #render the screen
    updateScreen()

pygame.quit()
