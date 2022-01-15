import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

white = (255,255,255)
blue = (0,0,255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    pygame.draw.circle(screen, blue, (320,240), 100)    # position (320,240), radius = 100

    pygame.display.update()

pygame.quit()

