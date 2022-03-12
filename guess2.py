#!/usr/bin/python3

from random import randrange

total_attempts = 0

for i in range(0, 5):
	random_number = randrange(10)
	attempts = 1
	your_guess = eval(input("\nEnter your guess (0-9): "))
	while your_guess != random_number:
		attempts += 1
		if your_guess < random_number:
			your_guess = eval(input("Guess too low! try again: "))
		else:
			your_guess = eval(input("Guess too high! try again: "))
	total_attempts += attempts
	print(your_guess, "is correct!\nNumber of attempted guesses", attempts)
print("\n\tResults\nNumber of rounds : 5\nAverage number of guesses :", int(total_attempts / 5), "per round")


