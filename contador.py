import collections
from collections import Counter

numeros = [7,5,9,2,2,3,9,7,0,1]


conteos = Counter(numeros)
Valor_Unicos= len(conteos)

for i in conteos:
    if i > Valor_Unicos:
        print('a',i) 
    else:
        print('no')




