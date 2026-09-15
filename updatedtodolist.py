def write():
    with open("task.txt","w") as file:
        file.write(input("Enter The tasks You need to complete: "+ "\n"))

def read():
    with open("task.txt","r") as file:
        data = file.read()

def delete():
    with open("task.txt", "r") as file:
        tasks = file.readlines()

    for i, task in enumerate(tasks, 1):
       print(i, task.strip())

    number = int(input("Which task is completed? "))

    tasks.pop(number - 1)

    with open("task.txt", "w") as file:
         file.writelines(tasks)
