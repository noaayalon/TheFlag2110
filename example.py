import consts
import pygame

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
screen.fill(consts.BACKGROUND)
pygame.display.update()

pygame.draw.line(screen, consts.WHITE, (60, 80), (130, 100))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False