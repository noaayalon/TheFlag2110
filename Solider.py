import MineField
import consts

grid = MineField.return_init_grid()


def is_solider_in_grid_range(arrow_motion):
    # 4 cases solider cant move:  (col/row - arrow motion): [col 0 - left], [row 0 - up], [col 48 - right], [row 21 - down]
    for row in range(consts.NUMBER_OF_ROWS):
        for col in range(consts.NUMBER_OF_COLS):
            if (grid[row][col][
                "state"] == "SOLIDER"):  # assumption -it will crash the left-up corner of solider first, while scanning

                if arrow_motion == "left":  # TODO - check maybe ther's a const for motion (left,up..)
                    if col == 0:
                        return False

                if arrow_motion == "up":
                    if row == 0:
                        return False

                if arrow_motion == "right":
                    if col == 48:
                        return False

                if arrow_motion == "down":
                    if row == 21:
                        return False

            return True


# def cordinate_xy_of_solider(): #find the left-up corner of solider
#     for row in range(consts.NUMBER_OF_ROWS):
#         for col in range(consts.NUMBER_OF_COLS):
#             if(grid[row][col]["state"]=="SOLIDER"): # assumption - it will crash the left-up corner of solider first, while scanning
#                 tuple_location_of_solider = (grid[row][col]["x"],grid[row][col]["y"])
#                 break
#     return tuple_location_of_solider


def cordinate_location_of_solider_in_matrix11():  # find the left-up corner of solider in matrix by (row,col)
    for row in range(consts.NUMBER_OF_ROWS):
        for col in range(consts.NUMBER_OF_COLS):
            if (grid[row][col]["state"] == "SOLIDER"):  # assumption - it will crash the
                # left-up corner of solider first, while scanning
                tuple_location_of_solider11 = (row, col)
                break
    return tuple_location_of_solider11


def calc_legs_solider_cordinates():  # notation XY cells - (X - height(range 4)), (Y - width(range 2))
    lst_location_solider_legs = []

    tuple_location_of_solider11 = cordinate_location_of_solider_in_matrix11()
    row_corner_solider11 = tuple_location_of_solider11[0]
    col_corner_solider11 = tuple_location_of_solider11[1]

    tuple_location_of_41 = (row_corner_solider11 - 3, col_corner_solider11)  # 41 - left down corner
    tuple_location_of_42 = (row_corner_solider11 - 3, col_corner_solider11 + 1)  # 42 - right down corner

    lst_location_solider_legs = [tuple_location_of_41, tuple_location_of_42]  # 1st val - cell of left leg(on tuple),
    # 2nd val - cell of right leg(on tuple)

    return lst_location_solider_legs


def calc_body_solider_cordinates():
    lst_location_solider_body = []

    tuple_location_of_solider11 = cordinate_location_of_solider_in_matrix11()
    row_corner_solider11 = tuple_location_of_solider11[0]
    col_corner_solider11 = tuple_location_of_solider11[1]

    tuple_location11 = (row_corner_solider11, col_corner_solider11)
    tuple_location21 = (row_corner_solider11 - 1, col_corner_solider11)
    tuple_location31 = (row_corner_solider11 - 2, col_corner_solider11)
    tuple_location12 = (row_corner_solider11, col_corner_solider11 + 1)
    tuple_location22 = (row_corner_solider11 - 1, col_corner_solider11 + 1)
    tuple_location32 = (row_corner_solider11 - 2, col_corner_solider11 + 1)

    lst_location_solider_body = [tuple_location11, tuple_location21, tuple_location31, tuple_location12,
                                 tuple_location22, tuple_location32]

    return lst_location_solider_body
