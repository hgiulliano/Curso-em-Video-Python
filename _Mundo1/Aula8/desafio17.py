# DESAFIO 17
from math import sqrt
co = float(input('Digite o seu cateto oposto: '))
ca = float(input('Digite o seu cateto adjacente: '))
#decidi resolver pela teoria do meu mano pitongas
#pow(base, exp): Calcula base elevado à exp
h2 = pow(co,2) + pow(ca,2)
h = sqrt(h2)
print(f'Sua hipotenusa vale {h}')