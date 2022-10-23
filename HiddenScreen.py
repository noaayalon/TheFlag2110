import consts
import pygame

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_mode()


def show_screen():
    screen.fill((0, 0, 0))
    draw_grid(consts.BACKGROUND)
    draw_hidden_soldier()
    pygame.display.update()


def draw_hidden_soldier():  # TODO: find current soldier x, y
    soldier_x = (consts.WINDOW_WIDTH / consts.NUMBER_OF_COLS)
    soldier_y = (consts.WINDOW_HEIGHT / consts.NUMBER_OF_ROWS)
    screen.blit(consts.HIDDEN_SOLDIER_IMAGE, (-consts.WIDTH_LINES, 0))
    pygame.display.update()


def draw_grid(color=consts.WHITE):
    blockSize_width = int(consts.WINDOW_WIDTH / consts.NUMBER_OF_COLS)  # Set the size of the grid block
    blockSize_height = int(consts.WINDOW_HEIGHT / consts.NUMBER_OF_ROWS)
    for x in range(0, consts.WINDOW_WIDTH, blockSize_width):
        for y in range(0, consts.WINDOW_HEIGHT, blockSize_height):
            rect = pygame.Rect(x, y, blockSize_width, blockSize_height)
            pygame.draw.rect(screen, color, rect, 1)
    pygame.display.update()


def draw_hidden_mines():
    pass
