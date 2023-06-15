import pygame, sys
from settings import *

class Game:
	def__init__(self):
		self.overworld = Overworld()
	def run(self):
		self.overworld.run()	
