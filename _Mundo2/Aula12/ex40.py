nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
media = (nota1+nota2)/2
print(f'A media do aluno é {media} com as notas {nota1:.1f} e {nota2:.1f}')
if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÂO')
elif media < 5:
    print('O aluno está REPROVADO')
else:
    print('Aluno APROVADO')