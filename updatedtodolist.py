def write():
    with open("task.txt","a") as file:
        file.write(input("Enter The tasks You need to complete: "+ "\n"))


def read():
    with open("task.txt","r") as file:
        data = file.read()
        print(data)


def delete():
    with open("task.txt", "r") as file:
        tasks = file.readlines()



    for i, task in enumerate(tasks, 1):
       print(i, task.strip())

       

    number = int(input("Which task is completed? "))

    tasks.pop(number - 1)

    with open("task.txt", "w") as file:
         file.writelines(tasks)

    with open ("task.txt","r") as file:
        data = file.read()
        print("\n Remaining tasks are \n"+data)

while True: # type: ignore
    choice = int(input("Enter what you want to do (1 for adding task , 2 for watching the remaining task , 3 for deleting the done task 4 for exit): "))
    
    if(choice == 4):
        break

    elif choice == 1:
       write()

    elif choice == 2:
       read()

    elif choice ==3:
        delete()


    else:
        print("Invalid input")