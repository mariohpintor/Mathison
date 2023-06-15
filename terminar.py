import pygame


class Terminar(pygame.sprite.Sprite):
	def __init__(self,pos,size):
		super().__init__()
		self.image = pygame.image.load("imagenes/murodelgado.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (size,size))
		self.rect = self.image.get_rect(topleft = pos)

	def finish_level():
		pass