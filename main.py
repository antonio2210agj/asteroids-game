import pygame
from constants import *
from player import Player



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  #
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

        screen.fill((0,0,0)) # Fill the screen with black
        player.update(dt)
        player.draw(screen) # Draw the player
        pygame.display.flip() # Update the display
        dt = clock.tick(FPS) / 1000  # Limit to 60 FPS and get delta time in seconds
        

if __name__ == "__main__":
    main()
