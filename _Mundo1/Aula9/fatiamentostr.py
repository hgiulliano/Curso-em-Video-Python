#FATIAMENTO DE STRING

frase = 'abcdefghijklmnopqrstuvwxyz'
print(frase[9])#printa só o 9 caracter da string
print(frase[9:13])#printa do  9 ate o 12 |ele inclui o 9, mas remove o 13| caracter da string
print(frase[9:26])#como a gente tem 25|pro python a contagem começa em 0 | letras, ele aceita 26, pq é como se excluisse o nada
print(frase[9:26:2])#ele pula de 2 em 2
print(frase[:5])#antes dos dois pontos é onde começa, dps termina, se não tem nada antes, ele sai do inicio e termina no caracter q vc mandou
print(frase[15:])#começa de onde vc pede e vai até o final, pq vc n especificou
print(frase[9::3])#ele começa do 9 e vai até o fim pulando de 3 em 3

#ANÁLISE

len(frase)

#QUANDO É UM ARRAY, É DIFERENTE

frase = 'Santo Andre'
frase = frase.split()
print(frase)
print(frase[0])
print(frase[1])

#ELE OLHA PELO INDICE DO ARRAY
