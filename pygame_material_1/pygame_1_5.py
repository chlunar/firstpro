
import pygame
import sys
from pygame.locals import *

pygame.init()

win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Hello Pygame")

strip = pygame.image.load("tiles_spritesheet.png")
FPSCLOCK = pygame.time.Clock()



images = []
for i in range(10):
    image = pygame.Surface((70,70))
    image.blit(strip, (0,0), Rect(i*70, 0, 70, 70))
    # image.set_colorkey((0,0,0))
    images.append(image)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            run = False

    win.fill((255, 255, 255))

    for i in range(10):
        win.blit(images[i], (i*70, 0))



    pygame.display.update()

pygame.quit()



