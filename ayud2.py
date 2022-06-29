



def lector(archivoEntrada):
	lineas= [] 
	archivo = open(archivoEntrada)
	for linea in archivo.readlines():
		a = linea.rstrip("\n")
		lineas.append(a)
	archivo.close()
	return lineas

def elevarNumero(lineas):
	dividendo = []
	for i in lineas:
		listaSeparada = i.split(" ")
		multiplicar = []
		try:
			n = 0
			u = 1
			for i in range(len(listaSeparada)):
				elevar = int(listaSeparada[n])**int(listaSeparada[u])
				n = n+2
				u = u+2
				multiplicar.append(elevar)
		except IndexError:
			pass

		contador  = 0
		product = 1

		for i in multiplicar:
			contador = contador + 1
			product *=i
			aux = (len(multiplicar))
			if len(multiplicar) == aux and contador == aux:
				dividendo.append(product)

		print(dividendo)
	return dividendo

def divisionF(dividendo):
	try:
		n = 0
		u = 1
		for i in range(len(dividendo)):
			dividir = int(dividendo[n])/int(dividendo[u])
			print(dividir)
			n = n+2
			u = u+2
	except IndexError:
		pass

if __name__ == '__main__':

	lineas  = lector("primos.txt")
	dividendo = elevarNumero(lineas)
	divisionF(dividendo)


#1 leer archivos txt
#2 linea por linea generar el numero 
	#1 funcion para que se eleve ok
		#multiplicar numeros ok
		#dividir por la segunda linea del par 
		#saber que numero eleva y cual es la base

	#2 funcion para que se multiplique
#3 segunda linea divida a la primera
 
"""
2 1
3 1 2 2
5 1 2 1"""