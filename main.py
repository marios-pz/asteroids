import pygame

from constants import *
from player import Player


def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game = True
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    player.containers = (updatable, drawable)

    while game:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                return

        for sprite in drawable:
            sprite.draw(screen)

        for sprite in updatable:
            sprite.update(dt)

        # end of the line
        pygame.display.update()
        dt = clock.tick(60) / 1000  # convert from milliseconds to seconds


if __name__ == "__main__":
    main()
