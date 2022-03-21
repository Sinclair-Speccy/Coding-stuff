from random import randint

num = randint(1, 10):
    guess = evalinput('Enter your guess: ')
    if guess==num:
        print('You got it!')
        break
    else:
        if guess < num:
            print('Higher')
        if guess > num:
            print('Lower')
            