from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    container = ()

    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self, *self.container)
        super().__init__(x, y, radius)

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(random_angle)
            vel2 = self.velocity.rotate(random_angle * -1)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x,self.position.y, new_rad).velocity = vel1 * 1.2
            asteroid = Asteroid(self.position.x,self.position.y, new_rad).velocity = vel2 * 1.2
