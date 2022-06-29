
from functools import reduce
import operator as op

#var
codig1 = [1,1,0,1,0,1,0,1,1]
sim_error = [1,1,0,1,0,1,0,1,0]
#def
#coding
def parity_bit(bits):
    cantidad_1 = bits.count('1')
    if cantidad_1%2 == 0:
        return 0 
    else:
        return 1


#decode:
def comprobar_paridad():
    enumerate(codig1)
    list(enumerate(codig1)) #organiza y cuenta carácteres
    print([i for i, bit in enumerate(codig1) if bit]) #devuelve resultado solo cuando el valor corresponda a un 1
    print(codig1)
    return codig1

   
def opxor():
    position=reduce(op.xor,[i for i, bit in enumerate(codig1) if bit])
    print(position) 
    return position



def main():
    
    decodificar = comprobar_paridad()
    print(decodificar)
    posicion = opxor(decodificar)
    print(posicion)
    return 

#code
if __name__ == "__main__":
    main()