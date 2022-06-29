#!/usr/bin/python
# -*- coding: utf-8 -*-
# Nombre del autor:Nicolás Robles Alarcón

# import <biblioteca> as <alias>
from os import link
import pandas as pd


#Declaración de funciones

def read(input):
    df = pd.read_csv(input)
    df.head()



    
#Código principal
if __name__ == "__main__":
    entrada = input("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto4/2021-09-28-CasosConfirmados-totalRegional.csv")
    salida = read(entrada)

