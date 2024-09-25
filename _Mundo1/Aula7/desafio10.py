real = float(input('Quanto dinheiro você tem na sua carteira em reais? : '))
dolar = real/3.27
if dolar >= 1: 
    print(f'O valor que você tem é {dolar:.2f} doláres')
else:
    print(f'O valor que você tem é {dolar:.2f} centavos de doláres')