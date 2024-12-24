from circleshape import *
from constants import *
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
    
    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, self.position, SHOT_RADIUS)

    def update(self, dt):
        self.position += (self.velocity * dt)