#=====importing libraries=====
from datetime import date

#=====Defining Functions=====
# register a user
def reg_user():
  
  # ask user for inputs
  new_username = input("Enter a new username: ")
  new_password = input("Enter a new password: ")
  confirm_password = input("Confirm new password: ")
  
  # check that the username is not already taken
  name_bool_invalid = False
  for user in range(len(valid_users)):
    if new_username == valid_users[user][0]:
      name_bool_invalid = True
      break
    else:
      name_bool_invalid = False
  
  # if the username is unique and the passwords match, add the user
  if new_password == confirm_password and name_bool_invalid is False:
    valid_users.append([new_username, new_password])
    user_list_read.append(f"{new_username}, {new_password}")
    user_list.write(f"\n{new_username}, {new_password}")
    print("User registration successful\n")
  
  # if the username is not unique, tell the user to try another username
  elif new_password == confirm_password and name_bool_invalid is True:
    
    while name_bool_invalid is True:
      print(f"The passwords match but {new_username} is already taken! Please try another username and we'll keep the password the same.")
      new_username = input("Enter a new username: ")
      
      for user in range(len(valid_users)):
        
        # if the username is not unique again, go back to the top of the while loop and ask the user to try again
        if new_username == valid_users[user][0]:
          name_bool_invalid = True
          break
        
        # when the username is unique, add the user and break the while loop so that the user is added once
        else:
          name_bool_invalid = False
          valid_users.append([new_username, new_password])
          user_list_read.append(f"{new_username}, {new_password}")
          user_list.write(f"\n{new_username}, {new_password}")
          print("User registration successful\n")
          break
          
  # in all other cases, the passwords do not match so tell the user to try again
  else:
    print("The passwords you entered do not match.\nPlease try registering a user again.\n")

# add a task
def add_task():
  
  # ask the user for inputs
  assigned_user = input("Enter the username of the person being assigned the task: ")
  task_title = input("Enter the title of the task: ")
  task_description = input("Enter a brief description of the task: ")
  date_assigned = date.today().strftime("%d %b %Y")
  date_due = input("Enter the date the task is due: ")
  completed = "No"
  
  # append the new task to list
  new_task = f"{assigned_user}, {task_title}, {task_description}, {date_assigned}, {date_due}, {completed}"
  task_list_read.append(new_task)

# view all tasks
def view_all():
  # split each item in the task list into into its components then print
  for task in range(len(task_list_read)):
    assigned_user, task_title, task_description, date_assigned, date_due, completed = task_list_read[task].split(", ")
    print(f"----- {task_title} -----\n"
    f"Task number: {task + 1}\n"
    f"Assigned to: {assigned_user}\n"
    f"Description: {task_description}\n"
    f"Date assigned: {date_assigned}\n"
    f"Due date: {date_due}\n"
    f"Completed: {completed}\n")

# mark task as complete
def complete_task():
  # split the task into its components
  assigned_user, task_title, task_description, date_assigned, date_due, completed = task_list_read[task_selected-1].split(", ")
  # mark the task as complete
  completed = "Yes"
  # rejoin the components
  task_list_read[task_selected-1] = ", ".join([assigned_user, task_title, task_description, date_assigned, date_due, completed])
  print(f"Task number {task_selected} completed!")

