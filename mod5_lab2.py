import os, operator

with open("./land_time_forgot.txt") as read_f:
    # Read the file into a list
    # Convert the list of book lines into a list of the words (hint: use string.split(), a for loop and list.extend (Links to an external site.) OR string.split, two for loops and list.append)
    lines_list = read_f.readlines()
    words_list = []
    for line in lines_list:
        words_list.extend(line.strip().split(" "))
    #Print a sentence using format with the total number of words
    print ("The total number of words is: {}".format(len(lines_list)))
    #Use split to get the project_title and author from the first line of your book lines list
    project_title, project_author = lines_list[0].split(", by ")
    project_owner, project_title = project_title.split("'s")
    print ("Project is : {}".format(project_owner))
    print ("Title is : {}".format(project_title))
    print ("Author is : {}".format(project_author))

# stretch goal
words_dict = {}
for word in words_list:
    if word in words_dict:
        words_dict[word] = words_dict[word] + 1
    else:
        words_dict[word] = 1

max_word = (max(words_dict.items(), key=operator.itemgetter(1)))
print ("The most common word is \"{}\" with {} occurences.".format(max_word[0], max_word[1]))
