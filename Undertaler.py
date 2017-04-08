import pygame, sys
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((1000,800))

black = pygame.Color(0,0,0)
white = pyame.Color(255,255,255)

continuer = True

while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	window.fill(black)
	pygame.display.update()
