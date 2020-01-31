import random
import re
animal_list = ["elephant"]
animal = random.choice(animal_list)
guesses = ""
guessed_letters = ""
list_animal = list(animal)
list_guesses = list(guesses)


# get the number of letters in the animal name (use len)
guess_amount = len(animal) + 3
print("\nYou have " + str(guess_amount) + " guesses to guess the mystery animal.")

# set the number of guesses to be the animal name length plus 3

# use a while loop with a sentry variable

def progress():
    for i in range(len(animal)):
        if animal[i] in guesses:
            print(animal[i], end=""),
        else:
            print("_", end="")

counter = 0

while counter < guess_amount:
    print("\n")
    guess = input("Enter a letter. You have " + str(guess_amount - counter) + " guess(es) remaining. ")
    if len(guess) != 1:
        print("\nLimit text to one character.")
        continue
    elif not re.match("^[a-z]*$", guess):
        print("\nEnter lower case letters only.")
        continue
    counter += 1
    guesses += guess
    if guess in animal:
        print("\nYour letter is in the word! \n\nYou have guessed the letter(s) \"" + guesses + "\" so far.")
        progress()
        result = all(item in list_guesses for item in list_animal)
        print (guess)
        print (list_guesses)
        print (list_animal)
        print (result)
        if result == True:
            print("\nYou guessed the animal! Well done!")
            break
        else:
            continue
    elif guess not in animal:
        print("\nYour letter is not in the word!")
        if counter == guess_amount:
            break
        continue
if counter == guess_amount:
    print("\nYou have run out of guesses. You lose!")
