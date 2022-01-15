
import pygame
import sys
pygame.init()

win = pygame.display.set_mode((640,480))
pygame.display.set_caption("Hello Pygame")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            run = False

    win.fill((255, 255, 2   55))
    pygame.display.update()

pygame.quit()

