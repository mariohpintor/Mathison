import pygame, sys
from settings import *
from level import Level
from overworld import Overworld
from initial_menu import Imenu


class Game:
	def __init__(self):
		self.max_level = 0
		#self.overworld = Overworld(0,self.max_level,screen,self.create_level,self.create_initial_menu)
		self.status = 'menu'
		self.initial_menu = Imenu(screen, self.create_overworld)
		self.contador = 0

	def create_level(self,current_level):
		self.level = Level(screen,current_level,self.create_overworld)
		self.status = 'level'

	def  create_overworld(self,current_level, new_max_level):
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		self.overworld = Overworld(current_level,self.max_level,screen,self.create_level,self.create_initial_menu)
		self.status = 'overworld'

	def create_initial_menu(self):
		self.initial_menu = Imenu(screen,self.create_overworld)
		self.status = 'menu'


	def run(self):
		if self.status == 'overworld':
			self.overworld.run()
		elif self.status == 'level':
			self.level.run()
		else:
			self.initial_menu.run()	

pygame.init()
pygame.display.set_caption("Mathison begins")
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()


game = Game()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	game.run()

	pygame.display.update()
	clock.tick(60)	

