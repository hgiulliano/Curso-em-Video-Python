import math
num = float(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'a raiz de {num} é igual {math.ceil(raiz)}') # posso executar comandos dentro das chaves

##OU

from math import sqrt,floor
num = float(input('Digite um número: '))
raiz = sqrt(num)
print(f'a raiz de {num} é igual {floor(raiz)}') # posso executar comandos dentro das chaves