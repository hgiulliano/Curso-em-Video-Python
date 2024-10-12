nome, idade, sexo, = [], [], []
media, holder, fcont = 0, 0, 0
hname = ''
for i in range (1,5):
    print('-'*15,f'{i}ª Pessoa','-'*15)
    nome.append(str(input(f'Digite o nome da {i}ª pessoa :')).strip())
    idade.append(int(input(f'Digite a idade da {i}ª pessoa :')))
    media+=idade[i-1] 
    sexo.append(str(input(f'Digite o sexo da {i}ª pessoa [ M | F ] : ')).strip().upper())
    if sexo[i-1] == 'M':
        if idade[i-1] > holder:
            holder = idade[i-1]
            hname = nome[i-1]
    if sexo[i-1] == 'F':
        if idade[i-1] < 20:
            fcont+=1
media = media/i
print('='*50)
print(f'A média da idade dos grupos é de {media:.2f}')
print(f'O homem mais velho tem {holder} anos de idade e seu nome é {hname}')
if fcont > 0:
    print(f'Ao todo são {fcont} mulheres com menos de 20 anos')
else:
    print('Não tem nenhuma mulher com menos de 20 anos')
print('='*50)
    
    