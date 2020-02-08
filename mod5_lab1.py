import os

def parse_book(lines_list):
    # Calculate the total number of lines in the file
    # Calculate the lines that are in 1/3rd of the file
    thirds = int(round(len(lines_list) / 3, 0))
    # Store the middle third of the book's lines in a list (hint: use list slicing)
    middle_lines_list = lines_list[thirds:thirds * 2]
    # Print the number of lines in the file and the number of lines in the middle third of the book
    outlines = []
    outlines.append("The number of lines in the file is {} and the number of lines in the middle third of the book is {}.".format(len(lines_list),len(middle_lines_list)))
    # Print the line that is 1/3rd of the way through the book and the line that is 2/3 of the way through the book
    outlines.append("The line that is 1/3rd of the way through the book is:\n\n>  {}".format(middle_lines_list[0]))
    outlines.append("The line that is 2/3rd of the way through the book is:\n\n>  {}".format(middle_lines_list[-1]))
    return outlines

with open("./land_time_forgot.txt") as read_f:
    # Read the file into a list
    lines_list = read_f.readlines()
    output = parse_book(lines_list)
    for line in output:
        print (line)
    with open('./output.txt', 'w') as write_f:
    # Write the lines you printed above to a file
        for line in output:
            write_f.write(line)
