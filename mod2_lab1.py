#!/usr/bin/env python

# For this Lab, we'll add on to what we learned in Module 1 while practicing some basic arithmetic and string formatting operations.
# For this Lab make a single function that does the following:

# Creates variables to store user input for:
# User name
# User phone number
# Favorite cheese
# Average monthly amount spent on their favorite cheese

# Calculates the daily amount this user spends on cheese and store this value as a variable
# Uses the string split() method to store the last four digits of the user's phone number as a variable
# Uses the string slice() method to store the first three letters of the user's name as a variable
# Combines the last_four_phone_number variable with the first_three_username variable to create an account ID
# Uses the replace() method to replace the first letter of your User ID with a Z and store that value as the final user ID
# Prints a sentence that references the user ID, their favorite cheese and how much they spend each day on that cheese. You may use any formatting method you prefer.

user_name = input("What is your name? ")
user_phone_number = input("What is your phone number? Please specify in XXX-XXX-XXXX: ")
user_favourite_cheese = input("What is your favourite cheese? ")
user_cheese_monthly_spend = input("How much do you spend a month on cheese? ")
days_per_month = 31
cheese_daily_spend = int(user_cheese_monthly_spend) / days_per_month
last_four_phone_number = user_phone_number.split('-')[-1]
#last_four_phone_number = user_phone_number[-4:]
first_three_username = user_name[:3]
account_ID = str(last_four_phone_number) + str(first_three_username)
account_ID = account_ID.replace(account_ID[0], "Z", 1)
# account_ID ="Z" + account_ID[1:]
print (account_ID + " you have spent " + "$" + str(round(cheese_daily_spend,2)) + " on " + user_favourite_cheese + " per day")
