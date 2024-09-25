from random import randint
number = randint(0,5)
print(number)
guess = int(input('guess a number between 0 and 5: '))
if guess == number:
    print('Congrats, nice guess!')
else:
    print('You got it wrong, sorry buddy')