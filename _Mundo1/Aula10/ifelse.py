name = str(input('Qual seu nome?: '))
if name.capitalize() == 'Henrique':
    print('Que nome bonito!!')
else:
    print('Henrique é um nome mais bonito')
    
print(f'Que nome bonito!!' if name.capitalize() == 'Henrique' else 'Pessimo nome')