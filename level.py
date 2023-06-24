import pygame, random
from tiles import Tile
from settings import tile_size, screen_width
from player import Player
from ecuacion import Ecuacion
from respuestas import Respuestas


class Level:
	def __init__(self, level_data,surface,current_level,create_overworld):
		self.display_surface = surface
		self.setup_level(level_data,current_level)
		self.world_shift = 0
		self.current_level = current_level
		self.new_max_level = 2
		self.create_overworld = create_overworld
		self.alternancia_r = 0
		self.alternancia_l = 0

	def setup_level(self,layout,level):
		self.level = level
		self.tiles = pygame.sprite.Group()
		self.player = pygame.sprite.GroupSingle()
		self.ecuacion = pygame.sprite.GroupSingle()
		self.respuestas_r = pygame.sprite.Group()
		self.respuestas_l = pygame.sprite.Group()

		for row_index, row in enumerate(layout):
			for col_index, cell in enumerate(row):
				x = col_index*tile_size
				y = row_index*tile_size

				if cell == 'X':    
					tile = Tile((x,y),tile_size)
					self.tiles.add(tile)			
				if cell == 'P':    
					player_sprite = Player((x,y))
					self.player.add(player_sprite)
				if cell == 'E':
					self.ecuacion_sprite = Ecuacion((x,y),tile_size,self.level)
					self.ecuacion.add(self.ecuacion_sprite)
					#las respuestas empiezan en los sprites R
				if cell == 'R':
					respuesta_sprite_r = Respuestas((x,y),tile_size,1)

					self.respuestas_r.add(respuesta_sprite_r)
				if cell == 'L':
					respuesta_sprite_l = Respuestas((x,y),tile_size,1)

					self.respuestas_l.add(respuesta_sprite_l)			
		sprite = random.choice(self.respuestas_r.sprites())
		sprite.texto = 	str(self.ecuacion_sprite.respuesta_correcta)

	def scroll_x(self):
		player = self.player.sprite
		player_x = player.rect.centerx
		direction_x = player.direction.x
		if player_x < screen_width/4 and direction_x < 0:
			self.world_shift = 8
			player.speed = 0
		elif player_x > screen_width - (screen_width/4) and direction_x > 0:
			self.world_shift = -8
			player.speed = 0	    	
		else:
			self.world_shift = 0
			player.speed = 8

	def horizontal_movement_collision(self,type_sprites):
		player = self.player.sprite
		player.rect.x += player.direction.x*player.speed

		for sprite in type_sprites:
			if sprite.rect.colliderect(player.rect) and player.rect.y > sprite.rect.y:
				if player.direction.x < 0:
					player.rect.left = sprite.rect.right
				elif player.direction.x > 0:
				    player.rect.right = sprite.rect.left
				keys = pygame.key.get_pressed()
				if keys[pygame.K_a] and type_sprites != self.tiles.sprites():
					self.collision_respuestas(sprite,type_sprites)					    	
	
	def vertical_movement_collision(self,type_sprites):
		player = self.player.sprite
		player.apply_gravity()

		for sprite in type_sprites:
			if sprite.rect.colliderect(player.rect):
				if player.direction.y > 0:
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
				elif player.direction.y < 0:
				    player.rect.top = sprite.rect.bottom
				    player.direction.y = 0
				keys = pygame.key.get_pressed()    
				if keys[pygame.K_a] and type_sprites != self.tiles.sprites():
					self.collision_respuestas(sprite,type_sprites)	

	def collision_respuestas(self,sprite,type_sprites):
	
		if type_sprites == self.respuestas_r.sprites():
			type_sprites = self.respuestas_l.sprites()
			self.alternancia_r += 1
			self.alternancia_l = 0
		else:
			type_sprites = self.respuestas_r.sprites()
			self.alternancia_l += 1 
			self.alternancia_r = 0

		sprite.revisar(self.ecuacion_sprite.respuesta_correcta,self.display_surface)

        if self.alternancia == 1:
			respuetas_temporal = []
			self.ecuacion_sprite.respuesta_correcta = self.ecuacion_sprite.generator(self.level)         	
			for sprite in type_sprites:
				if screen_width/4 < sprite.rect.x and sprite.rect.x < screen_width :
					sprite.texto = str(2)
					respuetas_temporal.append(sprite)

			sprite = random.choice(respuetas_temporal)	
			sprite.texto = 	str(self.ecuacion_sprite.respuesta_correcta)		
			

	def input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RETURN]:
			self.create_overworld(self.current_level,self.new_max_level)
		if keys[pygame.K_ESCAPE]:
			self.create_overworld(self.current_level,0)
			

	def run(self):
		self.input()
		self.tiles.update(self.world_shift)
		self.tiles.draw(self.display_surface)
		self.scroll_x()

		self.player.update()
		self.horizontal_movement_collision(self.tiles.sprites())
		self.vertical_movement_collision(self.tiles.sprites())

		self.horizontal_movement_collision(self.respuestas_r.sprites())
		self.vertical_movement_collision(self.respuestas_r.sprites())
		self.horizontal_movement_collision(self.respuestas_l.sprites())
		self.vertical_movement_collision(self.respuestas_l.sprites())		
		self.player.draw(self.display_surface)
        
		self.ecuacion.update()
		self.ecuacion.draw(self.display_surface)

		self.respuestas_r.update(self.world_shift)
		self.respuestas_r.draw(self.display_surface)
		self.respuestas_l.update(self.world_shift)
		self.respuestas_l.draw(self.display_surface)

