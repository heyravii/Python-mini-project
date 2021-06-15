# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether t
# hey guessed too low, too high, or exactly right.

import random
num = str(random.randint(1,9))

guess = input( "guess any number ")

if guess == num:
    print(" you guessed correct ")
elif guess < num:
    print(" you guessed too low")
else:
    print(" you guessed too high")

print("computer guess is" + str(num) )