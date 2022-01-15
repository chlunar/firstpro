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
hit = pygame.mixer.Sound('hit.wav')
#Mole Class
class Mole(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("mole.gif")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
    def flee(self):
        randx = randint(0, 600)
        randy = randint(0, 400)
        self.rect.center = (randx, randy)


class Shovel(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("shovel.gif")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
    def hit(self, target):
        pass

    # Follows the mouse cursor
    def update(self):
        self.rect = mouse.get_pos()

mole = Mole()
shovel = Shovel()
sprites = Group(mole, shovel)


run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.sprite.collide_mask(shovel,mole):
            mole.flee()
            hit.play()


    screen.fill((255,255,255))

    sprites.update()
    sprites.draw(screen)


    pygame.display.update()

pygame.quit()
