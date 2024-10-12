pesos = []
maior = 0 
menor = None
for indice in range (0,5):
    pesos.append(float(input(f'Digite o peso da {indice+1} pessoa: ')))
    print(pesos)
    if pesos[indice] > maior:
        maior = pesos[indice]
    if menor is None or pesos[indice] < menor: #NONE não define valor, então qualquer valor seria menor que none, facilitando a logica
        menor = pesos[indice]
print(f'O maior peso registrado foi {maior:.2f}')
print(f'O menor peso registrado foi {menor:.2f}')