#DESSE JEITO, COM VARIOS IF'S A GENTE CONSEGUE MONTAR AS CONDICIONAIS SEM PRECISAR DE UM SAIDA TIPO O ELSE
number = []
number.append(int(input('Digite um numero: ')))
number.append(int(input('Digite um numero: ')))
number.append(int(input('Digite um numero: ')))

#IF'S PARA MENOR:
if number[0] < number[1] and number [0] < number[2]:
    menor = number[0]
if number[1] < number[0] and number[1] < number[2]:
    menor = number[1]
if number[2] < number[0] and number[2] < number[1]:
    menor = number[2]
    
#IF'S PARA MAIOR:
if number[0] > number[1] and number [0] > number[2]:
    maior = number[0]
if number[1] > number[0] and number [1] > number[2]:
    maior = number[1]
if number[2] > number[0] and number [2] > number[1]:
    maior = number[2]

#PRINTA O MENOR E O MAIOR NÚMERO DEFINIDO PELOS IF'S ANTERIORES: 
print(f'O seu maior numero é {maior} e o menor é {menor}!!')

#opção mais simples e compacta: 
number.sort()
print(f'Seu maior número é {number[2]} e o menor é {number[0]}')


    