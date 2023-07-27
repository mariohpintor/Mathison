import pygame, random
from tiles import Tile
from settings import tile_size, screen_width, screen_height
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
		
		#Código nuevo ------------------

		#player 
		player_layout = import_csv_layout(level_data['player'])
		self.player = pygame.sprite.GroupSingle()
		self.goal = pygame.sprite.GroupSingle()
		self.player_setup(player_layout)

		#ecuacion
		ecuacion_layout = import_csv_layout(level_data['ecuacion'])
		self.ecuacion = pygame.sprite.GroupSingle()

		#terrain setup

		terrain_layout = import_csv_layout(level_data['terrain'])
		self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain')

		#'respuestas_r' setup

		respuestas_r_layout = import_csv_layout(level_data['respuestas_r'])
		self.respuestas_r_sprites = self.create_tile_group(respuestas_r_layout,'respuestas_r')

		#'respuestas_l' setup

		respuestas_l_layout = import_csv_layout(level_data['respuestas_l'])
		self.respuestas_l_sprites = self.create_tile_group(respuestas_l_layout,'respuestas_l')

		#enemy
		enemy_layout = import_csv_layout(level_data['enemies'])
		self.enemy_sprites = self.create_tile_group(enemy_layout, 'enemies')

		#constraint
		constrains_layout = import_csv_layout(level_data['constrains'])
		self.constrains_sprites = self.create_tile_group(constrains_layout, 'constrains')

	def create_tile_group(self, layout, type):
		sprite_group = pygame.sprite.Group()

		for row_index, row in enumerate(layout):
			for col_index, val in enumerate(row):
				if val != '-1':
					x = col_index*tile_size
					y = row_index*tile_size

					if type == 'terrain':
						terrain_tile_list = import_cut_graphics('../niveles_mathison/imagenes_nivel/terrain_tiles.png')
						tile_surface = terrain_tile_list[int(val)]
						sprite = StaticTile(tile_size,x,y,tile_surface)

					if type == 'respuestas_r':
						sprite = Respuestas((x,y),tile_size,random.randint(-5,5))

					if type == 'respuestas_l':
						sprite = Respuestas((x,y),tile_size,random.randint(-5,5))

					if type == 'enemies':
						sprite = Enemy(tile_size,x,y)

					if type == 'constrains':
						sprite = Tile(tile_size,x,y)

				
					sprite_group.add(sprite)

		return sprite_group	

	def player_setup(self,layout):
		for row_index, row in enumerate(layout):
			for col_index, val in enumerate(row):
				x = col_index*tile_size
				y = row_index*tile_size
				if val == '0':
					print('player goes here')
				if val == '1':
					hat_surface = pygame.image.load('../graphics/character/hat.png').convert_alpha()
					sprite = StaticTile(tile_size,x,y,hat_surface)
					self.goal.add(sprite)

	def enemy_collision_reverse(self):
		for enemy in self.enemy_sprites.sprites():
			if pygame.sprite.spritecollide(enemy,self.constrains_sprites,False):
				enemy.reverse()	
		#------------------------------------------------------------------
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
					respuesta_sprite_r = Respuestas((x,y),tile_size,random.randint(-5,5))

					self.respuestas_r.add(respuesta_sprite_r)
				if cell == 'L':
					respuesta_sprite_l = Respuestas((x,y),tile_size,random.randint(-5,5))

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
			self.alternancia_r += 1
			self.alternancia_l = 0
		else:
			self.alternancia_l += 1 
			self.alternancia_r = 0

		if self.alternancia_r == 1 or self.alternancia_l == 1:
			sprite.revisar(self.ecuacion_sprite.respuesta_correcta,self.display_surface)
			for sprite in type_sprites:
				sprite.texto = 'x'			
			if self.alternancia_r == 1:
				type_sprites = self.respuestas_l.sprites()
			if self.alternancia_l == 1:
				type_sprites = self.respuestas_r.sprites()	

			respuetas_temporal = []
			self.ecuacion_sprite.respuesta_correcta = self.ecuacion_sprite.generator(self.level)         	
			for sprite in type_sprites:
				if screen_width/4 < sprite.rect.x and sprite.rect.x < screen_width :
					sprite.texto = str(random.randint(-5,5))
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
		fondo = pygame.image.load("../archivos_produccion/fondos/university.jpeg").convert_alpha()
		fondo = pygame.transform.scale(fondo, (screen_width,screen_height)) 
		self.display_surface.blit(fondo,(0,0))
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

		#Código nuevo ---------------------------------

		self.terrain_sprites.update(self.world_shift)
		self.terrain_sprites.draw(self.display_surface)
		self.enemy_collision_reverse()

		self.respuestas_r_sprites.update(self.world_shift)
		self.respuestas_r_sprites.draw(self.display_surface)

		self.respuestas_l_sprites.update(self.world_shift)
		self.respuestas_l_sprites.draw(self.display_surface)

		self.enemy_sprites.update(self.world_shift)
		self.enemy_sprites.draw(self.display_surface)

		self.constrains_sprites.update(self.world_shift)

		#------------------------------------------------------------------


