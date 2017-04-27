import pygame
import sys
from Player import Player
from game_function import check_events

def run_game():
	pygame.init()
	screen_size = (1000,000)
	background_color = (82, 111, 53)
	screen = pygame.display.set_mode(screen_size)
	pygame.display.set_caption("A heroic 3rd person shooter")
	the_player = Player(screen)


	while 1:
		screen.fill(background_color)
		check_events()


		the_player.draw_me()
		pygame.display.flip()

run_game()