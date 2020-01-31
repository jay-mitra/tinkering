import re

s1 = "For instance, on the planet Earth, man had always assumed that he was more intelligent than dolphins because he had achieved so much — the wheel, New York, wars and so on — whilst all the dolphins had ever done was muck about in the water having a good time. But conversely, the dolphins had always believed that they were far more intelligent than man — for precisely the same reasons."
s2 = "The last ever dolphin message was misinterpreted as a surprisingly sophisticated attempt to do a double-backwards-somersault through a hoop whilst whistling the ‘Star Spangled Banner’, but in fact the message was this: So long and thanks for all the fish."

# Building the sets
s1 = (re.sub(r'[^\w]', ' ', s1.lower()))
s2 = (re.sub(r'[^\w]', ' ', s2.lower()))
set_s1 = set(s1.split(" "))
set_s2 = set(s2.split(" "))

# The number of unique words in each sentence
print ("The number of unique words in each sentence is {} for the first one and {} for the second one.".format(len(set_s1), len(set_s2)))

# The number of words that only appear in both sentences
print ("The number of words that only appear in both sentences is {}.".format(len(set_s1.intersection(set_s2))))

# The number of words that are contained in either one sentence or the other, but not in both
print ("The number of words that are contained in either one sentence or the other, but not in both is {}.".format(len(set_s1.symmetric_difference(set_s2))))
