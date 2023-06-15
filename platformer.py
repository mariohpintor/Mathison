import pygame, sys
from settings import *
from level import Level
from overworld import Overworld

class Game:
	def __init__(self):
		self.max_level = 3
		self.overworld = Overworld(0,self.max_level,screen,self.create_level)
		self.status = 'overworld'
	
	def create_level(self,current_level):
		self.level = Level(level_map0,screen,current_level,self.create_overworld)
		self.status = 'level'

	def  create_overworld(self,current_level, new_max_level):
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		self.overworld = Overworld(current_level,self.max_level,screen,self.create_level)
		self.status = 'overworld'	

	def run(self):
		if self.status == 'overworld':
			self.overworld.run()
		else:
			self.level.run()
		#self.level.run()	

pygame.init()
pygame.display.set_caption("Mathison begins")
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
#level0 = Level(level_map0,screen,number_level0)

game = Game()

#level2 = Level(level_map2,screen)
fondo = pygame.image.load("imagenes/cyberpunk.jpeg").convert_alpha()
fondo = pygame.transform.scale(fondo, (screen_width,screen_height))
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	#screen.fill((204,255,255))
	screen.blit(fondo,(0,0))
	game.run()
	#level0.run()

	pygame.display.update()
	clock.tick(60)	

