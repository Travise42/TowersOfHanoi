import pygame
import math
import random
import surfaces as images
from screens.title import Title
from screens.home import Home
from screens.game import Game

'''CREATE WINDOW'''

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Towers of Hanoi")
FPS = 100

'''CREATE PALLET'''

# colors
class color():
    LIGHT_GREY = (225, 225, 225)
    GREY = (88, 88, 88)
    
'''CREATE SCREENS'''

title = Title(WIN, color, images)
home = Home(WIN, color, images, title, (WIDTH, HEIGHT))
game = Game(WIN, color, images, home)

def main():
    cooldown = False
    screen = title

    clock = pygame.time.Clock()
    ACTIVE = True
    while ACTIVE:
        clock.tick(FPS)
        ACTIVE, screen, cooldown = screen.handleEvents([title, home, game], cooldown)
        pygame.display.update()
    pygame.quit()

# only run program when ran directly
if __name__ == "__main__":
    main()