name = input('Qual seu nome completo?: ').strip()
name = name.split()
print(len(name))
print(f'o seu primeiro nome é {name[0]} e o ultimo nome é {name[-1]}') #-1 pega o último elemento da lista 
#-1,-2,-3 pegam os elemtnos da lista ao contrario, do final para o começo!