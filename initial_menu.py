import pygame, sys
from settings import *

class Imenu:
	def __init__(self,surface,create_overworld):
		self.surface = surface
		self.create_overworld = create_overworld
		self.main_font = pygame.font.SysFont("arial", 80)

	def run(self):
		miTexto = self.main_font.render("MATHISON", 0, (166, 172, 175))
		subtitulo = self.main_font.render("[Un juego de ecuaciones]", 0, (166, 172, 175))
		miTexto_rect = miTexto.get_rect(center=(screen_width/2,screen_height/2-200))
		subtitulo_rect = subtitulo.get_rect(center=(screen_width/2,screen_height/2))
  
		keys = pygame.key.get_pressed()
		if keys[pygame.K_z]:
			self.create_overworld(0,3)    

		self.surface.fill((21, 67, 96))
		self.surface.blit(miTexto,miTexto_rect)
		self.surface.blit(subtitulo,subtitulo_rect)
	