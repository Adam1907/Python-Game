import pygame
import pygame_menu

from snake import snake
from food import food


pygame.init()

pygame.display.set_caption('Cobra')

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 15

GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE


eating = pygame.mixer.Sound("sound/eating.wav")
over = pygame.mixer.Sound("sound/game_over.wav")


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
        clock.tick(FPS)
        snakeOBJ.handle_keys()
        drawGrid(surface)
        snakeOBJ.move()

        if snakeOBJ.get_head_position() == foodOBJ.position:
            pygame.mixer.Sound.play(eating)
            snakeOBJ.length += 1
            score += 1
            foodOBJ.randomize_position()


        if snakeOBJ.state == 0:
            game_over = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            menu = pygame_menu.Menu('G A M E  O V E R!', SCREEN_WIDTH, SCREEN_HEIGHT, theme=pygame_menu.themes.THEME_DARK)
            menu.add.button('YOUR SCORE: {}'.format(score))
            menu.add.button('Quit', pygame_menu.events.EXIT)
            pygame.mixer.Sound.play(over)
            menu.mainloop(game_over)


        snakeOBJ.draw(surface)
        foodOBJ.draw(surface)
        screen.blit(surface, (0, 0))
        text = myfont.render("SCORE: {0}".format(score), 1, (0, 0, 0))
        screen.blit(text, (5, 10))
        pygame.display.update()