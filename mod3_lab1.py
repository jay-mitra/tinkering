#!/usr/bin/env python

numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
743, 527]

def main():
# use a for loop and enumerate to iterate through the numbers
    for x in enumerate(numbers):
        print (x)
        # if the number is 237 then break the loop
        if x[1] == 237:
            print ("Gah! We found 237 at position {}! Abandon ship!!".format(str(x[0])))
            abandon_ship(x[0])
            break
        # if the number is even print the number and index
        if x[1] % 2 == 0:
            print ("We found the even value {} in position {}".format(x[1],str(x[0])))

def abandon_ship(position):
    """Find what position 237 is in the list and make a new list that only contains the numbers up until that point"""
    new_numbers = numbers[:position]
    new_numbers.sort()
    # What is the maximum and minimum number in the new list?
    print ("The maximum and minimum numbers in the new list are {} and {}.".format(new_numbers[0],new_numbers[-1]))

main()
