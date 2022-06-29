#Autores: Bernardo Carrasco 21207423-3. Passcual Acevedo 20844139-6




#ésta será la función principal que realiza la operación
def primo_pe(narchivo):
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
			#aquí conseguimos las potencias
			pote1 = 1
			pote2 = 1
			base = 0 
			expo = 0
			i = 0			
			while(i < len(anterior)):
				if(anterior[i] != ' '):
					base = int(anterior[i])
					if((i+2) < len(anterior)):
						expo = int(anterior[i+2])
						pote1 = pote1 * (base**expo)
						if((i+3)<len(anterior)):
							i = i + 3
				i = i + 1
			j = 0
			base1_o = 0 
			expo1 = 0
			while(j < len(posicion)):
				if(posicion[j] != ' '):
					base1_o = int(posicion[j])
					if((j+2) < len(posicion)):
						expo1 = int(posicion[j+2])
						pote2 = pote2 * (base1_o**expo1)
						if((j+3)<len(posicion)):
							j = j + 3
				j = j + 1
			#dadas las potencias aqui procederemos a dividirlas
			if(pote1%pote2 == 0):
				numero = int(pote1/pote2)
				fact = factores(numero, llena_lista_primos(232))
				fact = bubbleSort(fact)
			
			    #tranformacion de primos_pe
				usados = []
				primol = []
				encontrado = 0
				for num in fact:
					for rep in usados:
						if(num == rep):
							encontrado = 1
							break
					if(encontrado == 0):
						primol.append(num)
						primol.append(fact.count(num))
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
#aqui se organiza la lista
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] < arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
#con esto nos dara a saber si el numero dado es primo o no
def primo(num1):
	for x in range (1,num1):
		if (num1%x==0 and x!=num1 and x!=1):
			return False
	return num1
#nos permitirá obtener dentro de un intervalo numeros primos
def llena_lista_primos(nro):
	primos = []
	for i in range(2, nro):
		if primo(i) :
		   primos.append(i)
	return primos	
#esto nos dara o nos permitira obtener los factores de un numero primo
def factores(numero, primos):
	severable=[]
	while numero > 1:
		if primo(numero):
			severable.append(numero)
			break
		for i in range(len(primos)):
			if numero % primos[i] == 0:
				severable.append(primos[i])
				numero = numero // primos[i]
				break
	return severable
if __name__ == "__main__":
	primo_pe("primos.txt")
