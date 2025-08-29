import pygame
from constants import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                return
            
        color =  (0, 0, 0) 
        screen.fill(color, rect=None, special_flags=0)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(dt)
        


if __name__ == "__main__":
    main()
