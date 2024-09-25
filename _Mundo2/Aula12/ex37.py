while True:
    number = input('Digite um valor inteiro (Digite exit para sair) :')
    if number == 'exit':
        break
    try:
        number = int(number)
    except ValueError:
        print('Digite um valor inteiro válido.')
        continue # retorna ao inicio do loop
    while True:
        print('[1] Converter para BINÁRIO: ')
        print('[2] Converter para OCTAL: ')
        print('[3] Converter para HEXADECIMAL: ')
        option = int(input('Sua opção: '))
        if option not in [1,2,3]: # SE A OPÇÃO NÃO ESTÁ EM UM DESSES VALORES DA LISTA 
            print('Insira uma opção válida!')
        if option == 1:
            print(f'{number} convertido para BINARIO é igual a {bin(number)[2:]}') # USEI O FATIAMENTO PRA REMOVER O PREFIXO
        if option == 2:
            print(f'{number} convertido para OCTAL é igual a {oct(number).removeprefix('0o')}')
        if option == 3:
            print(f'{number} convertido para HEXADECIMAL é igual a {hex(number).removeprefix('0x')}')
        break

