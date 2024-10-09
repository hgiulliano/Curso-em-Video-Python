b = []
soma = 0
for i in range(0,6):
    a = int(input('Digite um número inteiro: '))
    b.append(a)
    if b[i]%2 == 0: #pode substituir b[i] por a
        soma+=b[i] #pode substituir b[i] por a
print(soma)
