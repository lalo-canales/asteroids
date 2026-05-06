import pygame
import sys
from constants import *
from logger import log_state
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids with pygame version: 2.6.1")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	Shot.containers = (shots, updatable, drawable)
	asteroid_field = AsteroidField()
	my_ship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	game_clock = pygame.time.Clock()
	dt = 0

	while True:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")
		updatable.update(dt)
		for thing in asteroids:
			if my_ship.collides_with(thing):
				log_event("player_hit")
				print("Game over!")
				sys.exit()
		for thing in drawable:
			thing.draw(screen)
		for rock in asteroids:
			for shot in shots:
				if shot.collides_with(rock):
					log_event("asteroid_shot")
					shot.kill()
					rock.split()
		pygame.display.flip()
		delta_time = game_clock.tick(60)
		dt = delta_time/1000
        
if __name__ == "__main__":
    main()