# github.com/JDBLambert
# 4/18/2021
# Fireworks
# written for python2

import random
import pygame
pygame.init()
#simConfig
winWidth = 1920
winHeight = 1080
background = (0,0,0)

acc = winHeight/10000
lifeModifier = 90
fireworkDensity = 10
particleDensity = 150
trailDecay = 15

win = pygame.display.set_mode((winWidth, winHeight), pygame.FULLSCREEN)
pygame.display.set_caption("Watch the Fireworks!")
font = pygame.font.SysFont("Arial", 12)

class firework:
    def __init__(self, posx, color):
        self.color = color
        self.rect = pygame.Rect(posx, winHeight, 7, 11)
        self.vel = random.gauss(winHeight/lifeModifier,.5)

    def update(self):
        self.vel -= acc
        self.rect.y -= self.vel

    def isExplodeTime(self):
        if self.vel < 0:
            return True
        else:
            return False

    def createParticles(self):
        for i in range(particleDensity):
            x = random.gauss(0,(winHeight/500)+(winWidth/1000))
            y = random.gauss(0,(winHeight/500)+(winWidth/1000))
            particles.append(particle(self.rect.centerx, self.rect.centery, x, y, self.color))

    def leaveTrail(self):
        trails.append(trail(self.rect, self.color))

    def getColor(self):
        return self.color

    def getSize(self):
        return self.rect

class trail:
    def __init__(self, rect, color):
        self.color = color
        self.rect = pygame.Rect(rect.left, rect.top, rect.width, rect.height)

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


class particle:
    def __init__(self, posx, posy, velx, vely, color):
        self.timer = random.gauss(lifeModifier/4, 5)
        self.color = color
        self.rect = pygame.Rect(posx, posy, 3, 3)
        self.xVel = velx
        self.yVel = vely

    def update(self):
        self.yVel += acc
        self.rect.x += self.xVel
        self.rect.y += self.yVel

    def isExpired(self):
        if self.timer <= 0:
            particles.remove(self)
            return True
        else:
            self.timer -= 1
            return False

    def leaveTrail(self):
        trails.append(trail(self.rect, self.color))

    def getColor(self):
        return self.color

    def getSize(self):
        return self.rect


def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text


def updateScreen():
    win.fill(background)
    win.blit(update_fps(), (10,0))

    for shell in fireworks:
        pygame.draw.rect(win, background, shell.getSize())
        shell.update()
        shell.leaveTrail()
        if shell.isExplodeTime():
            shell.createParticles()
            fireworks.remove(shell)
        pygame.draw.rect(win, shell.getColor(), shell.getSize())

    for trail in trails:
        pygame.draw.rect(win, trail.getColor(), trail.getSize())
        trail.update()

    for spark in particles:
        spark.update()
        spark.leaveTrail()
        if not spark.isExpired():
            pygame.draw.rect(win, spark.getColor(), spark.getSize())

    pygame.display.update()


fireworks = []
particles = []
trails = []
specialEvents = 0
run = True
clock = pygame.time.Clock()
timer = 0
delay = 10
while run:
    dt = clock.tick(60)
  #  print(dt)
    timer += 1
    if (len(fireworks) < fireworkDensity and timer >= random.randint(delay,delay+50)):
        timer = 0
        red = int(150*random.random()+105)
        blue = int(150*random.random()+105)
        green = int(150*random.random()+105)
        fireworks.append(firework(random.gauss(winWidth/2, 250), (red, green, blue)))

    updateScreen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            run = False
        if keys[pygame.K_1]:
            timer = -100
        if keys[pygame.K_2]:
            timer = -150
        if keys[pygame.K_3]:
            timer = -200
        if keys[pygame.K_4]:
            timer = -250
        if keys[pygame.K_5]:
            timer = -300
        if keys[pygame.K_6]:
            timer = -350
        if keys[pygame.K_7]:
            timer = -400
        if keys[pygame.K_8]:
            timer = -450
        if keys[pygame.K_9]:
            timer = -500
        if keys[pygame.K_0]:
            timer = -550
        if keys[pygame.K_UP]:
                delay +=20
        if keys[pygame.K_DOWN]:
            if delay > 20:
                delay -= 20

    #specialEvents
    if (timer % 50) == 49 and timer < -50:
        fireworks.append(firework(random.gauss(winWidth/2, 250), (255, 20, 20)))
        fireworks.append(firework(random.gauss(winWidth/2, 250), (255, 255, 255)))
        fireworks.append(firework(random.gauss(winWidth/2, 250), (20, 20, 255)))
pygame.quit()
