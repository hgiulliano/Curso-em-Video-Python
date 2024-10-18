b = []
soma = 0
cont = 0
for i in range(0, 6):
    a = int(input("Digite um número inteiro: "))
    b.append(a)
    if b[i] % 2 == 0:  # pode substituir b[i] por a
        soma += b[i]  # pode substituir b[i] por a
        cont += 1
print(f"Você adicionou {cont} pares e a soma deu: {soma}")
