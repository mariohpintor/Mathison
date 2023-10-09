import pygame, sys
from game_data import screen_width,screen_height

class Imenu:
	def __init__(self,surface,create_overworld):
		self.surface = surface
		self.create_overworld = create_overworld
		self.main_font = pygame.font.SysFont("Courier", 100)
		self.sub_font = pygame.font.SysFont("Courier", 40)

	def run(self):
		miTexto = self.main_font.render("MATHISON", 0, (255, 255, 255))
		subtitulo = self.sub_font.render("[Un juego de ecuaciones]", 0, (255, 255, 255))
		instrucciones = self.sub_font.render('Presiona [ Z ] para iniciar',0,'white')
		miTexto_rect = miTexto.get_rect(center=(screen_width/2,screen_height/2-200))
		subtitulo_rect = subtitulo.get_rect(center=(screen_width/2,screen_height/2))
		instrucciones_rect = instrucciones.get_rect(center =(screen_width/2,screen_height/2+300))

		keys = pygame.key.get_pressed()
		if keys[pygame.K_z]:
			self.create_overworld(0,0)

		fondo = pygame.image.load("imagenes/fondos/main_menu1.jpeg").convert_alpha()
		fondo = pygame.transform.scale(fondo, (screen_width,screen_height)) 
		self.surface.blit(fondo,(0,0))
		pygame.draw.rect(self.surface, (0, 0, 0), miTexto_rect)
		pygame.draw.rect(self.surface, (0, 0, 0), subtitulo_rect)
		self.surface.blit(miTexto,miTexto_rect)
		self.surface.blit(subtitulo,subtitulo_rect)
		self.surface.blit(instrucciones,instrucciones_rect)

	