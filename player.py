import pygame
from support import import_folder
from math import sin

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,change_health):
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

		# health management
		self.change_health = change_health
		self.invincible = False
		self.invincible_duration = 400
		self.hurt_time = 0

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

		if self.invincible:
			alpha = self.wave_value()
			self.image.set_alpha(alpha)
		else:
			self.image.set_alpha(255)

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

	def get_damage(self):
		if not self.invincible:
			self.change_health(-10)
			self.invincible = True
			self.hurt_time = pygame.time.get_ticks()

	def invincibility_timer(self):
		if self.invincible:
			current_time = pygame.time.get_ticks()
			if current_time - self.hurt_time >= self.invincible_duration:
				self.invincible = False

	def wave_value(self):
		value = sin(pygame.time.get_ticks())
		if value >= 0: return 255
		else: return 0

	def update(self):
	    self.get_input()
	    self.apply_gravity()      
	    self.animate()
	    self.invincibility_timer()