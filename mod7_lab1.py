"""
Q1. What does list1 and list2 contain?
List1 containts a list of two lists, and List 2 is a pointer to it
Q2. What space in memory have list1 and list2 been assigned to? Are they the same?
The same memory
Q3. Now what do list1 and list2 contain? What happened?
The update changed the first sublist in list1, which also did it for list2 as it is a pointer
Q4. What does [:] in the above statement mean?
It explicitly instructs python to populate list2 with the elements of list1, so the list1 and list2 objects now occupy different memory spaces
Q5. What do list1 and list2 contain now? Why? (Hint, check the memory space each item has been assigned to).
The first elements are now different.
Q6. What do list1 and list2 contain now? Why?
The second elements have now both been updated through the append, as the elements within the lists themselves are still shallow copies (i.e. pointers).
Q7. Post your code for the following steps:

Following the instructions from the lecture, make list2 a deep copy of list1.
Append the letter "x" to list1
Report what list1 and list2 now contain

list2 = deepcopy(list1)
list1[1].append('x')

print (list1)
print (list2)
print (id(list1))
print (id(list2))
"""

from copy import deepcopy

list1 = [ [1,2,3], ['a','b'] ]
list2 = list1

print (list1)
print (list2)
print (id(list1))
print (id(list2))

# setting an element to a new value
list1[0] = [5,6,7]

print (list1)
print (list2)
print (id(list1))
print (id(list2))

list2 = list1[:]

print (list1)
print (list2)
print (id(list1))
print (id(list2))

list1[0] = [2,4,6]

print (list1)
print (list2)
print (id(list1))
print (id(list2))

list1[1].append('c')

print (list1)
print (list2)
print (id(list1))
print (id(list2))

list2 = deepcopy(list1)
list1[1].append('x')

print (list1)
print (list2)
print (id(list1))
print (id(list2))
