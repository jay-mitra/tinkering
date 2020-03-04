# When you try to open a file that doesn't exist on your file system the open function raises a nice error called FileNotFoundError
# ```bash
# >>> open('some_file_location.txt', 'r')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileNotFoundError: [Errno 2] No such file or directory: 'some_file_location.txt'
# >>>
# ```
# Write a script called module8_lab2.py. In the script write some pseudo code that opens a non-existent file location and use try/except to handle the FileNotFoundError and output a nicer message for the user about what happened.
# Let's say some other type of error happens but we don't know the specific name of it. How can our try/except handle this?
# Post your code and answers to this lab for credit
# HINT: look up try/except/finally and python built-in exceptions (Links to an external site.)
# Stretch goal: write a Command Line Interface (CLI) to get the file name from argv for your error handling.

import sys

if __name__ == "__main__":
    try:
        open(sys.argv[1], "r")
        print ("file \"{}\" was opened successfully!".format(sys.argv[1]))
    except FileNotFoundError:
        print ("Aw shucks pal, I couldn't find a file called \"{}\" ...".format(sys.argv[1]))
    except IndexError:
        print ("I don't think you gave me a file to open!")
    except Exception as e:
        print ("Yeah, something super weird happened, apparently the error was: \"{}\".".format(e))
