
import pygame
import sys
from pygame.locals import *

pygame.init()

win = pygame.display.set_mode((600,400))
pygame.display.set_caption("Hello Pygame")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((255, 255, 255))
    for xpos in range(0, 600, 25):
        pygame.draw.line(win, (0, 0, 0), (xpos, 0), (xpos, 600))

    for ypos in range(0, 600, 25):
        pygame.draw.line(win, (0, 0, 0), (0, ypos), (600, ypos))


    pygame.display.update()

pygame.quit()


