#!/usr/bin/env python

import random

print("""
	Guess my number game!

Guess a chosen number between 1 and 100 in 5 guesses or less!
""")

random_number = random.randint(1, 100)
total_guesses = 0
guess = 0
continue_playing = True

while continue_playing:
	if total_guesses == 5:
		continue_playing = False
		print("You lost! You'll do better next time!")	
	else:
		user_input = input("Take guess number {0}: ".format(str(total_guesses+1)))
		if user_input.isnumeric():
			guess = int(user_input)

		if not user_input.isnumeric():
			print("Your guess was '{0}'? You can only guess numbers silly!".format(user_input))
		elif guess > random_number:
			print("Your guess was too high!")
		elif guess < random_number:
			print("Your guess was too low!")
		elif guess == random_number:
			continue_playing = False
			print("You guessed it! You won!")
	
	total_guesses += 1
