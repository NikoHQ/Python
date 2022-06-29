#!/usr/bin/python
# -*- coding: utf-8 -*-
# Nombre del autor:Nicolás Alarcón

# import <biblioteca>
# from <biblioteca> import <modulo>
# import <biblioteca> as <alias>

#Declaración de funciones
def lcode(numero): 
    numero = int(input())
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for elem in letras:
        if numero.count(elem) == 0:
            return False
    return False
    


#Código principal
if __name__ == '__main__':
     #Instrucciones
    entrada = input ()
    resultado = lcode(entrada)
    print(resultado)
# No escribir codigo en este nivel