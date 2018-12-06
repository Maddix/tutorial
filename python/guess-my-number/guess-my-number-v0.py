#!/usr/bin/env python

import random

print("""
	Guess my number game!

Guess a chosen number between 1 and 100 in as few guesses as possible!
""")

random_number = random.randint(1, 100)
guess = 0

while guess != random_number:
	user_input = input("Take a guess: ")
	if user_input.isdigit() and not user_input.isalpha():
		guess = int(user_input)

	if guess > random_number:
		print("Your guess was too high!")
	elif guess < random_number:
		print("Your guess was too low!")
	else:
		print("You guessed it! You won!")
