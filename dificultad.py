import pygame
from game_data import screen_width,screen_height,AMARILLO

class Dificultad:
	def __init__(self,surface,create_initial_menu,create_overworld):
		self.surface = surface
		self.create_initial_menu = create_initial_menu
		self.create_overworld = create_overworld
		self.main_font = pygame.font.SysFont("tahoma", 60)
		self.sub_font = pygame.font.SysFont("tahoma", 40)

	def run(self):
		titulo = self.main_font.render("Dificultad", 0, (255, 255, 255))
		explorar  = self.sub_font.render("Explorar [E]", 0, AMARILLO)
		facil = self.sub_font.render("Fácil [F]", 0, AMARILLO)
		normal = self.sub_font.render('Normal [N]', 0, AMARILLO)
		mensaje = self.sub_font.render('Presiona [Z] para regresar',0, 'white')
		mensaje_rect = mensaje.get_rect(center=(screen_width/2,screen_height - 50))

		titulo_rect = titulo .get_rect(center=(screen_width/2,50))
		explorar_rect = explorar.get_rect(center=(screen_width/2,screen_height/2-200))
		facil_rect = facil.get_rect(center=(screen_width/2,screen_height/2))
		normal_rect = normal.get_rect(center=(screen_width/2,screen_height/2+200))

		keys = pygame.key.get_pressed()
		if keys[pygame.K_e]:
			self.create_overworld(0,11,0)
		if keys[pygame.K_f]:
			self.create_overworld(0,0,1)
		if keys[pygame.K_n]:
			self.create_overworld(0,0,2)
		if keys[pygame.K_z]:
			self.create_initial_menu()

		fondo = pygame.image.load("imagenes/fondos/dificulty.jpeg").convert_alpha()
		fondo = pygame.transform.scale(fondo, (screen_width,screen_height)) 
		self.surface.blit(fondo,(0,0))
		pygame.draw.rect(self.surface, (0, 0, 0),titulo_rect)
		pygame.draw.rect(self.surface, (0, 0, 0),explorar_rect)
		pygame.draw.rect(self.surface, (0, 0, 0), facil_rect)
		pygame.draw.rect(self.surface, (0, 0, 0), normal_rect)
		self.surface.blit(titulo,titulo_rect)
		self.surface.blit(explorar,explorar_rect)
		self.surface.blit(facil,facil_rect)
		self.surface.blit(normal,normal_rect)
		self.surface.blit(mensaje,mensaje_rect)
