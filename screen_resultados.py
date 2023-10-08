from overworld import Overworld

class Pantalla_resultados:
	def __init__(self,surface,current_level):
		self.display_surface = surface
		self.current_level = current_level

	def pantalla_resultados(self):
		tiempo = time.time()-self.tiempo
		print('Tiempo: ',tiempo)
		print('Buenas: ',self.contador_palomas)
		print('Errores: ',self.contador_ecuaciones-self.contador_palomas)
		print('Puntaje: ',round(tiempo,2)*100-self.contador_ecuaciones*100+self.contador_palomas*10)
