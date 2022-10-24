# This is a sample Python script.
import Screen
import time
import consts
import pygame
import MineField
import HiddenScreen

import movements

state = {
    "movement_arrow": None,
    "status": None,  # running/losing/winning
    "key_enter": False,
    "is_window_open": True
}


def main():
    pygame.init()
    MineField.create()
    Screen.draw_game()

    while state["is_window_open"]:
        handle_user_events()

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_RETURN]:
        #     HiddenScreen.show_screen()
        #     time.sleep(1)
        #     Screen.draw_game()
        # if keys[pygame.K_LEFT]:
        #     movements.move_solider("left")
        # if keys[pygame.K_RIGHT]:
        #     movements.move_solider("right")
        # if keys[pygame.K_UP]:
        #     movements.move_solider("up")
        # if keys[pygame.K_DOWN]:
        #     movements.move_solider("down")


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
            pygame.quit()
            break

        if event.type == pygame.KEYDOWN:  # TODO - full the func and multiple keys (up,right,down) & ENTER
            if event.key == pygame.K_RETURN:
                HiddenScreen.show_screen()
                time.sleep(1)
                Screen.draw_game()
            if event.key == pygame.K_LEFT:
                movements.move_solider("left")
            if event.key == pygame.K_RIGHT:
                movements.move_solider("right")
                print("hii")
                for row4 in range(len(MineField.grid)):
                    print(MineField.grid[row4])
            if event.key == pygame.KEYUP:
                movements.move_solider("up")
            if event.key == pygame.KEYDOWN:
                movements.move_solider("down")


def move_soldier_left():
    # check if lose or win
    # change the grid
    # change animation
    pass


def move_soldier_right():
    # check if lose or win
    # change the grid
    # change animation
    pass


def move_soldier_up():
    # check if lose or win
    # change the grid
    # change animation
    pass


def move_soldier_down():
    # check if lose or win
    # change the grid
    # change animation
    pass


def is_lose():
    # TODO: implement
    pass


def is_win():
    # TODO: implement
    pass


if __name__ == '__main__':
    main()
