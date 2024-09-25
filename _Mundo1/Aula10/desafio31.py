distance = float(input('Digite a distância da sua viagem: '))
if distance <= 200:
    value = distance*0.5
    print(f'O valor da sua viagem é {value:.2f}, com a taxa de 0,50 cents por km')
else:
    value = distance*0.45
    print(f'O valor da sua viagem é {value:.2f} e a taxa foi de 0,45 cents')     