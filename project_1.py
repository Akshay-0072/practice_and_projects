import random

randNumber = random.randint(1, 10)
userGuess = None
guesses = 0

while (userGuess != randNumber):
    userGuess = int(input("Enter a number: "))
    guesses += 1
    if(userGuess==randNumber):
        print("Your guess is right")
        print("you have tried: ", guesses, "times")
    else:
        if(userGuess>randNumber):
            print("Your guess is greater than the number! guess lower number")
        else:
            print("You guess is lesser than the number! guess higher number")
