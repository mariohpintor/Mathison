import pygame, sys
from game_data import screen_width,screen_height
import csv

class Pantalla_resultados:
	def __init__(self,surface,create_overworld,inicio,palomas,ecuaciones,fin,new_max_level,meta):
		self.surface = surface
		self.new_max_level = new_max_level
		self.create_overworld = create_overworld
		self.main_font = pygame.font.SysFont("Courier", 80)
		self.sub_font = pygame.font.SysFont("Courier", 40)
		#resultados
		self.meta = meta
		self.tiempo = round(fin-inicio,2)
		self.palomas = palomas
		self.errores = ecuaciones - palomas
		self.puntaje = round(self.tiempo,2)*100 - self.palomas*10 + self.errores*100


		# Definir los datos que deseas agregar en formato de lista
		nuevo_registro = [self.new_max_level-1, self.tiempo, self.palomas, self.errores, self.puntaje]

		# Nombre del archivo CSV
		archivo_csv = 'datos.csv'

		# Abrir el archivo en modo agregar (si no existe, se crea)
		with open(archivo_csv, 'a', newline='') as archivo:
		    escritor_csv = csv.writer(archivo)
		    # Agregar los datos como una fila en el archivo CSV
		    escritor_csv.writerow(nuevo_registro)

		self.tiempo_text  = self.main_font.render('Tiempo: '+str(self.tiempo) +' seg.', 0, (255, 255, 255))
		self.palomas_text = self.main_font.render('Correctas: '+str(self.palomas), 0, (255, 255, 255))
		self.errores = self.main_font.render('Errores: '+str(self.errores), 0, (255, 255, 255))
		self.puntaje = self.main_font.render('Puntaje: '+str(self.puntaje), 0, (255, 255, 255))
		self.mensaje = self.sub_font.render('Presiona [Z] para regresar al mapa', 0, (255, 255, 255))

	def run(self):
		tiempo_rect = self.tiempo_text.get_rect(center=(screen_width/2,screen_height/2-300))
		palomas_rect = self.palomas_text.get_rect(center=(screen_width/2,screen_height/2-150))
		errores_rect = self.errores.get_rect(center=(screen_width/2,screen_height/2))
		puntaje_rect = self.puntaje.get_rect(center=(screen_width/2,screen_height/2+150))
		mensaje_rect = self.mensaje.get_rect(center=(screen_width/2,screen_height/2+300))
		fondo = pygame.image.load("imagenes/fondos/taller.jpeg").convert_alpha()
		fondo = pygame.transform.scale(fondo, (screen_width,screen_height)) 

		keys = pygame.key.get_pressed()
		if keys[pygame.K_z]:
			if self.palomas < 5 and not(self.meta):
				self.new_max_level-=1
			self.create_overworld(0,self.new_max_level)


		self.surface.blit(fondo,(0,0))
		#pygame.draw.rect(self.surface, (0, 0, 0), miTexto_rect)
		#pygame.draw.rect(self.surface, (0, 0, 0), subtitulo_rect)
		self.surface.blit(self.tiempo_text,tiempo_rect)
		self.surface.blit(self.palomas_text,palomas_rect)
		self.surface.blit(self.errores,errores_rect)
		self.surface.blit(self.puntaje,puntaje_rect)
		self.surface.blit(self.mensaje,mensaje_rect)

	