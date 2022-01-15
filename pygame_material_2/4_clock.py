import pygame
from pygame.locals import *
import random
pygame.init()
screen = pygame.display.set_mode((640, 480))
color = [0, 0, 0]

clock = pygame.time.Clock()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_SPACE:
            color = [0, 0, 0]

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        color = [random.randint(0, 255) for rgb in color]

    screen.fill(color)
    pygame.display.update()
    clock.tick(40)

pygame.quit()
