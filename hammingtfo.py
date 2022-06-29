import numpy as np
bits = np.random.randint(0,2,9)
from functools import reduce
import operator as op

#bits= [1,1,0,1,0,1,0,1,1]
paridad= []


enumerate(bits)
list(enumerate(bits))
print([i for i, bit in enumerate(bits) if bit])
print(bits)
from functools import reduce
import operator as op
a=reduce(op.xor,[i for i, bit in enumerate(bits) if bit])
print(a)
bits[a] = 0
print(bits)
b=reduce(op.xor,[i for i, bit in enumerate(bits) if bit])
print(b)

