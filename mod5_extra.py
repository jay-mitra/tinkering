import csv

# Read in the CSV file using csv.reader
with open("./City_of_Seattle_Wage_Data.csv", "r") as read_fh:

    # Store the header line in a variable using next (Links to an external site.)
    header = next(read_fh)
    input_list = list(csv.reader(read_fh))

# Create a dictionary to store the list of 'Hourly Rate' by job title (hint: this is a dictionary where the value is a list - seattle[job] = [rates]. You'll need to use key in dictionary or dictionary.get to see if the key exists in each dictionary and create it if it does not, similar to counting with dictionaries.)
hourly_rate_dict = {}
for line in enumerate(input_list):
    if line[1][-2] in hourly_rate_dict:
        # append the list with the rates
        hourly_rate_dict[line[1][-2]].append(line[1][-1])
    else:
        # create a new entry
        hourly_rate_dict[line[1][-2]] = [line[1][-1]]

# After your data structure is created, use a for loop to go over each job and calculate the average pay
for job_title, salaries in hourly_rate_dict.items():
    temp_salary = 0
    for salary in salaries:
        temp_salary = temp_salary + float(salary)
    else:
        # Print a sentence for each job saying how many people work that job and what the average pay is. (hint: if there's one person, you just need to print the first value of the rates list)
        print ("There are {} employees with the title \"{}\", and the average salary for that position is ${:.2f}.".format(len(salaries), job_title, temp_salary / len(salaries)))

# Calculate the highest paying job
# find the highest paying salary in the original list
temp_salary = [0]
for line in input_list:
    temp_salary.append(float(line[-1]))

max_salary = (max(temp_salary))
# iterate through the salaries and find the job title with the highest salary
current_max = 0
for job_title, salaries in hourly_rate_dict.items():
    for salary in salaries:
        if float(max(salaries)) > float(current_max):
            current_max = max(salaries)
else:
    print ("The highest paying job is \"{}\", with a salary of ${}.".format(job_title, current_max))

# Print the seattle dictionary to a file
with open("output.txt", "w") as write_fh:
    write_fh.write(str(hourly_rate_dict))
