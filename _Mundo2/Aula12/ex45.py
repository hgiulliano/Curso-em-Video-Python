from random import randint
from time import sleep
print('='*20)
print('Suas opções: ')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
print('='*20)
option = int(input('Qual é a sua jogada? '))
print('='*25)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('='*25)
pcoption = randint(1,3)

if option == 1 :
    answer = 'PEDRA'
elif option == 2 :
    answer = 'PAPEL'
elif option == 3 :
    answer = 'TESOURA'

if pcoption == 1 :
    pcanswer = 'PEDRA'
elif pcoption == 2 :
    pcanswer = 'PAPEL'
elif pcoption == 3 :
    pcanswer = 'TESOURA'
print('-='*11)
print(f'Computador jogou {pcanswer}')
print(f'Jogador jogou {answer}')
print('-='*11)



