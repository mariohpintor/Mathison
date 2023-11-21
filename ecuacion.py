import pygame, sys, random

class Ecuacion(pygame.sprite.Sprite):
	def __init__(self,pos,size,nivel):
		super().__init__()
		self.pos = pos
		self.respuesta_correcta = self.generator(nivel)
		self.color = 'red'
		#self.texto = '¡Hola!'
		self.main_font = pygame.font.SysFont('Arial Rounded MT Bold', size)
		self.miTexto = self.main_font.render(self.texto, 0,self.color)
		self.rect = self.miTexto.get_rect(topleft = self.pos)
		w = self.miTexto.get_width()
		h = self.miTexto.get_height()
		self.image = pygame.image.load("imagenes/computer1.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (w+40,w*137/192))
		#self.image = pygame.Surface((W + 20,H + 20))
		self.image.blit(self.miTexto, [20,(w*137/192)/2-h/2])

	def generator(self,nivel):
		#ADICION POSITIVA
		if nivel == 0:
			a = random.randint(1,10)
			b = a + random.randint(1,10)
			self.texto = str(a) +' + x ' + ' = ' + str(b)
			respuesta = b - a
		#ADICION NEGATIVA
		elif nivel == 1:
			a = random.randint(1,10)
			b = a + random.randint(1,10)
			self.texto = str(b) +' - x ' + ' = ' + str(a)
			respuesta = b - a
		#ADICION COMBINADA
		elif nivel == 2:
			a = random.randint(1,10)
			b = random.randint(1,10)
			self.texto = str(a) +' + x ' + ' = ' + str(b)
			respuesta = b - a
		#MULTIPLICACION ENTERA POSITIVA
		elif nivel == 3:
			a = random.randint(2,10)
			b = random.randint(1,10)*a
			self.texto = str(a) +' x ' + ' = ' + str(b)
			respuesta = b//a
		#MULTIPLICACION ENTERA NEGATIVA (ERROR)
		elif nivel == 4:
			a = random.randint(2,10)
			b = -random.randint(1,10)*a
			self.texto = str(a) +' x ' + ' = ' + str(b)
			respuesta =  (b//a)
		#DIVISION ENTERA COMBINADA	
		elif nivel == 5:
			a = random.randint(1,10)
			b = random.randint(2,10)
			self.texto = ' x/' +str(b) + ' = ' + str(a)
			respuesta = b*a

		#ADICION Y PRODUCTO POSITIVO
		elif nivel == 6:
			a = random.randint(2,10)
			c = random.randint(1,10)*a
			b = c//a - random.randint(0,c//a)
			self.texto = str(a) + '(x  + ' + str(b) + ') = ' + str(c)
			respuesta = c//a - b
		#ADICION Y PRODUCTO NEGATIVO
		elif nivel == 7:
			a = random.randint(2,10)
			c = random.randint(1,10)*a
			b = c//a + random.randint(1,10)
			self.texto = str(a) + '('+ str(b) + ' - x) = ' + str(c)
			respuesta = b - c//a
		#ADICION Y PRODUCTO COMBINADO
		elif nivel == 8:
			a = random.randint(2,10)
			b = random.randint(1,10)
			c = random.randint(1,10)*a
			self.texto = str(a) + '(x  + ' + str(b) + ') = ' + str(c)
			respuesta = c//a - b
		#ADICION Y DIVISION POSITIVO
		elif nivel == 9:
			a = random.randint(1,10)
			c = random.randint(2,7)
			b = a*c - random.randint(0,a*c)
			self.texto = '('+ str(b) + ' + x)/'+str(c)+' = ' + str(a)
			respuesta = a*c - b
		#ADICION Y DIVISION NEGATIVO
		elif nivel == 10:
			a = random.randint(1,10)
			b = random.randint(1,10)
			c = random.randint(2,10)
			self.texto = '('+ str(b) + ' - x)/'+str(c)+' = ' + str(a)
			respuesta = b - a*c
		#ADICION Y DIVISION COMBINADO
		elif nivel == 11:
			a = random.randint(1,10)
			c = random.randint(2,10)
			b = random.randint(1,10)
			self.texto = '('+ str(b) + ' + x)/'+str(c)+' = ' + str(a)
			respuesta = a*c - b
			
		return str(respuesta)

	def update(self):
		self.miTexto = self.main_font.render(self.texto, 0,self.color)
		self.rect = self.miTexto.get_rect(topleft = self.pos)
		w = self.miTexto.get_width()
		h = self.miTexto.get_height()
		self.image = pygame.image.load("imagenes/computer1.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (w+40,w*137/192))
		self.image.blit(self.miTexto, [20,(w*137/192)/2-h/2])