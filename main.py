import pygame

size = width, height = 800, 400
screen = pygame.display.set_mode(size)

birdImg = pygame.image.load("img/frame-1.png")
birdX = 300
birdY = 20
birdX_change = 0
DEFAULT_IMAGE_SIZE = (80, 80)
birdImg = pygame.transform.scale(birdImg, DEFAULT_IMAGE_SIZE)
def player(x,y):
    screen.blit(birdImg,(x, y))

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #controle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                birdX_change = -0.1
            if event.key == pygame.K_RIGHT:
                birdX_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                birdX_change = 0


    birdX += birdX_change
    player(birdX, birdY)
    pygame.display.update()
