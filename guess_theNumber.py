import random

computerNumber = random.randint(1, 20)

print('What is your name? ')
name = input()
print('Hello,' + name)

for guesses in range(1, 7):
    print('Input a number')
    guessedNumber = int(input())

    if computerNumber > guessedNumber:
        print('Guess higher')
    elif computerNumber < guessedNumber:
        print('Guess lower')
    else:
        break

if computerNumber == guessedNumber:
    print('BRAVO! You guessed it in ' + str(guesses))
else:
    print('SORRY! The number I thinking of is ' + str(computerNumber))
