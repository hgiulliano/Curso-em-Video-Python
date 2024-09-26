while True:
    print(f'=' * 10 + ' HENRYO STORE ' + '=' * 10)
    try:
        value = float(input('Preço das compras: R$'))
    except ValueError:
        print('Forneça um valor numérico. ')
        continue # returns to the last input
    print('FORMAS DE PAGAMENTO')
    print(' [1] à vista dinheiro/cheque')
    print(' [2] à vista cartão')
    print(' [3] 2x no cartão')
    print(' [4] 3x ou mais no cartão')
    option = int(input('Qual é a opção? : '))
    if option == 1:
        discount = 0.1*value
        newvalue = value-discount
        print(f'Sua compra de R${value:.2f} vai custar R${newvalue:.2f} no final. (10% de desconto)')
    elif option == 2:
        discount = 0.05*value
        newvalue = value-discount
        print(f'Sua compra de R${value:.2f} vai custar R${newvalue:.2f} no final. (5$ de desconto)')
    elif option == 3:
        print(f'Sua compra no cartão sai no valor formal : R${value:.2f}, sem juros.')
    elif option == 4:
        rates = value*0.2
        installments = int(input('Quantas parcelas? :'))
        newvalue = value+rates
        iv = (newvalue)/installments #installments value
        print(f'Sua compra será parcelada em {installments}x de R${iv:.2f} COM JUROS')
        print(f'Sua compra de {value:.2f} vai custar R${newvalue:.2f} no final.')
    else:
        print('Entrada invalida, tente novamente.')
    break
    
