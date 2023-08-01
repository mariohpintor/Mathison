import pygame, sys, random

class Respuestas(pygame.sprite.Sprite):
	def __init__(self,pos,size,respuesta):
		super().__init__()
		#texto
		#self.pos = pos
		self.size = size
		self.texto = str(respuesta)
		self.color = (23, 32, 42  )
		self.main_font = pygame.font.SysFont('arial', size - 7)
		self.mitexto = self.main_font.render(self.texto, True,self.color)
        #rect and image
		self.rect = self.mitexto.get_rect(topleft=pos)
		self.W = self.mitexto.get_width()
		self.H = self.mitexto.get_height()
		self.image = pygame.image.load("../niveles_mathison/imagenes_nivel/respuesta.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (self.W + 20,self.H))		
		self.image.blit(self.mitexto,[10,0])
		

		# (self.W + 20,self.H)
	def revisar(self,respuesta_correcta,surface):
		if respuesta_correcta ==float(self.texto):
			calificacion = pygame.image.load("imagenes/paloma.png").convert_alpha()
			calificacion = pygame.transform.scale(calificacion,(self.size*2,self.size*2))
			print(self.texto)
		else:
			calificacion = pygame.image.load("imagenes/error.png").convert_alpha()
			calificacion = pygame.transform.scale(calificacion,(self.size*2,self.size*2))					
		surface.blit(calificacion,(4*64,64))   		

	def update(self, x_shift):
		self.mitexto = self.main_font.render(self.texto, True,self.color)
        #rect and image
		self.rect.x += x_shift	
		self.W = self.mitexto.get_width()
		self.H = self.mitexto.get_height()
		self.image = pygame.image.load("../niveles_mathison/imagenes_nivel/respuesta.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (self.W + 20,self.H))		
		self.image.blit(self.mitexto,[10,0])

