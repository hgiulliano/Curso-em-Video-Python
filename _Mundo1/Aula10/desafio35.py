a = float(input('Digite um valor: '))
b = float(input('Digite um valor: '))
c = float(input('Digite um valor: '))
if a+b > c and a+c >b and b+c > a:
    print(f'Você consegue formar um triângulo com esses valores!')
else:
    print('Você não consegue formar um triângulo com esses valores :(')