from datetime import datetime
birthyear = int(input('Ano de nascimento: '))
actualyear = datetime.now().year
age = actualyear - birthyear
falta = 18-age
if age < 18:
    print(f'Quem nasceu em {birthyear} tem {age} anos em {actualyear}.')
    print(f'Ainda faltam {falta} anos para o alistamento')
    print(f'Seu alistamento será em {actualyear+falta}')
if age > 18:
    print(f'Quem nasceu em {birthyear} tem {age} anos em {actualyear}.')
    print(f'Voce deveria ter se alistado há {age-18}')
    print(f'Seu alistamento foi em {actualyear+falta}')
else:
    print(f'Quem naceu em {birthyear} tem {age} anos em {actualyear}')
    print('Você tem que se alistar IMEDIATAMENTE!')