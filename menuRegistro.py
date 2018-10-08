from registro import Registro
from datetime import datetime, date

class MenuRegistro:
	def __init__(self,conexion,cursor):
		self.registro = Registro(conexion,cursor)

		while True:
			print("1) Agregar Registro")
			print("2) Mostrar Registro")
			print("0) Salir")
			op = input()

			if op == '1':
				self.agregar()
			elif op == '2':
				self.buscar()
			elif op == '0':
				break


	def agregar(self):
		fecha = datetime.now().date()
		ph = input("PH: ")
		luz = input("luz: ")
		humedad = input("Humedad: ")
		co2 = input("Co2: ")
		id_planta = input("Id Planta: ")

		self.registro.agregar(fecha,ph,luz,humedad,co2,id_planta)

	def buscar(self):
		id_planta = input("Id Planta: ")
		resultados = self.registro.buscar(id_planta)

		for p in resultados:
			print("{0:2} {1:10} {2:10} {3:10} {4:10} {5:10}".format(p[0],str(p[1]),p[2],p[3],p[4],p[5]))






