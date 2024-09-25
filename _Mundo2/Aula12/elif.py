name = str(input('Qual seu nome?')).strip().capitalize()
if name == 'Henrique':
    print('if - What a beatiful name')
elif name == 'Pedro' or name == 'Luis' or name == 'Marcelo':
    print('elif1 - seu nome é masculino')    
elif name in 'Guêssa Luisa Marcela': #pode fazer ele procurar em uma lista
    print('elif2 - seu nome é feminino')
else:
    print('else - Henrique is a better name')
print(f'Tenha um bom dia, {name}')