import pygame, sys, asyncio
from game_data import screen_width,screen_height
from level import Level
from overworld import Overworld
from initial_menu import Imenu
from screen_resultados import Pantalla_resultados
from creditos import Creditos
from ui import UI

class Game:
	def __init__(self):
		#Atributos
		#self.max_level = 0
		#self.overworld = Overworld(0,self.max_level,screen,self.create_level,self.create_initial_menu)
		self.max_health = 100
		self.cur_health = 100
		self.coins = 0

		# Creación del menu inicial
		self.status = 'menu'
		self.initial_menu = Imenu(screen, self.create_overworld,self.create_creditos)
		self.contador = 0

		# user interface
		self.ui = UI(screen)

	def create_level(self,current_level):
		self.level = Level(screen,current_level,self.create_results,self.change_coins,self.change_health)
		self.status = 'level'

	def create_overworld(self,current_level, new_max_level):
		#if new_max_level > self.max_level:
			#self.max_level = new_max_level
		self.overworld = Overworld(current_level,new_max_level,screen,self.create_level,self.create_initial_menu)
		self.status = 'overworld'

	def create_initial_menu(self):
		self.initial_menu = Imenu(screen,self.create_overworld,self.create_creditos)
		self.status = 'menu'

	def create_results(self,surface,inicio,palomas,ecuaciones,fin,new_max_level,meta):
		self.status = 'results'
		self.pantalla_results = Pantalla_resultados(surface,self.create_overworld,inicio,palomas,ecuaciones,fin,new_max_level,meta)

	def create_creditos(self,surface):
		self.status = 'creditos'
		self.creditos = Creditos(surface,self.create_initial_menu)

	def change_coins(self,amount):
		self.coins = amount

	def change_health(self,amount):
		self.cur_health += amount

	def check_game_over(self):
		if self.cur_health <= 0:
			self.cur_health = 100
			self.coins = 0
			#self.max_level = 0
			#self.pantalla_results.run()
			self.status = 'results'

	def run(self):
		if self.status == 'overworld':
			self.overworld.run()
		elif self.status == 'level':
			self.level.run()
			self.ui.show_health(self.cur_health,self.max_health)
			self.ui.show_coins(self.coins)
			self.check_game_over()
		elif self.status == 'menu':
			self.initial_menu.run()
		elif self.status == 'results':
			self.pantalla_results.run()
		else:
			self.creditos.run()
			#self.check_game_over()

pygame.init()
pygame.display.set_caption("Mathison begins")
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()


game = Game()

async def main():

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
	
		game.run()
	
		pygame.display.update()
		clock.tick(60)
		await asyncio.sleep(0)

asyncio.run(main())

