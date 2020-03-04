
def file_into_list(filename):
    """a function that turns an input filename, opens it and returns it as a list of lines"""
    with open(filename) as file:
        return file.readlines()

def list_into_words(in_list):
    """a function that converts an input list strings into a list of words, splitting by a space"""
    word_list = []
    for line in in_list:
        word_list.extend(line.strip().split(" "))
    return word_list

def word_count(in_list):
    """a function that calculates the word count"""
    word_count = {}
    for word in in_list:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
    return word_count

def min_word_count(in_dict):
    """a function that takes a dictionary as input, calculates the minimum word count and returns a list of words and the minimum word count as a tuple"""
    min_word_count = min(in_dict.values())
    min_words = []
    for word, cnt in in_dict.items():
        if cnt == min_word_count:
            min_words.append(word)
    return min_words, min_word_count

def main():
    """let's get this show on the road"""
    filename = "./land_time_forgot.txt"
    parsed_lines = file_into_list(filename)
    parsed_words = list_into_words(parsed_lines)
    unique_words = set(parsed_words)
    print("There are {} words in the book and {} of them are unique".format(len(parsed_words), len(unique_words)))
    unique_words_dict = word_count(parsed_words)
    max_word = max(unique_words_dict, key=unique_words_dict.get)
    print("The word that occurs most is '{}' with count {}".format(max_word, unique_words_dict[max_word]))
    min_words = min_word_count(unique_words_dict)
    print("The lowest word count is {} and there are {} words in the book with that word count".format(min_words[1], len(min_words[0])))

main()
