
import pygame
import sys
from pygame.locals import *

pygame.init()

win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Hello Pygame")

gslogo = pygame.image.load("gslogo.jpg")

run = True

pos =[400,400]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                pos[0] -= 5
            elif event.key== K_RIGHT:
                pos[0] += 5
            elif event.key == K_UP:
                pos[1] -= 5
            elif event.key == K_DOWN:
                pos[1] += 5


    win.fill((255, 255, 255))
    rect = gslogo.get_rect()
    rect.center = pos
    print(rect)
    win.blit(gslogo, rect)
    pygame.display.update()

pygame.quit()


