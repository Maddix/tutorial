#!/usr/bin/env python

import random

difficulty_types = ['novice', 'easy', 'medium', 'hard']
difficulty_indexes = list(map(str, range(0, len(difficulty_types))))

_DIFFICULTY_STEP_ = 5
_DIFFICULTY_ = list(map(lambda x: (1 + int(x))*_DIFFICULTY_STEP_, difficulty_indexes))
_DIFFICULTY_.reverse()
_DEFAULT_DIFFICULTY_ = difficulty_types[0]

print("""
	Guess my number game!

Guess a chosen number between 1 and 100!
""", end="")

pretty_difficulty_types = difficulty_types.copy()
pretty_difficulty_indexes = difficulty_indexes.copy()

pretty_difficulty_types.append("or {0}".format(pretty_difficulty_types.pop()))
pretty_difficulty_indexes.append("or {0}".format(pretty_difficulty_indexes.pop()))

pretty_difficulty_types = ", ".join(pretty_difficulty_types)
pretty_difficulty_indexes = ", ".join(pretty_difficulty_indexes)

print("""
	Choose a difficulty!

Type {0}. Alternatvely you can type {1}. To select the first option simply press enter.
""".format(pretty_difficulty_types, pretty_difficulty_indexes))

chosen_difficulty = None

while not chosen_difficulty:
	user_input_difficulty = input("Select a difficulty level: ".format(_DEFAULT_DIFFICULTY_)).strip().lower()

	if user_input_difficulty.isnumeric():
		if user_input_difficulty in difficulty_indexes:
			chosen_difficulty = difficulty_types[int(user_input_difficulty)]
		else:
			print("'{0}' isn't a valid choice! Try {1}".format(user_input_difficulty, pretty_difficulty_indexes))
	elif user_input_difficulty.isalpha():
		if user_input_difficulty in difficulty_types:
			chosen_difficulty = user_input_difficulty
		else:
			print("'{0}' isn't a valid choice! Try {1}".format(user_input_difficulty, pretty_difficulty_types))
	elif not user_input_difficulty:
		chosen_difficulty = _DEFAULT_DIFFICULTY_
	else:
		print("'{0}' isn't a valid choice! Try {1}. Alternatively you can type {2}.".format(
			user_input_difficulty,
			pretty_difficulty_types,
			pretty_difficulty_indexes
		))

max_guesses = _DIFFICULTY_[difficulty_types.index(chosen_difficulty)]

print("""
	{0} difficulty has been chosen! You have {1} guesses!
""".format(chosen_difficulty.capitalize(), max_guesses))

random_number = random.randint(1, 100)
total_guesses = 0
guess = 0
continue_playing = True

while continue_playing:
	total_guesses += 1

	if total_guesses > max_guesses:
		continue_playing = False
		print("You lost!\n\n\tYou'll do better next time!\n")	
	else:
		user_input = input("Take guess number {0}: ".format(str(total_guesses)))
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
			print("You guessed it!\n\n\tYou won in {0} guesses!\n".format(total_guesses))
	
