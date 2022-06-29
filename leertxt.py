'''lista = ["1 2 3 4"]
for i in lista:
    a = i.split(" ")
print(a)'''

def lector(archivoEntrada):
    lineas = []
    archivo= open(archivoEntrada)
    for linea in archivo.readlines():
        a = linea.rstrip('\n')
        lineas.append(a)
    archivo.close()
    return lineas

def elevarNum(lineas):
    for i in lineas:
        listaSeparada = i.split(" ")
        multiplicar = []
        try:
            n = 0
            u = 1
            for i in range(len(listaSeparada)):
            #print(listaSeparada[n],listaSeparada[u])
            #elevar = float(listaSeparada[n])**float(listaSeparada[u])
                elevar = int(listaSeparada[n])**int(listaSeparada[u])
                print(elevar)
                n = n+2
                u = u+2
                multiplicar.append(elevar)
        except IndexError:
            pass
        product = 1
        for i in multiplicar:
            product *= i
            print(product)
        

if __name__ == '__main__':
    print('toyvolaoalo')
    lineas = lector('primos.txt')
    elevarNum(lineas)