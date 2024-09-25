dias = int(input('Quantos dias você vai alugar? : '))
km = float(input('Quantos km rodados? : '))
total = (60*dias) + (0.15*km)
print(f'O total a pagar é R${total:.2f}')
