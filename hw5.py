import re

# Read in the file and store in a list. Convert the list of book lines into a list of the words
with open("./land_time_forgot.txt") as read_fh:
    lines_list = read_fh.readlines()
    words_list = []
    for line in lines_list:
        words_list.extend(line.strip().split(" "))

# Print a sentence using format with the total number of words and the unique number of words
print ("The total number of words is {} and the total unique number of words is {}.".format(len(words_list),len(set(words_list))))

# Calculate the word count for each word. Additioanly, store all of the words that have the minimum word count in a list (hint: use a for loop and items (Links to an external site.))
words_dict = {}
for word in words_list:
    if word in words_dict:
        words_dict[word] = words_dict[word] + 1
    else:
        words_dict[word] = 1

# Calculate the word with the maximum count (hint: use max (Links to an external site.))
max_word = max(words_dict, key=lambda k: words_dict[k])
max_count = words_dict[max_word]
print ("The word with the maximum count of {} is \"{}\"".format(max_count,max_word))

# Get the minimum word count (hint: use values (Links to an external site.))
min_word = min(words_dict, key=lambda k: words_dict[k])
min_count = words_dict[min_word]
print ("The word with the minimum count of {} is \"{}\"".format(min_count,min_word))

# Store all of the words that have the minimum word count in a list (hint: use a for loop and items)
min_words_list = []
for word, count in words_dict.items():
    if count == min_count:
        min_words_list.append(word)

# Print a sentence including the minimum word count and the number of words with that count
print ("The minimum word count is {} and the number of words with that count is {}.".format(min_count,len(min_words_list)))
# Print a sentence of the percentage of words that are unique in the book (hint: use :.1f in your format)
print ("The percentage of words that are unique in the book is {:.1f}%".format(len(set(words_list))/len(words_list)*100))

# Find all lines that contain the word "smoke" using the following regular expression and print them to a file
with open("output.txt", "w") as write_fh:
    now_count = 0
    dialogue_count = 0
    for line in lines_list:
        if re.match("(.*)smoke(.*)", line):
            write_fh.writelines("We found some smoke! : {}".format(line))
        # Add another regular expression to count the number of times the word 'now' is used in the book.
        if re.match("(.*)now(.*)", line):
            now_count += 1
        # Add another regular expression to count the number of times there is dialogue in the book - words separated by double quotes.
        if re.match("(.*)\"(.*)", line):
            dialogue_count += 1
    else:
        write_fh.writelines("We found the word \"now\" {} times.\n".format(now_count))
        write_fh.writelines("We found {} lines of dialogue.\n".format(int(dialogue_count/2)))
