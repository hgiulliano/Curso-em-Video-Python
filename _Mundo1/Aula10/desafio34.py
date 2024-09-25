budget = float(input('Qual seu salário?: '))
if budget > 1250 :
    newbudget = budget + (budget*0.1)
    print(f'Seu salário era {budget} e com o aumento de 10% virou {newbudget}')
else:
     newbudget = budget + (budget*0.15)
     print(f'Seu salário era {budget} e com o aumento de 15% virou {newbudget}')