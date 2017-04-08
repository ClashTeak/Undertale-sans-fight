import pygame, sys
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((1000,800))

#Pictures
cadre = pygame.transform.scale(pygame.image.load("Data/cadre.png"),(600,300))

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)

continuer = True

class Cadre(pygame.sprite.Sprite):
	
	def __init__(self):
		
		self.x = 200
		self.y = 400
		
		self.image = cadre
		
		pygame.sprite.Sprite.__init__(self)
		self.update()
	
	def update(self):
		
		self.rect = (self.x,self.y,self.image.get_width(),self.image.get_height())
		self.mask = pygame.mask.from_surface(self.image)

cadre = Cadre()

while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	
	window.fill(black)
	window.blit(cadre.image,cadre.rect)
	pygame.display.update()
