import sys
import pygame
from pygame import *
from pygame.locals import *
from pygame.sprite import *
from random import *

# main
pygame.init()
display.set_caption("Whack-a-mole")
screen = display.set_mode((640, 480))


#Mole Class
class Mole(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("mole.gif")
        self.rect = self.image.get_rect()

    def flee(self):
        randx = randint(0, 600)
        randy = randint(0, 400)
        self.rect.center = (randx, randy)


mole = Mole()
sprites = Group(mole)


run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == MOUSEBUTTONDOWN:
            print(mouse.get_pos())
            if mole.rect.collidepoint(mouse.get_pos()):
                mole.flee()


    screen.fill((255,255,255))

    sprites.update()
    sprites.draw(screen)


    pygame.display.update()

pygame.quit()
