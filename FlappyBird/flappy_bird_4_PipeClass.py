import pygame, random, time
from pygame.locals import *

WIDTH = 400
HEIGHT = 600
SPEED = 20
GRAVITY = 2.5
GAME_SPEED = 15

GROUND_WIDTH = 2 * WIDTH
GROUND_HEIGHT = 100

PIPE_WIDTH = 80
PIPE_HEIGHT = 500
PIPE_GAP = 150

# Sound
wing = 'assets/audio/wing.wav'
hit = 'assets/audio/hit.wav'
pygame.mixer.init()

# Initialize
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Image
BACKGROUND = pygame.image.load('assets/sprites/background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
BEGIN_IMAGE = pygame.image.load('assets/sprites/message.png').convert_alpha()




#====================

# Bird Class
class Bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('assets/sprites/redbird-upflap.png').convert_alpha(),
                       pygame.image.load('assets/sprites/redbird-midflap.png').convert_alpha(),
                       pygame.image.load('assets/sprites/redbird-downflap.png').convert_alpha()
                       ]

        self.speed = SPEED

        self.current_image = 0
        self.image = pygame.image.load('assets/sprites/redbird-upflap.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = WIDTH / 6
        self.rect[1] = HEIGHT / 2

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        self.speed += GRAVITY

        self.rect[1] += self.speed

    def jump(self):
        self.speed = -SPEED

    def begin(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]



#=========================================
class Ground(pygame.sprite.Sprite):

    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/sprites/base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()

        '''
        self.rect return value
            return (self.left.value(), self.bottom.value(),
                    self.width.value(), self.height.value())
        '''

        self.rect[0] = xpos
        self.rect[1] = HEIGHT - GROUND_HEIGHT

    def update(self):
        self.rect[0] -= GAME_SPEED


#Pipe class
class Pipe(pygame.sprite.Sprite):

    def __init__(self, inverted, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('assets/sprites/pipe-green.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = - (self.rect[3] - ysize)
            print(self.rect)
        else:
            self.rect[1] = HEIGHT - ysize

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect[0] -= GAME_SPEED


def get_random_pipes(xpos):
    size = random.randint(100, 300)
    pipe = Pipe(False, xpos, size)
    pipe_inverted = Pipe(True, xpos, HEIGHT - size - PIPE_GAP)
    return pipe, pipe_inverted





#########
def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])




#====================
#Sprite Group
bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

#====================
#Ground Group
ground_group = pygame.sprite.Group()
for i in range(2):
    ground = Ground(GROUND_WIDTH*i)
    ground_group.add(ground)


#Pipe Group
pipe_group = pygame.sprite.Group()
for i in range(2):
    pipes = get_random_pipes(WIDTH*i + 800)
    pipe_group.add(pipes[0])
    pipe_group.add(pipes[1])



clock = pygame.time.Clock()

# Begin Scene
begin = True
while begin:
    clock.tick(15)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_UP:

                pygame.mixer.music.load(wing)
                pygame.mixer.music.play()
                begin = False

    # new ground add if one is off screen
    if is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])

        new_ground = Ground(GROUND_WIDTH - 20)
        ground_group.add(new_ground)


    screen.blit(BACKGROUND, (0, 0))
    screen.blit(BEGIN_IMAGE, (120, 150))

    # ====================
    bird.begin()
    bird_group.draw(screen)

    # Ground Group Draw
    # ====================
    ground_group.update()
    ground_group.draw(screen)


    # Pipe Group Draw
    pipe_group.update()
    pipe_group.draw(screen)


    pygame.display.update()


pygame.quit()
