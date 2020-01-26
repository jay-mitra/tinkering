#!/usr/bin/env python

import random, os

global_animal_names = ["cat", "dog", "aardvaark", "narwhal", "ant", "ibex", "kudu", "wombat"]

def animal_guessing_game():
    """pick a random animal name from the global list, and play a guessing game with the user through stdin"""
    animal_name = random.choice(global_animal_names)
    guesses = len(animal_name) + 3
    name_render = ["?"] * len(animal_name)
    print ("Welcome to guess that animal!")
    print ("Enter letters one at a time.")
    print ("You have {} guesses, to get this word: {}".format((guesses),name_render))
    sentry = 0

    while sentry < guesses:
        user_input = input("\nguess a letter:")
        if len(user_input) > 1:
            print ("You were supposed to give me a single letter only. I'm assuming you meant just {}".format(user_input[0]))
            user_input = user_input[0]
        if user_input in animal_name:
            # this for loop is necessary to iterate through the whole string and grab any duplicate correctly guessed letters (e.g. all the "a"s in aardvaark and place them in the name_render array, otherwise the "if x in string" stops at the first one...)
            for x in enumerate(animal_name):
                if x[1] == user_input:
                    name_render[x[0]] = user_input
            print ("Excellent! You guessed well, {} is in the animal name.".format((user_input)))
            print ("You now have {}".format(str(name_render)))
            # the temp string is needed to be able to collapse the array of characters into a string for the comparison to see if the user has won or not.
            temp_string = ""
            temp_string = temp_string.join(name_render)
            if animal_name == temp_string:
                print ("you won!")
                break
        else:
            print ("Shame, that letter is not in my animal name...")
        sentry = sentry + 1
        print ("You have {} guesses remaining".format(guesses - sentry))
    else:
        print ("You ran out of guesses, better luck next time! My word was {}".format(animal_name))

os.system('cls' if os.name == 'nt' else 'clear')
animal_guessing_game()
