import MineField
import consts
import pygame

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_mode()


def show_screen():
    screen.fill((0, 0, 0))
    draw_grid(consts.BACKGROUND)
    draw_hidden_soldier()
    draw_flag()
    build_mine_list()
    pygame.display.update()


def draw_hidden_soldier():  # TODO: find current soldier x, y
    # soldier_x = (consts.WINDOW_WIDTH / consts.NUMBER_OF_COLS)
    # soldier_y = (consts.WINDOW_HEIGHT / consts.NUMBER_OF_ROWS)
    screen.blit(consts.HIDDEN_SOLDIER_IMAGE, (-consts.WIDTH_LINES, 0))


def draw_grid(color=consts.WHITE):
    blockSize_width = int(consts.WINDOW_WIDTH / consts.NUMBER_OF_COLS)  # Set the size of the grid block
    blockSize_height = int(consts.WINDOW_HEIGHT / consts.NUMBER_OF_ROWS)
    for x in range(0, consts.WINDOW_WIDTH, blockSize_width):
        for y in range(0, consts.WINDOW_HEIGHT, blockSize_height):
            rect = pygame.Rect(x, y, blockSize_width, blockSize_height)
            pygame.draw.rect(screen, color, rect, 1)


def build_mine_list():
    for row in range(consts.NUMBER_OF_ROWS):
        print(MineField.grid[row])
    for mine in range(len(MineField.mine_list)):
        row = MineField.mine_list[mine][0]
        col = MineField.mine_list[mine][1]
        x = MineField.grid[row][col]["x"]
        y = MineField.grid[row][col]["y"]
        draw_mine(x, y)


def draw_mine(x, y):
    screen.blit(consts.MINE_IMAGE, (x, y))


def draw_flag():
    flag_x = consts.WINDOW_WIDTH - (consts.WINDOW_WIDTH / consts.NUMBER_OF_COLS) * 4
    flag_y = consts.WINDOW_HEIGHT - (consts.WINDOW_HEIGHT / consts.NUMBER_OF_ROWS) * 3
    screen.blit(consts.FLAG_IMAGE, (flag_x, flag_y))