# edit task
def edit_task():
  # split the task into its components
  assigned_user, task_title, task_description, date_assigned, date_due, completed = task_list_read[task_selected-1].split(", ")
  
  edit_task_bool = True # create a switch to control while loop
  while edit_task_bool:
    # allow the user to select the component they want to edit
    edit_component = input(f"Select one of the following options to edit: \n\n"
    f"user - Assigned user\n"
    f"title - Task title\n"
    f"description - Task description\n"
    f"date - Date due\n"
    f"done - To finish editing\n\n"
    ).lower()
    
    if edit_component == "user":
      assigned_user = input("Enter the username of the new person assigned to this task: ")
      
    elif edit_component == "title":
      task_title = input("Enter the new task title: ")
      
    elif edit_component == "description":
      task_description = input("Enter the new task description: ")
      
    elif edit_component == "date":
      date_due = input("Enter the new due date for this task: ")
      
    elif edit_component == "done":
      # print the task after the edits so the user can check
      task_list_read[task_selected-1] = ", ".join([assigned_user, task_title, task_description, date_assigned, date_due, completed])
      print(f"----- {task_title} -----\n"
      f"Task number: {task_selected}\n"
      f"Assigned to: {assigned_user}\n"
      f"Description: {task_description}\n"
      f"Date assigned: {date_assigned}\n"
      f"Due date: {date_due}\n"
      f"Completed: {completed}\n")

      print("Editing complete")
      
      # add changes to the file
      
      # change to false to end the while loop
      edit_task_bool = False
      
    else:
      print("You have selected an invalid option.")

# view my tasks
def view_mine():
  # go through each item in the task list, split it into its components and if the assigned_user is the same as the user, print
  for task in range(len(task_list_read)):
    assigned_user, task_title, task_description, date_assigned, date_due, completed = task_list_read[task].split(", ")
    if assigned_user == username:
      print(f"----- {task_title} -----\n"
      f"Task number: {task + 1}\n"
      f"Assigned to: {assigned_user}\n"
      f"Description: {task_description}\n"
      f"Date assigned: {date_assigned}\n"
      f"Due date: {date_due}\n"
      f"Completed: {completed}\n")
  
  # allow the user to select a task
  while True:
    global task_selected # make this variable global so it can be passed into different functions
    task_selected = int(input(f"Enter the task number to edit or mark the task as complete.\n"
    f"If you would like to return to the main menu, please enter -1 ")) - 1
    
    # if the user selects an invalid option
    if task_selected < -2 or task_selected > len(task_list_read):
      print("You have selected an invalid option. Try again")
    
    
    # if the user has selected a task that they are not assigned to
    elif assigned_user != username:
      print("You are not permitted to see the tasks of other users")
      
    
    # if the user selects -1 to return to the main menu
    elif task_selected == -2:
      break
    
    # if the user has selected a task that is complete
    elif complete == "Yes":
      print("This task has already been completed")
    
    # if the user has selected one of their tasks
    elif assigned_user == username and complete != "Yes":
      edit_or_complete = input("Enter `edit` to edit the task or `complete` to mark it as complete. ").lower()
      
      # mark the task as complete
      if edit_or_complete == "complete":
        complete_task()
        break
      
      # edit the task
      elif edit_or_complete == "edit":
        print(f"Edit task number {task_selected}")
        edit_task()
        break
      
      # if the user has not selected edit or complete
      else:
        print("You have made an invalid option. Please try again.")

# task overview report
def task_overview_report():
  # total number of tasks generated and tracked
  tasks_total = len(task_list_read)
  
  
  # total number of completed tasks
  completed_counter = 0
  # split each task into its components
  for task in range(len(task_list_read)):
    assigned_user, task_title, task_description, date_assigned, date_due, completed = task_list_read[task].split(", ")
    # if the task is completed, add one to the counter
    if completed == "Yes":
      completed_counter += 1
  
  
  # total number of incomplete tasks
  incomplete_counter = 0
  # split each task into its components
  for task in range(len(task_list_read)):
    assigned_user, task_title, task_description, date_assigned, date_due, completed = task_list_read[task].split(", ")
    # if the task is completed, add one to the counter
    if completed == "No":
      incomplete_counter += 1
  
  
  # total number of tasks that are incomplete and overdue
  overdue_counter = 0
  # split each task into its components
  for task in range(len(task_list_read)):
    assigned_user, task_title, task_description, date_assigned, date_due, completed = task_list_read[task].split(", ")
    # if the date due is less then (i.e. before) today, add one to the couter
    if date_due < date.today().strftime("%d %b %Y"):
      overdue_counter += 1
  
  
  # percentage of tasks that are incomplete
  percentage_incomplete = incomplete_counter/tasks_total*100
  
  
  # percentage of tasks overdue
  percentage_overdue = overdue_counter/tasks_total*100
  
  
  # write text file report
  task_overview = open("task_overview.txt", "w")
  task_overview.write(f"Task Overview Report\n\n"
  f"Total number of tasks generated and tracked: {tasks_total}\n"
  f"Total number of completed tasks: {completed_counter}\n"
  f"Total number of incomplete tasks: {incomplete_counter}\n"
  f"Total number of tasks that are incomplete and overdue: {overdue_counter}\n"
  f"Percentage of tasks that are incomplete: {percentage_incomplete}%\n"
  f"Percentage of tasks overdue: {percentage_overdue}%")
  task_overview.close()

