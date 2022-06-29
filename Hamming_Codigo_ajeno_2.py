#Codigo de ejemplo 2

#Funcion para determinar la redundancia de los bits en el codigo.
def calc_Redundancia_bits(m): 
    for i in range(m): 
        if(2**i >= m + i + 1): 
            #print(m)
            return i 

#Funcion para comprobar la posicion de los bits de redundancia 
def posRedundantBits(data, r): 
    const = 0
    const_2 = 1
    codigo = len(data)
    #print(codigo)
    res = '' 
        
    for i in range(1, codigo + r+1): 
        if(i == 2**const): 
            res = res + '0'
            const += 1
            #print(const)
        else: 
            res = res + data[-1 * const_2] 
            const_2 += 1
            #print(const_2)
  
    
    
    return res[::-1] 

#Función para calcular la paridad de los bits con el codigo colocado ingresado.
def calc_Paridad_bits(array, r): 
    n = len(array) 
    
    for i in range(r): 
        valor = 0
        for j in range(1, n + 1):           
            if(j &(2**i) == (2**i)): 
                valor = valor ^ int(array[-1 * j]) 

        array = array[:n-(2**i)] + str(valor) + array[n-(2**i)+1:] 
    return array 
  
#Funcion para detectar error el el codigo
def detecError(array, nr): 
    n = len(array) 
    res = 0
  
    
    for i in range(nr): 
        val = 0
        for j in range(1, n + 1): 
            if(j &(2**i) == (2**i)): 
                val = val ^ int(array[-1 * j]) 
  
        res = res + val*(10**i) 
  
    
    return int(str(res), 2) 



#Parte principal del codigo, transformar en main. 
#Código de entrada
data = '100101011'
  
m = len(data) 
r = calc_Redundancia_bits(m) 
  
array = posRedundantBits(data, r) 
  
array = calc_Paridad_bits(array, r) 
  
print("Los datos transferidos son:" + array)   
  
#Codigo de salida o codigo que nos fue enviado. Necesario tenerlo para poder poner en marcha el código. Realizar el algoritmo de hamming desde afuera.
array ='1111001101011'

print("Los datos de error son:" + array) 
correcion = detecError(array, r) 
print("La posicion del error es:" + str(correcion)) 
