import pygame, sys, random

class Ecuacion(pygame.sprite.Sprite):
	def __init__(self,pos,size,nivel):
		super().__init__()
		self.pos = pos
		self.respuesta_correcta = self.generator(nivel)
		self.color = 'red'
		self.main_font = pygame.font.SysFont('arial', size)
		self.miTexto = self.main_font.render(self.texto, 0,self.color)
		self.rect = self.miTexto.get_rect(topleft = self.pos)
		W = self.miTexto.get_width()
		H = self.miTexto.get_height()
		self.image = pygame.image.load("imagenes/cartel.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (W + 40,H))
		#self.image = pygame.Surface((W + 20,H + 20))
		self.image.blit(self.miTexto, [10,0])

	def generator(self,nivel):
		a = random.randint(1,10)
		b = random.randint(1,10)
		#c = random.randint(1,10)		
		if nivel == 0:
			operacion = '+'
			respuesta = round(b-a,2)
		elif nivel == 1:
			operacion = 'x'
			respuesta = round(b/a,2)
		elif nivel == 2:
			operacion = '/'
			respuesta = round(a/b,2)		
		self.texto = str(a) +' ' +operacion +' ? ' + ' = ' + str(b)
		return respuesta

	def update(self):
		self.miTexto = self.main_font.render(self.texto, 0,self.color)
		self.rect = self.miTexto.get_rect(topleft = self.pos)
		W = self.miTexto.get_width()
		H = self.miTexto.get_height()
		self.image = pygame.image.load("imagenes/cartel.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (W + 40,H))
		self.image.blit(self.miTexto, [10,0])