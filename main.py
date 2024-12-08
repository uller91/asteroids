import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    ship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    Field = AsteroidField()

    while True:     #infinite loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('black')      #fill screen with black
        for items in updatable:
            items.update(dt)
            
        for items in asteroids:
            if items.collision(ship):
                print("Game over!")
                sys.exit()

            for bullet in shots:
                if items.collision(bullet):
                    print("Shot!")
                    items.kill()
                    bullet.kill()

        for items in drawable:
            items.draw(screen)
        pygame.display.flip()       #refresh screen
        dt = clock.tick(60)/1000             #60 FPS in s
        #print(dt)



if __name__ == "__main__":
    main()
