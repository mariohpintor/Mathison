import pygame, sys, random

class Ecuacion(pygame.sprite.Sprite):
	def __init__(self,pos,size,nivel):
		super().__init__()
		self.pos = pos
		self.respuesta_correcta = self.generator(nivel)
		self.color = 'red'
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
		a = random.randint(1,10)
		b = random.randint(1,10)
		#SUMA positiva	
		if nivel == 0:
			operacion = '+'
			respuesta = b-a
		elif nivel == 1:
			operacion = 'x'
			respuesta = round(b/a,2)
		elif nivel == 2:
			operacion = '/'
			respuesta = round(a/b,2)
		elif nivel == 3:
			c = random.randint(1,10)
			self.texto = str(a) + 'x + ' + str(b) + ' = ' + str(c)
			respuesta = round((c-b)/a,2) 
		elif nivel == 4:
			c = random.randint(1,10)
			self.texto = str(a) + '(x + ' + str(b) + ') = ' + str(c)
			respuesta = round(c/a - b,2)
		elif nivel == 5:
			c = random.randint(1,10)
			self.texto = str(a) + '/(x + ' + str(b) + ') = ' + str(c)
			respuesta = round(a/c - b,2) 

		if nivel < 3:		
			self.texto = str(a) +' ' + operacion +' ? ' + ' = ' + str(b)
		return respuesta

	def update(self):
		self.miTexto = self.main_font.render(self.texto, 0,self.color)
		self.rect = self.miTexto.get_rect(topleft = self.pos)
		w = self.miTexto.get_width()
		h = self.miTexto.get_height()
		self.image = pygame.image.load("imagenes/computer1.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (w+40,w*137/192))
		self.image.blit(self.miTexto, [20,(w*137/192)/2-h/2])