import pygame
import sys
from pygame.locals import *

pygame.init()

win = pygame.display.set_mode((800,800))
pygame.display.set_caption("Hello Pygame")


FPSCLOCK = pygame.time.Clock()

run = True

sysfont = pygame.font.SysFont(None, 100)
message = sysfont.render("Hello Pygame", True, (0,128,128))
message_rect = message.get_rect()
message_rect.center=(400,400)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            run = False

    win.fill((255, 255, 255))

    win.blit(message, message_rect)

    pygame.display.update()
    FPSCLOCK.tick(30)


pygame.quit()

