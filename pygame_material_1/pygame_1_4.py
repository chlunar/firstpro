
import pygame
import sys
from pygame.locals import *

pygame.init()

win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Hello Pygame")

gslogo = pygame.image.load("gslogo.jpg")


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            run = False

    win.fill((255, 255, 255))
    win.blit(gslogo, (0, 0))
    pygame.display.update()

pygame.quit()



