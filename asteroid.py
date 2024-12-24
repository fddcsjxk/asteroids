from circleshape import *
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        self.width = 2

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, self.position, self.radius, self.width)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_vector_1 = self.velocity.rotate(random_angle)
        new_vector_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        childroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        childroid_1.velocity = new_vector_1 * 1.2
        childroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        childroid_2.velocity = new_vector_2 * 1.2