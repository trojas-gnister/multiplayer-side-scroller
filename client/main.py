import pygame
import sys
from shared.config import SCREEN_H, SCREEN_W, FPS_CAP, FIXED_DT


def main() -> None:
    clock = pygame.time.Clock()
    accumulator = 0.0

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

    def update(dt):
        pass

    def render(alpha):
        screen.fill("black")
        pygame.display.flip()

    while True:
        frame_time = clock.tick(FPS_CAP) / 1000.0
        frame_time = min(frame_time, 0.25)
        accumulator = +frame_time
        while accumulator >= FIXED_DT:
            update(FIXED_DT)
            accumulator -= FIXED_DT
        alpha = accumulator / FIXED_DT
        render(alpha)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()
