import pygame
from support import import_folder

class Player(pygame.sprite.Sprite):
	def __init__(self,pos):
		super().__init__()
		self.import_character_assets()
		self.frame_index = 0
		self.animation_speed = 0.1
		self.image = self.animations['run'][self.frame_index]
		self.image = pygame.transform.scale(self.image, (48,96))
		self.rect = self.image.get_rect(topleft = pos)
		self.pos = pos
		

		#player movement
		self.direction = pygame.math.Vector2(0,0)
		self.speed = 8
		self.gravity = 0.8
		self.jump_speed = -12
		self.facing_right = True

	def import_character_assets(self):
		character_path = 'imagenes/'
		self.animations = {'run':[]}

		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)
	
	def animate(self):
		animation = self.animations['run']

		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0
		self.image = animation[int(self.frame_index)]
		self.image = pygame.transform.scale(self.image, (48,96))

		if self.facing_right:
			self.image = self.image
		else:
			flipped_image = pygame.transform.flip(self.image,True,False)
			self.image = flipped_image

	def get_input(self):
	    keys = pygame.key.get_pressed()

	    if keys[pygame.K_RIGHT]:
	    	self.direction.x = 1
	    	self.facing_right = True
	    elif keys[pygame.K_LEFT]:
	    	self.direction.x = -1
	    	self.facing_right = False
	    else:
	        self.direction.x = 0	

	    if keys[pygame.K_UP]:
	        self.jump()    

	def apply_gravity(self):
	    self.direction.y += self.gravity
	    self.rect.y += self.direction.y

	def jump(self):
	    self.direction.y = self.jump_speed    

	def update(self):
	    self.get_input()
	    self.apply_gravity()      
	    self.animate()