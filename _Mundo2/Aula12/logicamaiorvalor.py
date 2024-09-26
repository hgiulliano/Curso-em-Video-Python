#logica de análise de maior valor
a = 14343
b = 2545435
c = 3545354643
maior = 0
if a > b:
    maior = a
if b > a:
    maior = b
if maior < c:
    maior = c
print(maior)