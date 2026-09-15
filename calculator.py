def sum(a,b):
    return a+b

def sub(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divison (a,b):
    if (b ==0):
        print("Error cannot divide by 0")

    else:
        return a/b

a = int(input("Enter a number: "))
operator=input("Enter an operator: ")
b = int (input("Enter another number: "))

if (operator == "+"):
    result = sum(a,b)
    print(result)

elif(operator == "-"):
    result = sub(a,b)
    print(result)

elif(operator == "*"):
    result =  multiply(a,b)
    print(result)

elif(operator == "/"):
    result = divison(a,b)
    print(result)

else:
    print("Enter a valid operator")