import pygame, sys
from game_data import screen_width,screen_height
import csv

class Pantalla_resultados:
	def __init__(self,surface,create_overworld,inicio,palomas,ecuaciones,fin,new_max_level,meta):
		self.surface = surface
		self.new_max_level = new_max_level #mientras se prueba
		self.create_overworld = create_overworld
		self.main_font = pygame.font.SysFont("Courier", 80)
		self.sub_font = pygame.font.SysFont("Courier", 40)
		#resultados
		self.meta = meta
		self.tiempo = round(fin-inicio,2)
		self.palomas = palomas
		self.errores = ecuaciones - palomas
		self.puntaje = round(self.tiempo*100 - self.palomas*10 + self.errores*100,2)

		self.tiempo_text  = self.main_font.render('Tiempo: '+str(self.tiempo) +' seg.', 0, (255, 255, 255))
		self.palomas_text = self.main_font.render('Correctas: '+str(self.palomas), 0, (255, 255, 255))
		self.errores = self.main_font.render('Errores: '+str(self.errores), 0, (255, 255, 255))
		self.puntaje = self.main_font.render('Puntaje: '+str(self.puntaje), 0, (255, 255, 255))
		self.mensaje = self.sub_font.render('Presiona [Z] para regresar al mapa', 0, (255, 255, 255))
		self.nivel = self.main_font.render('Nivel: '+str(self.new_max_level), 0, (255, 255, 255))

	def run(self):
		nivel_rect = self.nivel.get_rect(center=(screen_width/2,screen_height/2-350))
		tiempo_rect = self.tiempo_text.get_rect(center=(screen_width/2,screen_height/2-200))
		palomas_rect = self.palomas_text.get_rect(center=(screen_width/2,screen_height/2-50))
		errores_rect = self.errores.get_rect(center=(screen_width/2,screen_height/2+100))
		puntaje_rect = self.puntaje.get_rect(center=(screen_width/2,screen_height/2+250))
		mensaje_rect = self.mensaje.get_rect(center=(screen_width/2,screen_height/2+400))
		fondo = pygame.image.load("imagenes/fondos/taller.jpeg").convert_alpha()
		fondo = pygame.transform.scale(fondo, (screen_width,screen_height)) 

		keys = pygame.key.get_pressed()
		if keys[pygame.K_z]:
			#if self.palomas < 5 or not(self.meta):
			#	self.new_max_level-=1
			self.create_overworld(self.new_max_level-1,11)#mientras se prueba


		self.surface.blit(fondo,(0,0))
		#pygame.draw.rect(self.surface, (0, 0, 0), miTexto_rect)
		#pygame.draw.rect(self.surface, (0, 0, 0), subtitulo_rect)
		self.surface.blit(self.nivel,nivel_rect)
		self.surface.blit(self.tiempo_text,tiempo_rect)
		self.surface.blit(self.palomas_text,palomas_rect)
		self.surface.blit(self.errores,errores_rect)
		self.surface.blit(self.puntaje,puntaje_rect)
		self.surface.blit(self.mensaje,mensaje_rect)

	