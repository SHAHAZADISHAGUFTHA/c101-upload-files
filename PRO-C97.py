import random
print("Number Guessing game")
number = 9
chances = 0
print("Guess a random number")

while chances < 5:
    guess = int(input("Enter your guess:- "))
    if guess == number:
        print("Congratulation YOU WON")
    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)
    else:
        print("Your guess was too high: Guess a number lower than", guess)
    chances += 1
    if not chances < 5:
        print("YOU LOSE!!! The number is,9")                   