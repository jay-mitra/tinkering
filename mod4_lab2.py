# Create the following name list
names = ['mark', 'henry', 'matthew', 'paul', 'robert', 'joseph', 'carl', 'luke', 'mark', 'robert', 'joseph', 'carl', 'michael', 'mark', 'henry', 'matthew']
# Add in at least five female names (with repeats) to support women in tech!  Use append or extend.
names.extend(['emielie', 'jessica', 'jenny', 'samreen', 'salimah', 'saloni', 'denise', 'kim', 'xin', 'sarah', 'jackie', 'emilie', 'kim', 'mai-lan', 'sarah', 'kim', 'joan', 'jenny', 'kim', 'jean', 'jenny', 'sue'])

# Create an empty dictionary
names_dict = {}

# Create a for loop that iterates through the names list
# Using the name as the key, increment the count of that name in the dictionary
for name in names:
    if name in names_dict:
        names_dict[name] = names_dict[name] + 1
    else:
        names_dict[name] = 1

# find the most common name
# make dict.values() into a list
values_list = list(names_dict.values())

# make dict.keys() into a list
values_index = list(names_dict.keys())

# the list index method to find the index of the maximum value and store it as max_index
max_index = (values_index[(values_list.index(max(values_list)))])

# use the max_index to get the key at that index
print ("Most common name is {} with {} occurences.".format(max_index, names_dict[max_index]))