# view task overview report
def view_task_overview():
  task_stats = open("task_overview.txt", "r")
  task_stats.seek(0)
  task_stats_read = task_stats.read()
  task_stats_read = task_stats_read.split("\n")

  for line in range(len(task_stats_read)):
    print(task_stats_read[line])
  
  task_stats.close()

# user overview report
def user_report():

  # total number of users
  users_total = len(user_list_read)
  
  
  # total number of tasks generated and tracked
  tasks_total = len(task_list_read)

  
  # total number of tasks assigned to user
  user_task_counter = []
  # take each user, parse through the tasks and if the user matches assigned_user, add one
  for user in range(len(valid_users)):
    a = valid_users[user][0]
    number_of_tasks = 0
    
    # split each task into its components
    for task in range(len(task_list_read)):
      assigned_user, task_title, task_description, date_assigned, date_due, completed = task_list_read[task].split(", ")
      # if the assigned_user is the same as the user in this iteration, add one to number_of_tasks
      if a == assigned_user:
        number_of_tasks += 1
    
    # before moving onto the next user, append the username of this iteration and the number_of_tasks
    user_task_counter.append([a, number_of_tasks])  
    # sublist item 0 is the username, item 1 is the user task counter


  # percentage of all tasks assigned to user
  for user in range(len(user_task_counter)):
    task_percentage = round(user_task_counter[user][1]/tasks_total*100, 2)
    user_task_counter[user].append(task_percentage)
    # sublist item 2 is the percentage of all tasks assigned


  # percentage of tasks assigned to user that have been completed
  # iterate through users, iterate through tasks and if the task is complete and assigned to the uer add 1
  for user in range(len(user_task_counter)):
    user_completed_counter = 0
    
    for task in range(len(task_list_read)):
      assigned_user, task_title, task_description, date_assigned, date_due, completed = task_list_read[task].split(", ")
      
      if completed == 0 and assigned_user == user_task_counter[user]:
        user_completed_counter += 1
    
    completed_percentage = round(user_completed_counter/tasks_total*100, 2)
    user_task_counter[user].append(completed_percentage)
    # sublist item 3 is the percentage of tasks completed by the user


  # percentage of tasks assigned that are incomplete
  for user in range(len(user_task_counter)):
    incomplete_percentage = 100 - user_task_counter[user][3]
    user_task_counter[user].append(incomplete_percentage)
    # sublist item 4 is the percentage of items incomplete for the user

  
  # percentage of tasks overdue
  for user in range(len(user_task_counter)):
    user_overdue_counter = 0
    
    for task in range(len(task_list_read)):
      assigned_user, task_title, task_description, date_assigned, date_due, completed = task_list_read[task].split(", ")
      
      if assigned_user == user_task_counter[user] and date_due < date.today().strftime("%d %b %Y"):
        user_overdue_counter += 1
    
    overdue_percentage = round(user_overdue_counter/tasks_total*100, 2)
    user_task_counter[user].append(overdue_percentage)
    # sublist item 5 is the percentage of tasks overdue for the user
  
  
  # write text file report
  # take the relevant data relevant to the total tasks assigned to each user from user_task_counter
  l = ""
  tasks_assigned_to_user = ""
  for user in range(len(user_task_counter)):
     l = (f"{user_task_counter[user][0]}\n"
     f"Assigned tasks: {user_task_counter[user][1]}\n"
     f"Assigned % of all work to be done: {user_task_counter[user][2]}%\n"
     f"Tasks completed: {user_task_counter[user][3]}%\n"
     f"Tasks incomplete: {user_task_counter[user][4]}%\n"
     f"Tasks overdue: {user_task_counter[user][5]}%\n\n")
     tasks_assigned_to_user = tasks_assigned_to_user + l
  
  user_overview = open("user_overview.txt", "w")
  user_overview.write(f"User Overview Report\n"
  f"Total number of users: {users_total}\n"
  f"Total number of tasks generated and tracked: {tasks_total}\n\n"
  f"User Stats\n"
  f"{tasks_assigned_to_user}\n")
  user_overview.close()

