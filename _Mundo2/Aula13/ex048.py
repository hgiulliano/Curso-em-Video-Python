var = 0
b = 0
for c in range (1 , 501, 2): # ele pediu nesse intervalo, entretanto, seria interessante começar pelo 3 e pular de 6 em 6 pra otimizar nosso codigo
    if c%3 == 0:
        b+=1
        var+=c
print(b)
print(var)