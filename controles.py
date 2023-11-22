import pygame
from game_data import screen_width,screen_height

class Controles:
	def __init__(self,surface,create_initial_menu):
		self.surface = surface
		self.create_initial_menu = create_initial_menu
		self.main_font = pygame.font.SysFont("Courier", 40)

	def run(self):
		titulo = self.main_font.render("Controles", 0, (255, 255, 255))
		titulo_rect = titulo.get_rect(center=(screen_width/2,50))
		mensaje = self.main_font.render('Presiona [Z] para regresar',0, (255, 255, 255))
		mensaje_rect = mensaje.get_rect(center=(screen_width/2,screen_height - 50))

		keys = pygame.key.get_pressed()
		if keys[pygame.K_z]:
			self.create_initial_menu()


		fondo = pygame.image.load("imagenes/fondos/base2.jpeg").convert_alpha()
		fondo = pygame.transform.scale(fondo, (screen_width,screen_height)) 
		mathison  = pygame.image.load ('imagenes/run/turing.png').convert_alpha()
		mathison = pygame.transform.scale(mathison,(100,200)) 
		flecha = pygame.image.load ('imagenes/flecha.png').convert_alpha()
		flecha = pygame.transform.scale(flecha,(50,50)) 
		self.surface.blit(fondo,(0,0))
		self.surface.blit(mathison,(100,200))
		self.surface.blit(flecha,(130,400))
		self.surface.blit(flecha,(80,450))
		self.surface.blit(flecha,(180,450))
		self.surface.blit(titulo,titulo_rect)
		self.surface.blit(mensaje,mensaje_rect)

	