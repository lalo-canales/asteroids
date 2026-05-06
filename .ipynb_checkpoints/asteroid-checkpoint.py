from circleshape import *
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

	def update(self, dt):
		self.position += (self.velocity*dt)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			log_event("asteroid_split")
			angle = random.uniform(20, 50)
			velocity_1 = self.velocity.rotate(angle) * 1.2
			velocity_2 = self.velocity.rotate(-1*angle) * 1.2
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
			new_asteroid_1.velocity = velocity_1
			new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
			new_asteroid_2.velocity = velocity_2