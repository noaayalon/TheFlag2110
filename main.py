# This is a sample Python script.
import Screen
import consts
import pygame
import MineField
import sys



def main():
    pygame.init()
    Screen.draw_grid(consts.WHITE)
    Screen.draw_soldier()
    MineField.create()
    # GAME LOOP
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False





def move_solidr(): #we have to consider if the solider is in range and turn on the func only if in the main the state of
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
