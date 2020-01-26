#!/usr/bin/env python

def main():

    # Ask the user to enter a starting number
    # The user must not enter a starting number less than 1
    # Create checks and error messages for the above
    while True:
        user_starting = input("Please enter a starting integer :")
        if user_starting.isdigit():
            if int(user_starting) >= 1:
                break
            else:
                print ("The integer should be greater than 1, please try again.")
        else:
            print ("That is not an integer, please try again.")

    # Ask the user to enter an ending number
    # The user must enter an ending number at least 5 times greater than the starting number
    # Create checks and error messages for the above
    while True:
        user_ending = input("Please enter an ending integer, which must be at least 5 times greater than the starting integer :")
        if user_ending.isdigit():
            if int(user_ending) >= (int(user_starting) * 5):
                break
            else:
                print ("The integer should be greater than {}, please try again.".format(int(user_starting)*5))
        else:
            print ("That is not an integer, please try again.")

    # Create a list of integers in the range of the user's starting and ending numbers
    user_list = list(range(int(user_starting),int(user_ending)))
    running_total = 0

    # Print out the number and index of each item in the list that is even, sum all the odd numbers in the list using a for loop
    # I thought I'd do it all in the same for loop...
    for x in enumerate(user_list):
        if x[1] % 2 == 0:
            print ("The number {} is at index {} in the list.".format(x[1],x[0]))
        else:
            running_total += x[1]

    # Print out the cumulative sum calculated above (running total)
    print ("The sum of the odd numbers in your list is {}.".format(running_total))

# Wrap your steps in a function and call the function
main()
