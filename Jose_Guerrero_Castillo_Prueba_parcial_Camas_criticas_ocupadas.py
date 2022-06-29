#!/usr/bin/python
#-*- coding: utf-8 -*-
#Autor: José Guerrero Castillo
#Sección: 2
#Asignatura: Programación
#Carrera: Ingeniería Civil Informática

#Biblioteca a utilizar
import matplotlib.pyplot as plt


#Aqui las funciones iniciales.
def lectura_camas(camasocupadas):                #Función con la que se leerá el archivo de texto
    lista=[]                            #Conjunto de datos que irán en la gráfica del eje X 
    X = []                             #Variable que guardara las variables en el eje X
    lista_Y = []                       #Conjunto de datos que irán en el eje y
    Y = []                             #Lo mismo que arriba en el eje Y
    archivo=open(camasocupadas)                 #Abrir archivo
    for rail in archivo:
        rail=rail.rstrip('\n')      #Separar lineas del archivo por cada iteración.
        rail = rail.split(',')     #Eliminar los espacios con (,)
    
    print(rail)
    print(archivo)


    for elem in lista:      #Guardar estos valores en X
        X.append(elem)
        lista_Y.append(elem[-1])

    for elem in lista_Y:
        elem=int(elem)             #Transformar datos de lista a enteros
        Y.append(elem)                     #Se añaden estos al final de la variable
    return X,Y                            #Retornar estos datos a las variables

def Graficar(X,Y):                  #Función en la que se grafica.
    plt.title('Fecha X Cantidad de Camas Críticas Ocupadas')   #Título de la gráfica
    plt.plot(X,Y)                                             #Variables a mostrar en la gráfica
    plt.xticks(rotation=85)                                 #Rota las letras para que no se sobrepongan en la gráfica.
    plt.show()                                               #Se muestra la gráfica


def Detalle(X,Y):                  #Muestra los lugares o comunas
    a = ''
    while len(X)>0:
        if len(X) ==1:
            a+'En la fecha'+''+str(X[0])+''+'Están ocupadas'+''+str(Y[0]+'Camas críticas') #Indica por separado la comuna y la cantidad de datos en la terminal
        else:
            a=a+'En la fecha'+str(X[0])+' '+'Están ocupadas'+''+str(Y[0]+'\n')          #Indica por separado la comuna y la cantidad de datos en la terminal
        X.pop(0)
        Y.pop(0)
    print(a)



if __name__ =="__main__":              #Finalmente, el código principal.
    X,Y = lectura_camas('ventiladores_ocupados.csv')              #Abrimos el archivo archivo csv para lectura(r).
    Graficar(X,Y)                       #Graficamos los datos del archivo
    Detalle(X,Y)                       #Finalmente, coloca en detalle en la terminal de datos la fecha y la cantidad de ventiladores.