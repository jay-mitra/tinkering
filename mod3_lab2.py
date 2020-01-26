#!/usr/bin/env python

import random

def human_binary_search():
    """let's play a game! the human will be guessing a number between 1 and 10, and we'll give them hints"""
    # generate a target between 1 and 10
    target = random.randint(1, 10)
    # sentinel variable to track the number of guesses a user has used, they'll have a max of 3
    sentinel = 0
    print ("Hi! Welcome to the number guesser.\nI've picked a number between 1 and 10.\nYou get three attempts to guess my number.")
    while sentinel < 3:
        guess = int(input("What's your guess? "))
        if guess < 0 or guess > 10:
            print ("You seem to be struggling with following basic instructions... Maybe go read up on some maths...")
            break
        # if it does match print congratulations and break
        if guess == target:
            print ("Wow, you got it! Winner winner chicken dinner...")
            break
        # if it doesn't match see if it's higher or lower than the number and print a hint
        elif guess > target:
            print ("Too high bud")
        elif guess < target:
            print ("Too low bud")
        sentinel = sentinel + 1
        # let them know how many guesses they have left
        print ("You've got {} guesses left.".format(3-sentinel))
    print ("Game over!")

human_binary_search()
