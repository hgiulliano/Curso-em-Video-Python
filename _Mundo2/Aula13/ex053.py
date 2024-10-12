phrase = str(input('Digite sua frase: ')).upper().strip()
separated = phrase.split()
together = ''.join(separated)
palindromo = []

#for para inverter a string

for letra in range(len(together)-1, -1, -1):
    palindromo.append(together[letra])

# Mas, poderia ser substituido em PYTHON por inverter a string usando slicing:
# palindromo = together[::-1]

palindromo= ''.join(palindromo)
print(palindromo)
if together == palindromo:
    print('A sua palavra/frase é um palindromo')
else:
    print('A sua palavra/frase não é um palindromo')