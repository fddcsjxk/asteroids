from circleshape import *
from constants import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        self.width = 2

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, self.position, self.radius, self.width)

    def update(self, dt):
        self.position += (self.velocity * dt)
