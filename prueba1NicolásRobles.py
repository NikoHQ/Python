#!/usr/bin/python
# -*- coding: utf-8 -*-
# Nombre del autor:Nicolás Robles Alarcón

# import <biblioteca> as <alias>
import matplotlib.pyplot as plt

#Declaración de funciones
def datos(casos_por_region):
    lista = []
    X = []
    lista_Y = []
    Y = []
    ar = open(casos_por_region)
    for fila in ar:
        fila = fila.rstrip('\n')
        lis = fila.split(',')
        if lis[0] == 'Maule':
            lista.append(lis)
    for elem in lista:
        X.append(elem[2])
        lista_Y.append(elem[-1])
    for elem in lista_Y:
        elem = int(float(elem))
        Y.append(elem)
    return X,Y

def grafico(X,Y):
    plt.title(' Casos totales del país confirmados de covid-19 en comunas de la Region del maule ')
    plt.plot(X,Y)
    plt.xticks(rotation=77)
    plt.show()
    
#Código principal
if __name__ == "__main__":
    X,Y = datos("casos_por_region.csv")
    print(Y)
    "grafico(X,Y)"