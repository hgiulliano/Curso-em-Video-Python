from os import get_terminal_size
from random import randint
from time import sleep
playagain = 'y'
placarpc = 0
placarjog = 0
size = get_terminal_size().lines #ele te da largura e altura, com o .lines, vc pega so a quantidade de
while playagain in ['Y','y']:
    try:
        print('='*20)
        print('Suas opções: ')
        print('[ 1 ] PEDRA')
        print('[ 2 ] PAPEL')
        print('[ 3 ] TESOURA')
        print('='*20)
        while True:
            option = int(input('Qual é a sua jogada? '))
            if option not in [1,2,3] :
                print('Entrada inválida, escolha uma das opções dadas.')
                continue
            else:
                break
    except ValueError:
        print('Entrada inválida, escolha uma das opções dadas.')
        continue
    
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

    if pcoption == 1: #pc jogou PEDRA

        if option == 1:
            print('EMPATE!!')
        elif option == 2:
            print('JOGADOR VENCE')
            placarjog+=1
        elif option == 3:
            print('COMPUTADOR VENCE')
            placarpc+=1


    elif pcoption == 2: #pc jogou PAPEL

        if option == 1:
            print('COMPUTADOR VENCE')
            placarpc+=1
        elif option == 2:
            print('EMPATE')
        elif option == 3:
            print('JOGADOR VENCE')
            placarjog+=1


    elif pcoption == 3: #pc jogou TESOURA

        if option == 1:
            print('JOGADOR GANHA')
            placarjog+=1
        elif option == 2:
            print('COMPUTADOR GANHA')
            placarpc+=1
        elif option == 3:
            print('EMPATE')
    print('='*7 + 'PLACAR' + '='*7)
    print(F'JOGADOR : {placarjog} Pontos')
    print(F'COMPUTADOR : {placarpc} Pontos')
    print('='*20)

    while True:

        playagain = str(input('Deseja jogar novamente? (Y/N) : '))

        if playagain in ['y','Y']:
            print('\n'*size)
            break

        if playagain in ['n','N']:
            print('\n'*size)
            print('Obrigado por jogar! :) ')
            break

        if playagain not in ['y','Y','n','N']:
            print('Entrada inválida, favor escolher entre Y ou N!!')
            continue
    if playagain in ['n','N']:
        if placarpc > placarjog:
            print(f'PLACAR FINAL: {placarpc}x{placarjog} --> COMPUTADOR GANHOU')
        elif placarjog > placarpc:
            print(f'PLACAR FINAL: {placarjog}x{placarpc} --> JOGADOR GANHOU')
        break
input('PRESSIONE QUALQUER TECLA PARA FINALIZAR O PROGRAMA!!')