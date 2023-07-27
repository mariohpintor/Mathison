import pygame
from support import import_folder
'''
class Tile(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		#self.image = pygame.Surface((size,size))
		#self.image.fill((0,153,0))
		self.image = pygame.image.load("../archivos_produccion/terreno.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (size,size))
		self.rect = self.image.get_rect(topleft = pos)
'''

#Clases de tiles
class Tile(pygame.sprite.Sprite):
	def __init__(self,size,x,y):
		super().__init__()
		self.image = pygame.Surface((size,size))
		self.rect = self.image.get_rect(topleft = (x,y))

	def update(self, x_shift):
	    self.rect.x += x_shift			

class StaticTile(Tile):
	def __init__(self,size,x,y,surface):
		super().__init__(size,x,y)
		self.image = surface

class AnimatedTile(Tile):
	def __init__(self,size,x,y,path):
		super().__init__(size,x,y)
		self.frames = import_folder(path)
		self.frame_index = 1
		self.image = self.frames[self.frame_index]

	def animate(self):
		self.frame_index += 0.15
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self,shift):
		self.animate()
		self.rect.x += shift	



