import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
       
    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        direction1 = self.velocity.rotate(random_angle)
        direction2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = direction1 *1.2
        a2.velocity = direction2 *1.2

        