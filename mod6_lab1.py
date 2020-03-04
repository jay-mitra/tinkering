import os

# Change to your documents directory
os.chdir("../Documents/")

files_count = 0
directories_count = 0

for file in os.listdir():
    # Count the number of word and pdf files in your documents folder
    if file.endswith(".pdf") or file.endswith(".docx"):
        files_count += 1
    # Do the same for directories
    if file.startswith("."):
        directories_count += 1

print ("the number of files is {} and the number of directories is {}".format(files_count,directories_count))
