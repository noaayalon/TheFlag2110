import pygame
import pygame as pg

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 550
NUMBER_OF_ROWS = 25
NUMBER_OF_COLS = 50
WIDTH_LINES = int(WINDOW_WIDTH / NUMBER_OF_COLS)
HEIGHT_LINES = int(WINDOW_HEIGHT / NUMBER_OF_ROWS)

GRASS_IMAGE = pygame.image.load('grass.png')
SOLDIER_IMAGE = pygame.image.load('soldier.png')
SOLDIER_IMAGE = pg.transform.scale(SOLDIER_IMAGE, (((WINDOW_WIDTH / NUMBER_OF_COLS)*4), (WINDOW_HEIGHT / NUMBER_OF_ROWS)*2))

BACKGROUND = (138, 201, 38)
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)

BLOCK_SIZE = (WINDOW_HEIGHT * WINDOW_WIDTH) / (NUMBER_OF_COLS * NUMBER_OF_ROWS)


RUNNING_STATE = 1
LOSE_STATE = 2
WIN_STATE = 3