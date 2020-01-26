#!/usr/bin/env python

# Assignment key deliverables:
# 1. Ask the user three original questions and store their input as variables
# 2. Combine the three answers into a sentence of your choosing
# 3. Print out the final combined sentence using one of the string operations
# 4. Add docstrings and comments to your code
# 5. (S) Create a function that contains the print statement (pass the variables in as arguments to use in the print function).

# Combine the three answers into a sentence of your choosing
# Print out the final combined sentence using one of the string operations
def print_sentence(user_name, user_birthplace, user_occupation):
    """ Create a function that contains the print statement (pass the variables in as arguments to use in the print function). """
    print ("Hey " + user_name + " I hope that " + user_occupation + "s are valued in " + user_birthplace)
    return

# Ask the user three original questions and store their input as variables
user_name = input("What is your name? ")
user_birthplace = input("What country were you born in? ")
user_occupation = input("What is your occupation or job? ")
print_sentence(user_name, user_birthplace, user_occupation)
