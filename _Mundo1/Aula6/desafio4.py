n = input('Digite algo: ')
print(f'O tipo da variável que você me ofereceu é {type(n)}')
print(f'{n} é composto somente por digitos ? {n.isdigit()}')
print(f'{n} é decimal? {n.isdecimal()}')
print(f'{n} é composto somente por letras? {n.isalpha()}')
print(f'{n} é composto alfa numérico?? {n.isalnum()}')
print(f'{n} é escrito somente por letras maiúsculas? {n.isupper()}')
print(f'{n} é escrito somente por letras minúsculas? {n.islower()}')