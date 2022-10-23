import random
import pygame
import consts

grid = []
mine_list = []


def create():
    global grid
    grid = []
    blockSize_width = int(consts.WINDOW_WIDTH / consts.NUMBER_OF_COLS)  # Set the size of the grid block
    blockSize_height = int(consts.WINDOW_HEIGHT / consts.NUMBER_OF_ROWS)

    grid = [[{"state": "EMPTY", "x": 0, "y": 0} for i in range(consts.NUMBER_OF_COLS)] for j in
            range(consts.NUMBER_OF_ROWS)]  # set dict for each cell in matrix
    x = 0
    y = 0
    for row in range(consts.NUMBER_OF_ROWS):
        for col in range(consts.NUMBER_OF_COLS):
            grid[row][col]["x"] = x
            grid[row][col]["y"] = y
            x = x + blockSize_width
        x = 0
        y = y + blockSize_height
    insert_solider()
    insert_flag()
    create_mines()


def create_mines():
    extra = insert_mines()
    while True:
        if extra == 0:
            break
        extra = insert_mines(extra)


def insert_mines(mines=20):
    extra_mine = 0
    for mine in range(mines):
        row = random.randrange(0, consts.NUMBER_OF_ROWS)
        col = random.randrange(0, consts.NUMBER_OF_COLS - 3)
        if not check_if_empty(row, col):
            extra_mine += 1
    return extra_mine


def check_if_empty(row, col):
    check = 0
    for i in range(3):
        box = grid[row][col + i]
        if box["state"] == "EMPTY":
            check += 1
    if check == 3:
        mine_list.append([row, col])
        for i in range(3):
            box["state"] = "MINE"
        return True
    return False



def insert_flag():
    for i in range(21, 24, 1):
        for j in range(46, 50, 1):
            grid[i][j]["state"] = "FLAG"


def insert_solider():
    for row in range(4):
        for col in range(2):
            grid[row][col]["state"] = "SOLIDER"


# TODO fill the functions and link them with screen's "draw_hidden_XXX"
def find_left_up_corner_cordinate_of_solider():
    pass


def find_left_up_corner_cordinate_of_flag():
    pass


def find_left_up_corner_cordinate_of_mine():
    pass
