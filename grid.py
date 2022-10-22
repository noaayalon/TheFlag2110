import random
import pygame
import consts
import Screen


grid = []


def create():
    # spot = {
    #     "state": "EMPTY",
    #     "x": 0,
    #     "y": 0
    # }


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

    return grid


def insert_mines(mines=20):
    isValid_enter_mine = False

    cols_mines = []
    extra_mine = 0
    for mine in range(mines):
        while isValid_enter_mine == False:
            row = random.randrange(0, consts.NUMBER_OF_ROWS - 1)  # TODO assure theres no duplication
            col = random.randrange(0, consts.NUMBER_OF_COLS - 3)
            for i in range(3):
                cols_mines.append(col + i)
            if check_if_empty(row, cols_mines):
                isValid_enter_mine = True
        for j in range(3):
            grid[row][cols_mines[j]]["state"] = "MINE"
        isValid_enter_mine = False

    for row1 in range(len(grid)):
        print(grid[row1])


def check_if_empty(row, lst_cols):
    for i in range(3):
        if not grid[row][lst_cols[i]]["state"] == "EMPTY":
            return False
    return True


grid = create()
insert_mines()
# for row1 in range(len(grid)):
#     print(grid[row1])


def insert_solider():
    pass#TODO

def insert_flag():
    pass#TODO


#TODO fill the functions and link them with screen's "draw_hidden_XXX"
def find_left_up_corner_cordinate_of_solider():
    pass

def find_left_up_corner_cordinate_of_flag():
    pass

def find_left_up_corner_cordinate_of_mine():
    pass

