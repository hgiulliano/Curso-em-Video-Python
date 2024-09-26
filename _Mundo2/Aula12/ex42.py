seg1 = float(input('Segmento 1: '))
seg2 = float(input('Segmento 2: '))
seg3 = float(input('Segmento 3: '))
tipo = ''

if seg1 == seg2 == seg3:
    tipo = 'Equilátero'
elif seg1 != seg2 != seg3: #pode comparar 3 elementos dessa forma.
    tipo = 'Escaleno'
else:
    tipo = 'Isósceles'

if seg1 + seg2 > seg3 and seg2 +seg3 > seg1 and seg3 + seg1 > seg2:
    print(f'Os segmentos acima podem formar um triângulo {tipo}')
else:
    print('Esses segmentos não formam um triangulo')