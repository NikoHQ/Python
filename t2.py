#Funcion que realiza toda la operacion
def primolandia(narchivo):
	listaArchivo = []
	#guardamos todas las lineas del archivo en una lista
	with open(narchivo) as archivo:
		for linea in archivo:
			lineaM = linea.rstrip('\n')
			listaArchivo.append(lineaM)
	archivo.close()

	contador = 1
	anterior = ""
	listaPotencias = []
	salida = open("resultado.txt", "w")
	for posicion in listaArchivo:
		if(contador == 2):
			contador = 1
			#Obtenemos potencias
			potencia1 = 1
			potencia2 = 1
			base = 0 
			expotente = 0
			i = 0
			while(i < len(anterior)):
				if(anterior[i] != ' '):
					base = int(anterior[i])
					if((i+2) < len(anterior)):
						expotente = int(anterior[i+2])
						potencia1 = potencia1 * (base**expotente)
						if((i+3)<len(anterior)):
							i = i + 3
				i = i + 1
			j = 0
			base1 = 0 
			expotente1 = 0
			while(j < len(posicion)):
				if(posicion[j] != ' '):
					base1 = int(posicion[j])
					if((j+2) < len(posicion)):
						expotente1 = int(posicion[j+2])
						potencia2 = potencia2 * (base1**expotente1)
						if((j+3)<len(posicion)):
							j = j + 3
				j = j + 1
			#Ahora dividimos nuestras potencias
			if(potencia1%potencia2 == 0):
				numero = int(potencia1/potencia2)
				factor = factores(numero, llena_lista_primos(232))
				factor = bubbleSort(factor)
				
				#Transformamos a primolandia
				usados = []
				primol = []
				encontrado = 0
				for num in factor:
					for rep in usados:
						if(num == rep):
							encontrado = 1
							break
					if(encontrado == 0):
						primol.append(num)
						primol.append(factor.count(num))
						encontrado = 0
				for t in primol:

					salida.write(str(t) + " ")
				salida.write('\n')
			else:
				salida.write("NO DIVISIBLE\n")
		else:
			anterior = posicion
			contador = contador + 1
	salida.close()
#Ordenar lista
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] < arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
#Nos sirve para saber si un numero es primo
def primo(num1):
	for x in range (1,num1):
		if (num1%x==0 and x!=num1 and x!=1):
			return False
	return num1
#Nos permite obtener una lista de numeros primos dentro de un rango
def llena_lista_primos(nro):
	primos = []
	for i in range(2, nro):
		if primo(i) :
			primos.append(i)
	return primos
#Nos permite sacar los factores de un numero primo
def factores(numero, primos):
	divisibles=[]
	while numero > 1:
		if primo(numero):
			divisibles.append(numero)
			break
		for i in range(len(primos)):
			if numero % primos[i] == 0:
				divisibles.append(primos[i])
				numero = numero // primos[i]
				break
	return divisibles
if __name__ == "__main__":
	primolandia("primos.txt")
