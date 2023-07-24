import pygame

class Tile(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		#self.image = pygame.Surface((size,size))
		#self.image.fill((0,153,0))
		self.image = pygame.image.load("../archivos_produccion/terreno.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (size,size))
		self.rect = self.image.get_rect(topleft = pos)

	def update(self, x_shift):
	    self.rect.x += x_shift	