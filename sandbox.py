import random

# make a list of animals
# animals = ["otter", "monkey", "rabbit", "horse", "tiger", "rat", "snake", "panda"]
animals = ["aardvaark"]
# get a random animal
random_animal = animals[random.randint(0, len(animals)-1)]
# find the longest animal name
longest_animal_name = ""
longest_length = 0
for animal in animals:
    if len(animal) > longest_length:
        longest_length = len(animal)
        longest_animal_name = animal
# set the number of guesses to be the animal name length plus 3
total_guesses = longest_length + 3
# print welcome and instructions
print("Welcome to guess that animal!  Enter letters one at a time.  You have " + str(total_guesses) + " guesses.")
# create a list to store the guessed letters and correct letters
guessed_letters = []
correct_letters = list('-' * len(random_animal))
# use a while loop with a sentry variable
guesses = 0
while guesses < total_guesses:
    # get user input of a letter
    letter = input("")
    # clean user input
    # make sure they are guessing letters
    while letter.isalpha() is False:
        print("That's not a letter, please try again.")
        letter = input("")
    # make sure they are guessing one letter
    while len(letter) > 1:
        print("Only guess one letter at a time, please.")
        letter = input("")
    # check if the letter is in the animal name
    if letter in random_animal:
        print("That letter is in my animal!")
    # store the guessed letter in a list
    guessed_letters.append(letter)
    # increment the sentry variable
    guesses += 1
    # update the correct letter list
    for index, letter in enumerate(random_animal):
        if letter in guessed_letters:
            correct_letters[index] = letter
    # if all of the letters in the animal are in the guess letter list, break and congratulate the user
    if random_animal == ''.join(correct_letters):
        print("Congratulations you have guessed my animal! " + "[ " + ' '.join(correct_letters) + " ]")
        break
    # if the sentry variable is bigger or equal to the guesses, break and console the loser
    if guesses >= total_guesses:
        print("Sorry, you're out of guesses! The animal was " + animal + ".")
        break
    # print the status of the game
    print("[ " + ' '.join(correct_letters) + " ]")
    print("You have " + str(total_guesses - guesses) + " more guesses. What is your next guess?")
