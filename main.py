# IMPORT LIBRARIES/MODULES
import pygame
from controls import *

# PYGAME SETTINGS
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(NAME)

# VARIABLES
BACKGROUND_COLOR = BLACK
FPS = FPS


# CREATE OBJECTS


# DRAW GRAPHICS
def draw_graphics():
    win.fill(BACKGROUND_COLOR)


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        clock.tick(FPS)
        draw_graphics()
    pygame.quit()


if __name__ == '__main__':
    main()
