
import pygame
import sys
from pygame.locals import *

pygame.init()

win = pygame.display.set_mode((640,480))
pygame.display.set_caption("Hello Pygame")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            run = False

    win.fill((255, 255, 255))

    # 빨간색: 직사각형 (빈틈없이 칠한다)
    pygame.draw.rect(win, (255, 0, 0), (10, 20, 100, 50))
    # 빨간색: 직사각형 (굵기 3)
    pygame.draw.rect(win, (255, 0, 0), (150, 10, 100, 30), 3)
    # 녹색: 직사각형
    pygame.draw.rect(win, (0, 255, 0), ((100, 80), (80, 50)))
    # 파란색: 직사각형, Rect 오브젝트
    rect0 = Rect(200, 60, 140, 80)
    pygame.draw.rect(win, (0, 0, 255), rect0)
    # 노란색: 직사각형, Rect 오브젝트
    rect1 = Rect((30, 160), (100, 50))
    pygame.draw.rect(win, (255, 255, 0), rect1)

    pygame.display.update()

pygame.quit()


