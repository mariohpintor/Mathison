import pygame, sys
from game_data import screen_width,screen_height,AMARILLO 
import csv

class Pantalla_resultados:
	def __init__(self,surface,create_overworld,inicio,palomas,ecuaciones,fin,new_max_level,meta,nivel_dificultad):
		self.surface = surface
		self.new_max_level = new_max_level 
		self.create_overworld = create_overworld
		self.main_font = pygame.font.SysFont("tahoma", 80)
		self.sub_font = pygame.font.SysFont("tahoma", 40)
		self.nivel_dificultad = nivel_dificultad
		#resultados
		self.meta = meta
		self.tiempo = round(fin-inicio,2)
		self.palomas = palomas
		self.errores = ecuaciones - palomas
		self.puntaje = round(self.tiempo*100 - self.palomas*10 + self.errores*100,2)
		self.current_level = new_max_level-1

		self.tiempo_text  = self.main_font.render('Tiempo: '+str(self.tiempo) +' seg.', 0, AMARILLO )
		self.palomas_text = self.main_font.render('Correctas: '+str(self.palomas), 0, AMARILLO )
		self.errores = self.main_font.render('Errores: '+str(self.errores), 0, AMARILLO )
		self.puntaje = self.main_font.render('Puntaje: '+str(self.puntaje), 0, AMARILLO )
		self.mensaje = self.sub_font.render('Presiona [Z] para regresar al mapa', 0,'white' )
		self.nivel = self.main_font.render('Nivel: '+str(self.new_max_level), 0, AMARILLO )

		if self.nivel_dificultad  == 0:
			self.new_max_level = 11
		elif self.nivel_dificultad  == 1:
			if self.palomas < 4:
				self.new_max_level -= 1
		else:
			if self.palomas < 9 or not self.meta:
				self.new_max_level -= 1

	def run(self):
		nivel_rect = self.nivel.get_rect(center=(screen_width/2,screen_height/2-350))
		tiempo_rect = self.tiempo_text.get_rect(center=(screen_width/2,screen_height/2-200))
		palomas_rect = self.palomas_text.get_rect(center=(screen_width/2,screen_height/2-50))
		errores_rect = self.errores.get_rect(center=(screen_width/2,screen_height/2+100))
		puntaje_rect = self.puntaje.get_rect(center=(screen_width/2,screen_height/2+250))
		mensaje_rect = self.mensaje.get_rect(center=(screen_width/2,screen_height/2+400))
		fondo = pygame.image.load("imagenes/fondos/taller1.jpeg").convert_alpha()
		fondo = pygame.transform.scale(fondo, (screen_width,screen_height)) 

		keys = pygame.key.get_pressed()
		if keys[pygame.K_z]:
			self.create_overworld(self.current_level,self.new_max_level,self.nivel_dificultad)

		self.surface.blit(fondo,(0,0))
		self.surface.blit(self.nivel,nivel_rect)
		self.surface.blit(self.tiempo_text,tiempo_rect)
		self.surface.blit(self.palomas_text,palomas_rect)
		self.surface.blit(self.errores,errores_rect)
		self.surface.blit(self.puntaje,puntaje_rect)
		self.surface.blit(self.mensaje,mensaje_rect)

	