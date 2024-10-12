red = '\033[91m'
yellow = '\033[93m' 
reset = '\033[0m'
cont = 0
number = int(input('Digite seu número: '))
for i in range(1,number+1):
    prime = number/i
    if number%i != 0 :
        print(f'{red}{prime:.2f}{reset}', end= ' ')
    else:
        print(f'{yellow}{prime}{reset} ', end= ' ')
        cont+=1
if cont == 2:
    print('\nSeu número é primo')
else:
    print(f'\nSeu número não é primo e tem {cont} divisores exatos')