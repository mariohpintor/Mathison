from os import walk
import pygame

def import_folder(path):
	surface_list = []

	tupla = [i for i in walk(path) ]
	img_files = tupla[0][2]
	#quitamos el archivo .DS_Store
	img_files.pop(0)

	for image in img_files:
		full_path = path + '/' + image
		image_surf = pygame.image.load(full_path).convert_alpha()
		surface_list.append(image_surf)

	return surface_list					