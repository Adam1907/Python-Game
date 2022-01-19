import pygame
import pygame_menu
from main import main


pygame.init()
surface = pygame.display.set_mode((800, 800))

start = pygame.mixer.Sound("sound/start.wav")


def start_the_game():
    pygame.mixer.Sound.play(start)
    main()
    pass

menu = pygame_menu.Menu('Cobra', 800, 800, theme=pygame_menu.themes.THEME_DARK)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT,)


menu.mainloop(surface)