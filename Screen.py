import HiddenScreen
import consts
import pygame
import random

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
screen.fill(consts.BACKGROUND)
pygame.display.update()


def draw_game():
    draw_soldier()
    for bush in range(21):
        draw_bush()


def draw_soldier():
    soldier_x = (consts.WINDOW_WIDTH / consts.NUMBER_OF_COLS)
    soldier_y = (consts.WINDOW_HEIGHT / consts.NUMBER_OF_ROWS)
    screen.blit(consts.SOLDIER_IMAGE, (-consts.WIDTH_LINES, 0))
    pygame.display.update()


def draw_grid(color):
    blockSize_width = int(consts.WINDOW_WIDTH / consts.NUMBER_OF_COLS)  # Set the size of the grid block
    blockSize_height = int(consts.WINDOW_HEIGHT / consts.NUMBER_OF_ROWS)
    for x in range(0, consts.WINDOW_WIDTH, blockSize_width):
        for y in range(0, consts.WINDOW_HEIGHT, blockSize_height):
            rect = pygame.Rect(x, y, blockSize_width, blockSize_height)
            pygame.draw.rect(screen, consts.WHITE, rect, 1)
    pygame.display.update()


def draw_bush():
    screen.blit(consts.GRASS_IMAGE, (random.randrange(0, consts.WINDOW_WIDTH), random.randrange(0, consts.WINDOW_HEIGHT)))
    pygame.display.update()


# TODO - draw the hidden screen

def draw_hidden_screen():
    HiddenScreen.show_screen()


def draw_hidden_solider():
    pass


def draw_hidden_mines():
    pass
