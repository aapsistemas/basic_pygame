import pygame

#criar tela
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


#titulo
pygame.display.set_caption("game basic")


#player
playerImg = pygame.image.load("img/borb.png")
playerX = 100
playerY = 100
DEFAULT_IMAGE_SIZE = (80, 80)
playerImg = pygame.transform.scale(playerImg, DEFAULT_IMAGE_SIZE)

def player(x, y):
    screen.blit(playerImg, (x, y))
# loop game
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #color screen
    screen.fill((60, 72, 107))

    player(playerX,playerY)
    #update
    pygame.display.update()
