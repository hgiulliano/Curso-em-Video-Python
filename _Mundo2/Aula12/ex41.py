from datetime import datetime
birthyear = int(input('Ano de nasicmento: '))
atual = datetime.now().year
idade = atual-birthyear
if idade <= 9:
    print('Mirim')
elif idade <=14:
    print('Infantil')
elif idade <=19:
    print('Junior')
elif idade <=25:
    print('Senior')
else:
    print('Master')