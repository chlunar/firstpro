
import pygame
import sys
from pygame.locals import *

pygame.init()

win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Hello Pygame")

run = True

mousepos = []
mousedown = False

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

        elif event.type == MOUSEBUTTONDOWN:
            mousedown = True

        elif event.type == MOUSEMOTION:
            if mousedown:
                mousepos.append(event.pos)

        elif event.type == MOUSEBUTTONUP:
            mousedown = False
            mousepos.clear()

    win.fill((255, 255, 255))
    for pos in mousepos:
        pygame.draw.circle(win, (255,0,0), pos, 5)

    pygame.display.update()

pygame.quit()



