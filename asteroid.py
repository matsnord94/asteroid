from circleshape import *
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.position = pygame.Vector2(x,y)
        self.radius = radius
        self.velocity = 0 
    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20,50)
            positive_angle= self.velocity.rotate(new_angle)
            negative_angle = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
            new_asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
            new_asteroid1.velocity = positive_angle * 1.2
            new_asteroid2.velocity = negative_angle * 1.2

