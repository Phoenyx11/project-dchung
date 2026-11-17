# This library is necessary to get input from a text file.
# Note that this is intended for use on the clusters - the
# regular python library is simply "ast"
from asteval import Interpreter
aeval = Interpreter()

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# Insert your weekly report function
# Ensure the function takes 3 pieces of input - the task dictionary,
# habit dictionary, and file name to read the data.

def weekly_report(tasks, habits, file_name):
    '''
    summarizes tasks and habits the user has added over the course of the week
    and whether they are complete or not
    '''
    print(f"{file_name} Weekly Report:")
    # Check if habits exist
    if len(habits) == 0:
        print("You do not have any active habits")
    else:
        print("Habit Summary:")
        # Loop through each habit, adding 1 for each day the habit was completed
        for habit in habits:
            completed_days = 0
            for day in weekdays:
                if habits[habit][day] == True:
                    completed_days += 1
            # Print the habit and how many days it was completed
            print(f"\t You completed {habit} {completed_days} days this week!")

    # Initialize task lists
    completed_tasks = []
    incomplete_tasks = []
    # Loop through each day and task and add to complete or incomplete list
    for day, val in tasks.items():
        for task, boo in val.items():
            if boo == True:
                completed_tasks.append(f"{task} ({day})")
            elif boo == False:
                incomplete_tasks.append(f"{task} ({day})")

    # Check if lists are empty
    if len(completed_tasks) != 0 or len(incomplete_tasks) != 0:
        # Check number of complete tasks, print message if none
        if len(completed_tasks) == 0:
            print("No completed tasks")
        else:
            # Loop through each complete task and print out
            print("Completed tasks:")
            for task in completed_tasks:
                print("\t", task)
        # Check number of incomplete tasks, print message if none
        if len(incomplete_tasks) == 0:
            print("No incomplete tasks")
            return
        else:
            # Loop throuhg each incomplete task and print out
            print("Incomplete tasks:")
            for task in incomplete_tasks:
                print("\t", task)
    # If no tasks are found, print that
    else:
        print("\n No tasks found")
        return

# Provide the list of files to process.
# The dictionaries.txt files each contain a list of
# two dictionaries, the first being for habits and
# the second for tasks. 
#
# Note that the files and this python script should be in the
# same directory when you run it.
file_list = ['dictionaries_1.txt', 'dictionaries_2.txt', 'dictionaries_3.txt', 'dictionaries_4.txt', 'dictionaries_5.txt', 'dictionaries_6.txt', 'dictionaries_7.txt', 'dictionaries_8.txt', 'dictionaries_9.txt', 'dictionaries_10.txt'] 

# This section will loop through the files in the list above, and 
# run the report_week() function for each file. 
#
# The use of the ast library allows you to read text files
# that contain Python structures, in this case a list of dictionaries
#
# This code loops through each file, assigns the list of dictionaries
# as the variable 'data', then gives the report_week() function
# the appropriate input.
#
# Ensure you edit the final line so it matches your function name,
# and supply the appropriate input.
for file_name in file_list:
    with open(file_name) as f:
        content = f.read()
        data = aeval(content)
        weekly_report(data[0], data[1], file_name)