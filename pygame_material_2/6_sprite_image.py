import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

white = (255, 255, 255)
blue = (0, 0, 255)


class Gshs(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("gshs.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = [320, 240]

    def update(self):
        pass


def draw(sprites):
    screen.fill(white)
    sprites.draw(screen)
    pygame.display.flip()


gshs = Gshs()
sprites = pygame.sprite.Group(gshs)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sprites.update()  # game events!
    draw(sprites)

pygame.quit()
