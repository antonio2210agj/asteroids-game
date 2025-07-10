import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    
    updatables = pygame.sprite.Group() 
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # Register the containers for each class
    Player.containers = updatables, drawables
    Asteroid.containers = updatables, drawables, asteroids
    AsteroidField.containers = (updatables,)
    Shot.containers = (updatables, drawables, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()



    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()  # Clock-Objekt to manage frame rate
    dt = 0  # Delta time variable
    FPS = 60  # Frames per second

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0,0,0))  # black background
        updatables.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                return
                                      
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()
                    break  # Exit the loop after the first hit


        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000

        

if __name__ == "__main__":
    main()
