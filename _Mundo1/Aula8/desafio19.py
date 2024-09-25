from random import choice
a = str(input('digite o nome do estudante A: '))
b = str(input('digite o nome do estudante B: '))
c = str(input('digite o nome do estudante C: '))
d = str(input('digite o nome do estudante D: '))
nomes = [a,b,c,d]
#criar listas  pode ser uma forma interessante de organizar as coisas
print(f'O estudante escolhido foi {choice(nomes)}')