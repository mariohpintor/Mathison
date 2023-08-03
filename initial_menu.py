import pygame, sys
from settings import *

class Imenu:
	def __init__(self,surface,create_overworld):
		self.surface = surface
		self.create_overworld = create_overworld
		self.main_font = pygame.font.SysFont("Arial Rounded MT Bold", 80)
		self.sub_font = pygame.font.SysFont("Arial Rounded MT Bold", 40)

	def run(self):
		miTexto = self.main_font.render("MATHISON", 0, (36, 229, 14))
		subtitulo = self.main_font.render("[Un juego de ecuaciones]", 0, (36, 229, 14))
		instrucciones = self.sub_font.render('Presiona [ Z ] para iniciar',0,'white')
		miTexto_rect = miTexto.get_rect(center=(screen_width/2,screen_height/2-200))
		subtitulo_rect = subtitulo.get_rect(center=(screen_width/2,screen_height/2))
		instrucciones_rect = instrucciones.get_rect(center =(screen_width/2,screen_height/2+300))
  
		keys = pygame.key.get_pressed()
		if keys[pygame.K_z]:
			self.create_overworld(0,5)

		fondo = pygame.image.load("../imagenes/fondos/main_menu1.jpeg").convert_alpha()
		fondo = pygame.transform.scale(fondo, (screen_width,screen_height)) 
		self.surface.blit(fondo,(0,0))
		self.surface.blit(miTexto,miTexto_rect)
		self.surface.blit(subtitulo,subtitulo_rect)
		self.surface.blit(instrucciones,instrucciones_rect)
	