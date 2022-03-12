#!/usr/bin/python3

from random import randrange

def get_input(text: str) -> int:
	n = -1
	while n < 0:
		try:
			n = eval(input(text))
		except NameError as error:
			print(f"Ivalid input : {str(error)}")
	return n

def main() -> None:
	a_l = 0
	for i in range(0, 5):
		attempts, r_n = 1, randrange(10)
		u_g = get_input("\nEnter your guess (0-9): ")
		while u_g != r_n:
			attempts += 1
			u_g = get_input(f"{'guess is too low' if u_g < r_n else 'guess to high'}! try again (0-9): ")
		a_l += attempts
		print(f"{u_g} is correct.\nNumber of attempted guesses : {attempts}")
	print(f"\n\tResults\nNumber of rounds : 5\nAverage number of guesses : {int(a_l / 5)} per raund")

if __name__ == "__main__":
	main()
