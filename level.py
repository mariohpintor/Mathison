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

	def setup_level(self,layout,level):
		contador = 0
		self.respuestas_positions =[]
		self.level = level
		self.tiles = pygame.sprite.Group()
		self.player = pygame.sprite.GroupSingle()
		self.ecuacion = pygame.sprite.GroupSingle()
		self.respuestas = pygame.sprite.Group()

		for row_index, row in enumerate(layout):
			for col_index, cell in enumerate(row):
				x = col_index*tile_size
				y = row_index*tile_size

				if cell == 'X':    
					tile = Tile((x,y),tile_size)
					self.tiles.add(tile)			
				if cell == 'P':    
					player_sprite = Player([x,y])
					self.player.add(player_sprite)
				if cell == 'E':
					self.ecuacion_sprite = Ecuacion((x,y),tile_size,self.level)
					self.ecuacion.add(self.ecuacion_sprite)
					#respuesta.append(self.ecuacion_sprite.respuesta_correcta)
				if cell == 'R':
					self.respuestas_positions.append((x,y))
					if ((x > player_sprite.rect.centerx and x < screen_width) or x < player_sprite.rect.centerx) and contador < 4:
						respuesta_sprite = Respuestas((x,y),tile_size,random.randint(1,10))
						contador += 1

					self.respuestas.add(respuesta_sprite)
		print(self.respuestas_positions)			
		sprite = random.choice(self.respuestas.sprites())
		sprite.texto = 	str(self.ecuacion_sprite.respuesta_correcta)

	def scroll_x(self):
		player = self.player.sprite
		player_x = player.rect.centerx
		direction_x = player.direction.x
		self.righttimes = 0
		if player_x < screen_width/4 and direction_x < 0:
			self.world_shift = 8
			player.speed = 0
			self.righttimes += 1
		elif player_x > screen_width - (screen_width/4) and direction_x > 0:
			self.world_shift = -8
			player.speed = 0
			self.righttimes += -1		    	
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
				#keys = pygame.key.get_pressed()
				if type_sprites == self.respuestas.sprites():
					self.collision_respuestas(sprite,player)					    	
	
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
				#keys = pygame.key.get_pressed()    
				if type_sprites == self.respuestas.sprites():
					self.collision_respuestas(sprite,player)	

	def collision_respuestas(self,sprite,player):
		sprite.revisar(self.ecuacion_sprite.respuesta_correcta)
		#cambiamos posiciones de respuestas	
		contador = 0
		changes = []
		for new_position in self.respuestas_positions:	
			if ((new_position[0] > player.rect.centerx +8*self.righttimes and new_position[0] < screen_width+8*self.righttimes) or (new_position[0] < player.rect.centerx+8*self.righttimes and new_position[0]>8*self.righttimes)) and contador < 4:
				changes.append(new_position)
				contador += 1
		print(changes)
		#actualizamos texto 
		nueva_respuesta = self.ecuacion_sprite.generator(self.level)
		contador = 0
		for sprite in self.respuestas.sprites():
			sprite.texto = str(random.randint(1,10))
			sprite.pos = changes[contador]
			contador += 1
		sprite = random.choice(self.respuestas.sprites())	
		sprite.texto = 	str(nueva_respuesta)		
			




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
		self.horizontal_movement_collision(self.respuestas.sprites())
		self.vertical_movement_collision(self.respuestas.sprites())
		self.player.draw(self.display_surface)
        
		self.ecuacion.update()
		self.ecuacion.draw(self.display_surface)
		self.respuestas.update(self.world_shift)
		#self.collision_respuestas()	
		self.respuestas.draw(self.display_surface)

		#self.terminar.draw(self.display_surface)	

