password = Egg
guesses = 0
PWG

while guess < 5 and PWG == password:
    PWG = input('Please enter the password')
    if PWG == password:
        print('Welcome back')
    else:
        guesses = guesses + 1
        print('Incorrect password. Guesses remaining: '), 5 - guesses

print('Too many attempts. System will now terminate')
