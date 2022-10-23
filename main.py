# This is a sample Python script.
import Screen
import consts
import pygame
import MineField
import sys

state = {
        "movement_arrow": None,
        "status": None,  # running/losing/winning
        "key_enter": False,
        "is_window_open": True
    }
def main():
    pygame.init()
    Screen.draw_game()
    MineField.return_init_grid()


    while state["is_window_open"]:

        handle_user_events()


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["status"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.KEYDOWN:#TODO - full the func and multiple keys (up,right,down) & ENTER
            if event.key ==pygame.K_KP_ENTER:
                pass

            if event.key == pygame.K_LEFT:
                move_solider()
                pass







def move_solider():  # we have to consider if the solider is in range and turn on the func only if in the main the state of
    # if "state[is_solider_moved] == True"
    pass


def is_lose():
    # TODO: implement
    pass


def is_win():
    # TODO: implement
    pass


if __name__ == '__main__':
    main()

# GAME LOOP
    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False