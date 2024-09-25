from random import shuffle
A = str(input('Digite o nome do aluno A: '))
B = str(input('Digite o nome do aluno B: '))
C = str(input('Digite o nome do aluno C: '))
D = str(input('Digite o nome do aluno D: '))
ordem = [A,B,C,D]
shuffle(ordem)
print(f'A ordem escolhida foi: {ordem}')