# view user overview report
def view_user_overview():
  user_stats = open("user_overview.txt", "r")
  user_stats.seek(0)
  user_stats_read = user_stats.read()
  user_stats_read = user_stats_read.split("\n")
  
  for line in range(len(user_stats_read)):
    print(user_stats_read[line])
  
  user_stats.close()

#====Login Section====
# read the usernames and passwords with each user and their password as an item in a list
user_list = open("user.txt", "a+")
user_list.seek(0) # citation: https://stackoverflow.com/questions/14639936/how-to-read-from-file-opened-in-a-mode
user_list_read = user_list.read()
user_list_read = user_list_read.split("\n")

# store the usernames and passwords in a nested list
valid_users = []
for i in range(len(user_list_read)):
  valid_users.append(user_list_read[i].split(", "))


# read the task list file with each task being an item on the list
task_list = open("tasks.txt", "r+")
task_list.seek(0)
task_list_read = task_list.read()
task_list_read = task_list_read.split("\n")


# while loop to validate the username and password
validation_bool = True # create a switch to break the loop
while validation_bool:
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  
  for i in range(len(valid_users)):
    # if the username and password are correct as a pair, break the loops
    if username == valid_users[i][0] and password == valid_users[i][1]:
      print("Login successful\n")
      validation_bool = False
      break

    # if the username is correct but the password is not, tell the user
    elif username == valid_users[i][0] and password != valid_users[i][1]:
      print("The password you entered is incorrect\n")
    
    # when the username is not correct, tell the user
    else:
      print("The username you entered is not valid\n")


#=====Menu=====
while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    
  if username == "admin":
      menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my tasks
gr - Generate reports
s - Statistics
e - Exit
: ''').lower()

  else:
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my tasks
e - Exit
: ''').lower()


  if menu == 'r' and username == "admin":
    print("\nRegister a user\n")
    reg_user()


  elif menu == 'a':
    print("\nAdding a task\n")
    add_task()


  elif menu == 'va':
    print("\nView all tasks\n")
    view_all()


  elif menu == 'vm':
    print("\nView my tasks\n")
    view_mine()


  elif menu == "gr":
    task_overview_report()
    user_report()
    print("Reports generated: `user_overview.txt` and `task_overview.txt`\n")
  
  
  elif menu == "s":
    print("\nStatistics\n")
    view_task_overview()
    view_user_overview()

  
  elif menu == 'e':
      print('Goodbye!!!')
      
      # write to file - join tasks from list into a string then overwrite the task file with updated data and close
      task_list_new = "\n".join(task_list_read)
      task_list_file = open("tasks.txt", "w")
      task_list_file.write(task_list_new)
      task_list.close()
      task_list_file.close()
      
      # close user file
      user_list.close()
      
      # quit/end the programme
      exit()


  else:
      print("You have made a wrong choice, Please Try again")
