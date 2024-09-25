frase = 'Curso em Vídeo Python'
frase = frase.split()#divisão considerando os espaços, como se fossem strings diferentes, nova indexação, dentro de outra lista, separadas
print('-'.join(frase))#juntou as listas que foram separadas no split, colocando '-' nas divisões

dividido = frase.split()
print(dividido [2] [3])
#vai me mostrar a segunda string q foi dividida pelo split e a letra 4 , pq começa do 0