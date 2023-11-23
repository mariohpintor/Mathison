import pygame
from game_data import screen_width,screen_height


class Imenu:
	def __init__(self,surface,create_dificultad,create_credits,create_controles):
		self.surface = surface
		self.create_controles = create_controles
		self.create_credits = create_credits
		self.create_dificultad = create_dificultad
		self.main_font = pygame.font.SysFont("Courier", 100)
		self.sub_font = pygame.font.SysFont("Courier", 40)

	def input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_i]:
			self.create_dificultad()
			print('i')
		if keys[pygame.K_d]:
			self.create_credits()
			print('d')
		if keys[pygame.K_c]:
			self.create_controles()
			print('c')

	def run(self):
		miTexto = self.main_font.render("MATHISON", 0, (255, 255, 255))
		subtitulo = self.sub_font.render("[Un juego de ecuaciones]", 0, (255, 255, 255))
		nuevo_text = self.sub_font.render("Iniciar [I]", 0, (255, 255, 255))
		creditos_text = self.sub_font.render("Créditos [D]", 0, (255, 255, 255))
		controles = self.sub_font.render('Controles [C]', 0, (255, 255, 255))

		miTexto_rect = miTexto.get_rect(center=(screen_width/2,screen_height/2-250))
		subtitulo_rect = subtitulo.get_rect(center=(screen_width/2,screen_height/2-150))
		nuevo_rect = nuevo_text.get_rect(center=(screen_width/2,screen_height/2))
		creditos_rect = creditos_text.get_rect(center=(screen_width/2,screen_height/2+100))
		controles_rect = controles.get_rect(center=(screen_width/2,screen_height/2+200))

		fondo = pygame.image.load("imagenes/fondos/base2.jpeg").convert_alpha()
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

	