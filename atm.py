user_data = {
    "name": "Dinesh",
    "pin": 1234,
    "balance": 1000
}
pin = int(input("Enter your pin: "))

if(user_data["pin"] == pin):

    def balance():
        print("Your balance is " ,user_data["balance"])

    def diposit():
        diposit = int(input("Enter The amount you want to diposit: "))

        if(diposit > 0):
            user_data["balance"] = user_data["balance"]+ diposit
            print("Successfully Diposited \n Your new balance is ",user_data["balance"])

        else:
            print("Enter valid amount")

    def withdraw():
        withdraw = int(input("Enter the amount you want to withdraw: "))

        if(withdraw < user_data["balance"] and withdraw > 0):
           user_data["balance"] = user_data["balance"] - withdraw
           print("money withdrawn successfully \n Your balance after withdraw is " ,user_data["balance"])

        else:
            print("Invalid input")
           
           
    user_input=int(input("Enter 1 for balance inquiry , 2 for diposit and 3 for withdraw amount: "))

    if(user_input == 1):
       balance()
    
    elif(user_input == 2):
        diposit()
    
    elif(user_input == 3):
         withdraw()
            
else:
    print("Invalid Pin")