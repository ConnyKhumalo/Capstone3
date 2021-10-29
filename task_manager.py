from datetime import date
#User.txt stores the username and password for each user that has permission to use your program
#The username and password for each user must be written to this file in the following format:
users = {}
#The username followed by a comma,a space and then the password
#One username and corresponding password per line
with open("user.txt","r") as username:
    for line in username:
        username, password = line.split(",")
        users[username.strip()] = password.strip()#Strip removes leading whitespaces
#Program should allow users to do the following:
#Login,user should be asked to enter a username and a password
uinput = input("Please enter your username: ")
while uinput not in users:
    print("Username incorrect.")
    uinput = input("Please enter a valid username: ")

if uinput in users:
    print("The username entered is correct")

with open("user.txt","r") as password:
    for line in password:
        username, password = line.split(",")
        users[password.strip()] = password.strip()
#A list of valid usernames and passwords are stored in a text file called user.txt
password = input("Please enter your password: ")
while password not in users:
    print("Your username is correct but your password is incorrect.")
    password = input("Please enter a valid password: ")
#Once user has successfully logged  in a menu will be displayed
if password in users:
    print("Password   correct")
#If the user chooses 'r' to register a user , the user should be asked to confirm the passwor.
#If the value entered to confirm the password matches the value of the password,the username and password should be written to user.txt in the appropriate format.
    if uinput == "admin":
        menu = (input("\nPlease select one of the following options:\nr - register user\na - add task\nva - view all tasks\nvm - view my task\nd- display statistics = Total number of tasks and users\ne - exit\n"))
    else:
        menu = (input("\nPlease select one of the following options:\na - add task\nva - view all tasks\nvm - view my task\ne - exit\n"))
   
if menu == "r" and uinput == "admin":
       
    new_user = (input("Please enter a new user name: "))
    new_user_password = (input("Please enter a new password: "))
                           
    new_password = False

    while new_password == False:
        confirm_new_password = input("Please retype your password just for confirmation: ")

        if new_user_password == confirm_new_password:
            new_password = True
                                   
        elif new_password == False:
            print("Your passwords do not match!")
                                    
        
    with open("user.txt","a") as username:
        username.write("\n" + new_user + "," + new_user_password)
        print("You have been registered")
                

#If the user chooses 'a' to add a  task ,the user should be asked to enter the username of the person the task is assigned to.
#The title of the task ,a description of the task and the due date of the task.
#The data about the new task should be written to tasks.txt.
            
elif menu == "a":
    
    name = input("Please enter the username of the person the task is assigned to.\n")
    while name not in username:
        name = input("Username not registered.Please enter a valid username.\n")
    else:
        task_title = input("Please enter the title of the task.\n")
        task_description = input("Please enter the task description.\n")
        task_due = input("Please enter due date of the task. (yyyy-mm-dd)\n")
        date = date.today()
        task_completed = False
        if task_completed == False:
            task_completed = "No"
        else:
            task_completed = ("Yes")
        with open("tasks.txt","a+")  as task:
            task.write("\n{}, {}, {}, {}, {}, {}".format(str(name), str(task_title), str(task_description), str(task_due), str(date), str(task_completed)))
            print("Task has been added")
            
#If the user chooses 'va' to view alltasks,displayed information for each task wiil be on the screen in an easy to read format'.
elif menu == "va":
    
    all_tasks = open("tasks.txt","r")
    text = all_tasks.readlines()
    for line in text:
        text =  line.split(",")
        print(f"""

Task: {text[1]}
Assinged to: {text[0]}
Date assigned: {text[3]}
Due date: {text[4]}
Task Complete? {text[5]}
Task description: {text[2]}

""")
            
        all_tasks.close()
        
#If the user  chooses 'vm' to view the tasks that are assigned to them,only display all the tasks that have been assigned to the user that is currently logged in.
elif menu == "vm":
    
    with open("tasks.txt","r") as fl:
        data = fl.readlines()
        for line in data:
            data = line.split(",")
            if uinput == data[0] :
                print(f"""

Task: {data[1]}
Assigned to:{data[0]} 
Date assigned: {data[3]}
Due date: {data[4]} 
Task Complete? {data[5]} 
Task description:{data[2]} 

""")
                
            fl.close()

elif menu == "d" and uinput == "admin":
#These variables will only count the lines inside the "txt" files.
#but since I'll be storing every new task and user on a new line.
#we can just count the lines for the desired results
    tasks_num = 0
    users_num = 0
    
    with open("tasks.txt","r") as file:
        for line in file:
                tasks_num += 1
    print(f"\nThe total number of tasks: {tasks_num}")

    with open("user.txt","r") as username:
        for line in username:
                users_num+= 1
    print(f"\nThe total number of users: {users_num}")
          
elif menu == "e":
    exit







       





            







            
