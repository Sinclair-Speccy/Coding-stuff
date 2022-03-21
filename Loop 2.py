guess = eval(input("Guess a number between 1 and 10: "))

while guess != 13:
    print("Wrong, guess again")
    guess = eval(input("Guess a number between 1 and 10: "))

print("You guessed the number")