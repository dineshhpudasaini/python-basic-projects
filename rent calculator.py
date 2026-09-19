rent = int(input("Enter your rent: "))
food = int(input("Enter the amount of food ordered: "))
electricity = int(input("Enter the total of electricity spend: "))
chargeperunit= int(input("Enter  the charge per unit: "))
persons= int(input("Enter the number of persons living in the room: "))

total_bill = electricity * chargeperunit 
output = (food + rent + total_bill) // persons
print("Each person will pay " , output)