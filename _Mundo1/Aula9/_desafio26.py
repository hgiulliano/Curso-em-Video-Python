phrase = input('Digite uma frase: ').lower().strip()
print(f'A letra \'a\' aparece {phrase.count('a')} vezes')
print(f'A letra \'a\' apareceu pela primeira vez na posição {phrase.find('a')+1}')#+1 pra adequar ao python que começa em 0
print(f'A letra \'a\' apareceu pela última vez na posição {phrase.rfind('a')+1}')#+1 pra adequar ao python que começa em 0
#rfind olha da direita pra esquerda

