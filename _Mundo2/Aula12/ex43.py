weight = float(input('Peso (Kg): '))
altura = float(input('Altura (m): '))
IMC = weight/(altura**2)
if IMC < 18.5:
    print('Abaixo do peso')
elif 18.5 <= IMC < 25:
    print('Peso Ideal')
elif 25 <= IMC < 30:
    print('Sobrepeso')
elif 30 <= IMC < 40:
    print('Obesidade')
elif IMC >= 40:
    print('Obesidade Mórbida')
print(f'Seu IMC é {IMC:.1f}')