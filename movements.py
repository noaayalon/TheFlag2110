import MineField
import Solider
import consts


def move_solider(arrow_motion):
    lst_legs_cordinates = Solider.calc_legs_solider_cordinates()
    lst_body_cordinates = Solider.calc_body_solider_cordinates()

    if arrow_motion == "left":
        if Solider.is_solider_in_grid_range("left"):
            move_index("col", "left", lst_legs_cordinates)  # move the legs
            move_index("col", "left", lst_body_cordinates)  # move the body

    if arrow_motion == "right":
        if Solider.is_solider_in_grid_range("right"):
            move_index("col", "right", lst_legs_cordinates)  # move the legs
            move_index("col", "right", lst_body_cordinates)  # move the body

    if arrow_motion == "up":
        if Solider.is_solider_in_grid_range("up"):
            move_index("row", "up", lst_legs_cordinates)  # move the legs
            move_index("row", "up", lst_body_cordinates)  # move the body

    if arrow_motion == "down":
        if Solider.is_solider_in_grid_range("down"):
            move_index("row", "down", lst_legs_cordinates)  # move the legs
            move_index("row", "down", lst_body_cordinates)  # move the body

    # reset the grid  - start
    for row in range(consts.NUMBER_OF_ROWS):
        for col in range(consts.NUMBER_OF_COLS):
            if MineField.grid[row][col]["state"] == "SOLIDER":
                MineField.grid[row][col]["state"] = "EMPTY"
    # reset the grid - end

    for i in range(len(lst_legs_cordinates)):
        row1 = lst_legs_cordinates[i][0]
        col1 = lst_legs_cordinates[i][1]
        MineField.grid[row1][col1]["state"] = "SOLIDER"

    for i in range(len(lst_body_cordinates)):
        row2 = lst_body_cordinates[i][0]
        col2 = lst_body_cordinates[i][1]
        MineField.grid[row2][col2]["state"] = "SOLIDER"


def move_index(colrow, arrow_motion, lst):  # calc - plus/minus, colrow - col(input "col") or row(input "row")
    if colrow == "col":
        if arrow_motion == "left":
            for i in range(len(lst)):
                lst[i][1] -= 1
        elif arrow_motion == "right":
            for i in range(len(lst)):
                lst[i][1] += 1
    if colrow == "row":
        if arrow_motion == "up":
            for j in range(len(lst)):
                lst[j][0] -= 1

        elif arrow_motion == "down":
            for j in range(len(lst)):
                lst[j][0] += 1
