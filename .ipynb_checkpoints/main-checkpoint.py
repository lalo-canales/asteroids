import pygame
from constants import *
from logger import log_state
from player import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids with pygame version: 2.6.1")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	my_ship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
	game_clock = pygame.time.Clock()
	dt = 0

	while True:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")
		#my_ship.update(dt)
		updatable.update(dt)
		#my_ship.draw(screen)
		for thing in drawable:
			thing.draw(screen)
		pygame.display.flip()
		delta_time = game_clock.tick(60)
		dt = delta_time/1000
        
if __name__ == "__main__":
    main()
