# github.com/JDBLambert
# 4/18/2021
# Better Fireworks
# WIP
# written for python2
import random
import pygame
pygame.init()

# simConfig
winWidth = 1920
winHeight = 1080
background = (0, 0, 0)

trailDecay = 10


win = pygame.display.set_mode((winWidth, winHeight), pygame.FULLSCREEN)
pygame.display.set_caption("Watch the Fireworks!")
font = pygame.font.SysFont("Arial", 18)


class firework:
        def __init__(self, startx, endy, color):
            self.color = color
            self.endy = endy
            self.rect = pygame.Rect(startx, winHeight, 7, 1)
            self.vel = endy/winHeight

        def getSize(self):
            return self.rect

        def getColor(self):
            return self.color

        def leaveTrail(self):
            trails.append(trail(self.rect, self.color))

        def isExplodeTime(self):
            if self.vel < .1:
                return True
            else:
                return False

        def update(self):
            self.vel = ((self.rect.y - self.endy)/50)
            self.rect.y -= self.vel
            self.leaveTrail()

class trail:
    def __init__(self, rect, color):
        self.rect = pygame.Rect(rect.left, rect.top, rect.width, rect.height)
        self.color = color

    def update(self):
        red = self.color[0] - trailDecay
        green = self.color[1] - trailDecay
        blue = self.color[2] - trailDecay
        if red<0 or green<0 or blue<0:
            trails.remove(self)
        else:
            self.color = (red,green,blue)

    def getColor(self):
        return self.color

    def getSize(self):
        return self.rect



def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("green2"))
    return fps_text


def updateScreen():
    win.fill(background)
    win.blit(update_fps(), (10, 0))
    for firework in fireworks:
        firework.update()
        if firework.isExplodeTime():
            fireworks.remove(firework)
        pygame.draw.rect(win, (255, 255, 255,), firework.getSize())

    pygame.display.update()


run = True
clock = pygame.time.Clock()

fireworks = []


while run:
    dt = clock.tick(60)
    updateScreen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            run = False
        if keys[pygame.K_1]:
            fireworks.append(firework(random.gauss(winWidth/2, 500), random.gauss(winHeight/4, 200)), (255, 255, 255))


pygame.quit()
