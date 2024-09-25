value = float(input('Qual o valor da casa que você quer comprar?: '))
salary = float(input('Qual o valor da casa que você quer comprar?: '))
years = int(input('Qual o valor da casa que você quer comprar?: '))

#prestação = valor/meses
installment = (value/(12*years))

if installment > (0.3*salary):
    print(f'{installment:.2f} - Emprestimo negado')
elif installment <= (0.3*salary):
    print(f'{installment:.2f} - Emprestimo concedido!')