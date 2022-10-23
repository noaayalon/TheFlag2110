# This is a sample Python script.
import Screen
import time
import consts
import pygame
import MineField
import HiddenScreen
import sys

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
    # HiddenScreen.show_screen()

    while state["is_window_open"]:
        handle_user_events()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            HiddenScreen.show_screen()
            time.sleep(1)
            Screen.draw_game()
        if keys[pygame.K_RIGHT]:
            pass
        if keys[pygame.K_UP]:
            pass
        if keys[pygame.K_DOWN]:
            pass


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["status"] != consts.RUNNING_STATE:
            continue


        # if event.type == pygame.KEYDOWN:  # TODO - full the func and multiple keys (up,right,down) & ENTER
        #     if event.key == pygame.K_KP_ENTER:
        #         HiddenScreen.show_screen()
        #     if event.key == pygame.K_LEFT:
        #         # move_solider()
        #         print("left")
        #     if event.key == pygame.K_RIGHT:
        #         print("RIGHT")
        # if event.type == pygame.KEYUP:
        #     print("bii")


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
