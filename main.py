import pygame

from constants import *


def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                return

        screen.fill((0, 0, 0))
        pygame.display.update()


if __name__ == "__main__":
    main()
