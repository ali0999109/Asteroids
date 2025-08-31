import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import * 


def main():
    pygame.init()
    clock = pygame.time.Clock()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable =  pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField() 

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                return
            
        dt = clock.tick(60) / 1000
            
        updatable.update(dt)

        for asteroid in asteroids:

            if asteroid.collides_with(player):
                print("Game over")
                return
        
        for asteroid in asteroids:

            for bullet in shots:

                if asteroid.collides_with(bullet):
                    bullet.kill()
                    asteroid.split()

        
            
        color =  (0, 0, 0) 
        screen.fill(color, rect=None, special_flags=0)
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        print(dt)
        


if __name__ == "__main__":
    main()
