import pygame, random
from tiles import Tile
from settings import tile_size, screen_width
from player import Player
from ecuacion import Ecuacion
from respuestas import Respuestas
#from terminar import Terminar

class Level:
	def __init__(self, level_data,surface,current_level,create_overworld):
		self.display_surface = surface
		self.setup_level(level_data,current_level)
		self.world_shift = 0
		self.current_level = current_level
		self.new_max_level = 2
		self.create_overworld = create_overworld

	def setup_level(self,layout,level):
		i = 0
		respuesta =[]
		self.level = level
		self.tiles = pygame.sprite.Group()
		self.player = pygame.sprite.GroupSingle()
		self.ecuacion = pygame.sprite.GroupSingle()
		self.respuestas = pygame.sprite.Group()
		self.terminar = pygame.sprite.GroupSingle()

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
					respuesta.append(self.ecuacion_sprite.respuesta_correcta)
					#print('E',respuesta)
				if cell == 'R':
					if i < 3:
						respuesta.append(random.randint(1,10))
					answer = random.choice(respuesta)	
					respuesta_sprite = Respuestas((x,y),tile_size,answer)
					i+=1
					respuesta.remove(answer)
					#print('R',respuesta)
					self.respuestas.add(respuesta_sprite)
				#if cell == 'T':
				   #terminar_sprite = Terminar((x,y),tile_size)
				   #self.terminar.add(terminar_sprite)	

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

	def horizontal_movement_collision(self):
		player = self.player.sprite
		player.rect.x += player.direction.x*player.speed

		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect) and player.rect.y > sprite.rect.y:
				if player.direction.x < 0:
					player.rect.left = sprite.rect.right
				elif player.direction.x > 0:
				    player.rect.right = sprite.rect.left	
	
	def vertical_movement_collision(self):
		player = self.player.sprite
		player.apply_gravity()

		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direction.y > 0:
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
				elif player.direction.y < 0:
				    player.rect.top = sprite.rect.bottom
				    player.direction.y = 0	

	def collision_respuestas(self):
		player = self.player.sprite
		for sprite in self.respuestas.sprites():
			if sprite.rect.colliderect(player.rect):
				sprite.revisar(self.ecuacion_sprite.respuesta_correcta)
				nueva_respuesta = self.ecuacion_sprite.generator(self.level)
				for sprite in self.respuestas.sprites():
					sprite.texto = str(random.randint(1,10))
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
		self.horizontal_movement_collision()
		self.vertical_movement_collision()
		self.player.draw(self.display_surface)
        
		self.ecuacion.update()
		self.ecuacion.draw(self.display_surface)
		self.respuestas.update(self.world_shift)
		self.collision_respuestas()	
		self.respuestas.draw(self.display_surface)

		#self.terminar.draw(self.display_surface)	

