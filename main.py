import pygame
from constants import *
from player import *

def main():
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    ship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:     #infinite loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('black')      #fill screen with black
        ship.update(dt)
        ship.draw(screen)
        pygame.display.flip()       #refresh screen
        dt = clock.tick(60)/1000             #60 FPS in s
        #print(dt)



if __name__ == "__main__":
    main()
