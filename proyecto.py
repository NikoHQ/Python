#!/usr/bin/python
# -*- coding: utf-8 -*-
# Nombre del autores: Nicolás Robles, Lucas Pereira

#Declaración de funciones
def abrirArchivo():	#Abre archivo
	f = open("primos.txt","r")
	return f

def leerArchivo(proyect): #Funcion para leer y separar lineas e el archivo
	lista = [] 
	for linea in proyect: 
		lista.append(linea.rstrip('\n')) 
	proyect.close() 
	return lista

def guardarArchivo(resultado):	#Guarda resultados en el .txt
	f = open("resultado.txt","w")
	for l in resultado:
		f.write(str(l)+"\n")
	f.close()

def factores(numero, primos):	#saca los descomposicion de factores primos
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

def primo(num1): # Comporobar si primo o no
	for x in range (1,num1):
		if (num1%x==0 and x!=num1 and x!=1):
			return False
	return num1

def llena_lista_primos(nro): #crea una lista finita de numeros primos
	primos = []
	for i in range(2, nro):
		if primo(i) :
			primos.append(i)
	return primos

def modificarNumero(lista):
	i = 0 # cuando i valga 1 significa que es un nuevo proceso
	resultado = []
	listaDelProceso = [] 
	for x in lista: 
		listaDelProceso.append(x)
		i= i + 1
		if(i == 2):
			#Realizar lo que necesario
			potencias = []
			pivote = 0
			# 3 4 1 5, 1 2 3 4
			for a in listaDelProceso: 
				base = 0
				exponente = 0
				# 3 4 1 5
				for b in a:
					if b != ' ':
						if pivote == 0:						
							base = b
							pivote = 1
						else:
							exponente = b
							pivote = 0
							potencia = int(base)**int(exponente)
							potencias.append(potencia)
			potenciaspryct = []
			n = 0
			m = 0
			impar = len(potencias)%2
			for c in potencias:
				if m == 0:
					n = c
					m = 1
				else:
					nc = c * n
					m = 0
					potenciaspryct.append(nc)
			if(impar == 1):
				potenciaspryct.append(n)
			divisionespryct = []
			da = 0
			k = 0
			for d in potenciaspryct:
				if k == 0:
					da = d
					k = 1
				else:
					dada = da / d
					if(da%d!=0):
						resultado.append("NO DIVISIBLE")
					else:
						factorx = factores(int(dada), llena_lista_primos(int(dada)+2))
						factorx = sorted(factorx, reverse=True) # Ordenar lista de mayor a menor
						ga = []
						anterior = 0
						for g in factorx:
							if anterior != g:
								respfactor = factorx.count(g)
								anterior = g
								ga.append(g)
								ga.append(respfactor)
						strx = ""
						for fin in ga:
							strx = (strx + str(fin) + " ")

						resultado.append(strx)
					k = 0
					divisionespryct.append(dada)
			listaDelProceso = []
			i = 0
	guardarArchivo(resultado)

#Código principal
if __name__ == "__main__":
	#Instrucciones
	proyect = abrirArchivo()
	lista = leerArchivo(proyect)
	modificarNumero(lista)






