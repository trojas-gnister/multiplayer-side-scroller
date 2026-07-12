import pygame
import sys
from shared.config import SCREEN_H, SCREEN_W


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


if __name__ == "__main__":
    main()
