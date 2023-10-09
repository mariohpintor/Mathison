import pygame, sys
from game_data import screen_width,screen_height

class Imenu:
	def __init__(self,surface,create_overworld,create_credits):
		self.surface = surface
		self.create_credits = create_credits
		self.create_overworld = create_overworld
		self.main_font = pygame.font.SysFont("Courier", 100)
		self.sub_font = pygame.font.SysFont("Courier", 40)

	def run(self):
		miTexto = self.main_font.render("MATHISON", 0, (255, 255, 255))
		subtitulo = self.sub_font.render("[Un juego de ecuaciones]", 0, (255, 255, 255))
		nuevo_text = self.sub_font.render("Nueva partida [N]", 0, (255, 255, 255))
		continuar_text = self.sub_font.render("Continuar partida [C]", 0, (255, 255, 255))
		creditos_text = self.sub_font.render("Creditos [D]", 0, (255, 255, 255))

		miTexto_rect = miTexto.get_rect(center=(screen_width/2,screen_height/2-250))
		subtitulo_rect = subtitulo.get_rect(center=(screen_width/2,screen_height/2-150))
		nuevo_rect = nuevo_text.get_rect(center=(screen_width/2,screen_height/2))
		continuar_rect = continuar_text.get_rect(center=(screen_width/2,screen_height/2+100))
		creditos_rect = creditos_text.get_rect(center=(screen_width/2,screen_height/2+200))

		keys = pygame.key.get_pressed()
		if keys[pygame.K_n]:
			self.create_overworld(0,0)
		elif keys[pygame.K_c]:
			#leer archivo
			nivel_max = 6
			self.create_overworld(0,nivel_max)
		elif keys[pygame.K_d]:
			self.create_credits(self.surface)


		fondo = pygame.image.load("imagenes/fondos/base2.jpeg").convert_alpha()
		fondo = pygame.transform.scale(fondo, (screen_width,screen_height)) 
		self.surface.blit(fondo,(0,0))
		pygame.draw.rect(self.surface, (0, 0, 0), miTexto_rect)
		pygame.draw.rect(self.surface, (0, 0, 0), subtitulo_rect)
		pygame.draw.rect(self.surface, (0, 0, 0), nuevo_rect)
		pygame.draw.rect(self.surface, (0, 0, 0), continuar_rect)
		pygame.draw.rect(self.surface, (0, 0, 0), creditos_rect)
		self.surface.blit(miTexto,miTexto_rect)
		self.surface.blit(subtitulo,subtitulo_rect)
		self.surface.blit(nuevo_text,nuevo_rect)
		self.surface.blit(continuar_text,continuar_rect)
		self.surface.blit(creditos_text,creditos_rect)

	