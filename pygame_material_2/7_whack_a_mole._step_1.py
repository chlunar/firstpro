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

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255,255,255))
    pygame.display.update()

pygame.quit()
