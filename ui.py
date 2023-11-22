import pygame

class UI():
	def __init__(self, surface):

		self.display_surface = surface
		self.health_bar = pygame.image.load('../clear_code/graphics/ui/health_bar.png')
		self.coin = pygame.image.load('../clear_code/graphics/ui/coin.png')
		self.coin_rect = self.coin.get_rect(topleft = (1000,100))
		self.health_bar_topleft =(1033,78)
		self.bar_height = 4
		self.bar_max_width = 152

	def show_health(self, current, full):
		self.display_surface.blit(self.health_bar,(1000,50))
		current_health_ratio = current / full
		current_bar_width = self.bar_max_width*current_health_ratio
		health_bar_rect = pygame.Rect(self.health_bar_topleft,(current_bar_width,self.bar_height))
		pygame.draw.rect(self.display_surface,'red',health_bar_rect)

	def show_coins(self,amount):
		self.display_surface.blit(self.coin, self.coin_rect)
		self.main_font = pygame.font.SysFont("Courier", 50)
		coin_amount_surf = self.main_font.render(str(amount),False,'black')
		coin_amount_rect = coin_amount_surf.get_rect(midleft = (self.coin_rect.right +4,self.coin_rect.centery))
		self.display_surface.blit(coin_amount_surf,coin_amount_rect)