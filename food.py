import pygame
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE


class food:
    def __init__(self):
        self.position = (0, 0)
        self.color = (255, 40, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (
            random.randint(0, GRID_WIDTH - 1) * GRIDSIZE,
            random.randint(0, GRID_HEIGHT - 1) * GRIDSIZE,
        )

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)