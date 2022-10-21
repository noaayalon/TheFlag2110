# This is a sample Python script.
import Screen
import consts
import pygame
import grid
import sys



def main():
    pygame.init()
    Screen.draw_grid(consts.WHITE)
    Screen.draw_soldier()
    grid.create()
    # GAME LOOP
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False





def is_lose():
    # TODO: implement
    pass


def is_win():
    # TODO: implement
    pass


if __name__ == '__main__':
    main()
