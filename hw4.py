#!/usr/bin/env python

# Define two lists at the top of your file such as the ones below:
# These lists should match up, so Aliyah's age is 20, Bob’s age is 21, and so on. In this example, the names should be the keys and the age should be the value.
names = ["Aliyah", "Bob", "Cathy", "Dan", "Ed", "Frank", "Darnell", "Gary", "Shanice", "Irene", "Jack", "Kelly", "Demetrius"]
ages = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19, 30]
names_dict = dict(zip(names,ages))
# Give a the user 5 tries to check to see if a name is in the dictionary
# give them up to five tries by using a sentinel variable
# use a while loop to continue to ask if they haven't found a name in the dictionary or until they run out of tries
tries = 0
while tries < 5:
    tries += 1
    # ask the user to input a name
    # check if the name is in the dictionary (hint: use membership or get)
    # if the user is in the dictionary, return the user's age
    name_query = input("What name would you like to look up: ")
    if name_query in names_dict:
        print ("Your stalking has been successful! {} is {} years old...".format(name_query, names_dict[name_query]))
        break
    else:
        # if the user is not in the dictionary, return an error message
        print ("Beep Bop Boop. There is no {} here".format(name_query))
print ("You've used up {} out of 5 tries. Buh bye!".format(tries))
