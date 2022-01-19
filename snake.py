import pygame
import sys
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE

class snake:
    def __init__(self):
        self.state = 1
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 24, 47)

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (
            ((cur[0] + (x * GRIDSIZE)) % SCREEN_WIDTH),
            (cur[1] + (y * GRIDSIZE)) % SCREEN_HEIGHT,
        )
        #
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.state = 0
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRIDSIZE, GRIDSIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (0, 0, 0), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)