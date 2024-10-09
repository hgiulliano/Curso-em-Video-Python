from time import sleep
max = int(input('DEFINA O TEMPORIZADOR DA SUA BOMBA!!! : '))
contagem = max+1
for i in range(max):
    contagem-=1
    sleep(1)
    print(contagem)
print('BOOOOMMMMM!!!!!')