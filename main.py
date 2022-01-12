import pygame
import sys
import random

from snake import snake
from food import food

# pygame.mixer.pre_init()
pygame.init()

pygame.display.set_caption('Cobra')

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE

eating = pygame.mixer.Sound("sound/eating.wav")


def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (208, 255, 161), r)
            else:
                rr = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (181, 255, 107), rr)


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snakeOBJ = snake()
    foodOBJ = food()
    myfont = pygame.font.SysFont("arial", 20)

    score = 0
    while True:
        clock.tick(15)
        snakeOBJ.handle_keys()
        drawGrid(surface)
        snakeOBJ.move()
        if snakeOBJ.get_head_position() == foodOBJ.position:
            pygame.mixer.Sound.play(eating)
            snakeOBJ.length += 1
            score += 1
            foodOBJ.randomize_position()
        snakeOBJ.draw(surface)
        foodOBJ.draw(surface)
        screen.blit(surface, (0, 0))
        text = myfont.render("SCORE: {0}".format(score), 1, (0, 0, 0))
        screen.blit(text, (5, 10))
        pygame.display.update()

main()