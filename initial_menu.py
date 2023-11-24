import pygame
from game_data import screen_width,screen_height, AMARILLO
from controles import Controles
from creditos import Creditos 

class Imenu:
	def __init__(self,surface,create_dificultad):
		self.surface = surface
		self.create_dificultad = create_dificultad
		self.main_font = pygame.font.SysFont("tahoma", 100)
		self.sub_font = pygame.font.SysFont("tahoma", 40)

	def create_initial_menu(self):
		self.initial_menu = Imenu(self.surface,self.create_dificultad,self.create_creditos,self.create_controles)

	def create_controles(self):
		self.controles = Controles(self.surface,self.create_initial_menu)
		self.controles.run()

	def create_creditos(self):
		self.creditos = Creditos(self.surface,self.create_initial_menu)
		self.creditos.run()

	def input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_i]:
			self.create_dificultad()
		if keys[pygame.K_d]:
			self.create_creditos()
		if keys[pygame.K_c]:
			self.create_controles()
		
	def run(self):
		miTexto = self.main_font.render("MATHISON", 0, (255, 255, 255))
		subtitulo = self.sub_font.render("[Un juego de ecuaciones]", 0, (255, 255, 255))
		nuevo_text = self.sub_font.render("Iniciar [I]", 0, AMARILLO)
		creditos_text = self.sub_font.render("Créditos [D]", 0, AMARILLO)
		controles = self.sub_font.render('Controles [C]', 0, AMARILLO)

		miTexto_rect = miTexto.get_rect(center=(screen_width/2,screen_height/2-250))
		subtitulo_rect = subtitulo.get_rect(center=(screen_width/2,screen_height/2-150))
		nuevo_rect = nuevo_text.get_rect(center=(screen_width/2,screen_height/2))
		creditos_rect = creditos_text.get_rect(center=(screen_width/2,screen_height/2+100))
		controles_rect = controles.get_rect(center=(screen_width/2,screen_height/2+200))

		fondo = pygame.image.load("imagenes/fondos/cris.jpeg").convert_alpha()
		fondo = pygame.transform.scale(fondo, (screen_width,screen_height)) 
		self.surface.blit(fondo,(0,0))
		pygame.draw.rect(self.surface, (0, 0, 0), miTexto_rect)
		pygame.draw.rect(self.surface, (0, 0, 0), subtitulo_rect)
		pygame.draw.rect(self.surface, (0, 0, 0), nuevo_rect)
		pygame.draw.rect(self.surface, (0, 0, 0), creditos_rect)
		pygame.draw.rect(self.surface, (0, 0, 0), controles_rect)
		self.surface.blit(miTexto,miTexto_rect)
		self.surface.blit(subtitulo,subtitulo_rect)
		self.surface.blit(nuevo_text,nuevo_rect)
		self.surface.blit(creditos_text,creditos_rect)
		self.surface.blit(controles,controles_rect)

		self.input()

	