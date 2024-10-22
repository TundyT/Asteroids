import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x, y)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for updatee in updatable:
            updatee.update(dt)
        
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.is_colliding(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")
        
        for drawee in drawable:
            drawee.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()