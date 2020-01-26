#!/usr/bin/env python

import random

def fizzbuzz(test_num):
    """take an input integer, and return the correct fizzbuzz string"""
    if test_num % 15 == 0:
        return "FIZZBUZZ!"
    elif test_num % 3 == 0:
        return "FIZZ"
    elif test_num % 5 == 0:
        return "BUZZ"
    else:
        return "womp womp"

def main():
    while True:
        user_starting = input("Please enter a starting integer greater than zero :")
        if user_starting.isdigit():
            if int(user_starting) > 0:
                break
            else:
                print ("The integer should be greater than zero, please try again.")
        else:
            print ("That is not an integer, please try again.")

    while True:
        user_ending = input("Please enter an ending integer, which must be greater than the starting integer :")
        if user_ending.isdigit():
            if int(user_ending) > (int(user_starting)):
                break
            else:
                print ("The integer should be greater than {}, please try again.".format(int(user_starting)))
        else:
            print ("That is not an integer, please try again.")

    # Create a list of integers in the range of the user's starting and ending numbers
    user_list = list(range(int(user_starting),int(user_ending)))

    for x in user_list:
        print ("{}: {}".format(x,fizzbuzz(x)))

main()
