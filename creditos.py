import pygame, sys
from game_data import screen_width,screen_height

class Creditos:
	def __init__(self,surface,create_initial_menu):
		self.surface = surface
		self.create_initial_menu = create_initial_menu
		self.main_font = pygame.font.SysFont("Courier", 40)
		self.sub_font = pygame.font.SysFont("Courier", 40)

	def run(self):
		yo = self.main_font.render('Mario Alberto Hernández Pintor', 0, (255, 255, 255))
		zeleny = self.main_font.render('Pablo Rodrigo Zeleny Vázquez', 0, (255, 255, 255))
		facultad = self.main_font.render('FCFM-BUAP Otoño 2023', 0, (255, 255, 255))
		correo1 = self.main_font.render('marioalbertohp@outlook.com', 0, (255, 255, 255))
		correo2 = self.main_font.render('rodrigozeleny28@gmail.com', 0, (255, 255, 255))
		instruccion = self.main_font.render('Presiona [Z] para regresar', 0, (255, 255, 255))
		yo_rect = yo.get_rect(center=(screen_width/2,screen_height/2-300))
		zeleny_rect = zeleny.get_rect(center=(screen_width/2,screen_height/2-150))
		facultad_rect = facultad.get_rect(center=(screen_width/2,screen_height/2))
		correo1_rect = correo1.get_rect(center=(screen_width/2,screen_height/2+150))
		correo2_rect = correo2.get_rect(center=(screen_width/2,screen_height/2+300))
		instruccion_rect = instruccion.get_rect(center=(screen_width/2,screen_height/2+400))

		fondo = pygame.image.load("imagenes/fondos/base2.jpeg").convert_alpha()
		fondo = pygame.transform.scale(fondo, (screen_width,screen_height)) 

		keys = pygame.key.get_pressed()
		if keys[pygame.K_z]:
			self.create_initial_menu()
			print('z')

		self.surface.blit(fondo,(0,0))
		self.surface.blit(yo,yo_rect)
		self.surface.blit(zeleny,zeleny_rect)
		self.surface.blit(facultad,facultad_rect)
		self.surface.blit(correo1,correo1_rect)
		self.surface.blit(correo2,correo2_rect)
		self.surface.blit(instruccion,instruccion_rect)


	