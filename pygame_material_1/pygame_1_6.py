
import pygame
import sys
from pygame.locals import *

pygame.init()

win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Hello Pygame")

gslogo = pygame.image.load("gslogo.jpg")
FPSCLOCK = pygame.time.Clock()

run = True
theta = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            run = False

    win.fill((255, 255, 255))

    theta += 1
    tr_logo = pygame.transform.rotate(gslogo, theta)
    win.blit(tr_logo, (200, 200))

    pygame.display.update()
    FPSCLOCK.tick(30)

pygame.quit()


