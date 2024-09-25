n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print(f'A soma vale {n1+n2}, \n o produto é {n1*n2} \n e a divisão é {n1/n2:.3f}',end=' ')
#,end='' te permite além de retirar a quebra de linha padrão da função print, modificar o que você quer colocar nesse espaço
print(f'A divisão inteira é {n1//n2} e a exponenciação é {n1**n2}')