from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        split_vectors = (self.velocity.rotate(split_angle), self.velocity.rotate(-split_angle))
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        split_1 = Asteroid(self.position.x, self.position.y, split_radius)
        split_1.velocity = split_vectors[0] * 1.2
        split_2 = Asteroid(self.position.x, self.position.y, split_radius)
        split_2.velocity = split_vectors[1] * 1.2