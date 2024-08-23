import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

def main():
    pygame.init()
    score = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,drawable,updatable)
    new_player = Player(x= SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    new_asteroid = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,1))  
        for sprite in drawable:
            sprite.draw(screen)
        
        for stuff_to_update in updatable:
            stuff_to_update.update(dt)

        for stones in asteroids:
            if new_player.collsion(stones):
                print("Game over!")
                print(f"Your score was: {score}")
                return
        
        for rocks in asteroids:
            for bullets in shots:
                if rocks.collsion(bullets):
                    rocks.split()
                    bullets.kill()
                    score += 100


                
        
        pygame.display.flip()
        dt = (time.tick(60)/1000)
        
        



if __name__ == "__main__":
    main()