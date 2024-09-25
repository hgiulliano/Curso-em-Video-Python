frase = 'Curso em Vídeo Python'
print(len(frase))#comprimento da frase
print(frase.count('o'))#conta quantas vezes aparece a letra 'o' na variável
print(frase.count('o',0,13))#conta quantas vezes aparece a letra 'o' entre o caracter 0 e o 13
print(frase.find('deo'))#diz onde começou esse pedaço da frase
print(frase.find('Android'))#se colocar uma string q n existe ele coloca -1, dizendo q n foi encontrado
print(frase.rfind('a')+1)#rfind olha da direita pra esquerda
print('Curso' in frase)#Confere se existe a string 'Curso' na sua variável -> True | False