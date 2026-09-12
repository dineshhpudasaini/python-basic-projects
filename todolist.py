print("To Do List")

task = input("Enter What You Want To Do : w for Write and r for Read : ")

try:
    if(task =="r"):
        with open ("task.txt","r") as file :
             data = file.read()
             print(data + "\n")

    elif(task == "w"):
        with open("task.txt","a") as file : 
            file.write(input("Enter the task: "+ "\n"))

    else:
        print("Invalid Input")
except:
    print("Error")
