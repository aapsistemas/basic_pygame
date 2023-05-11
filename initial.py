import pygame

#criar tela
pygame.init()
size = width, height = 400, 400
screen = pygame.display.set_mode(size)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
