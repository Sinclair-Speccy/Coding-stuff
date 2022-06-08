from random import randint
secret_num = randint(1,10)
guess = 0
number_guesses = 0
while guess != secret_num:
    number_guesses = number_guesses + 1
    guess = eval(input('Guess the secret number: '))
print('You finally got it!', number_guesses, 'guesses!')