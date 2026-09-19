import random

choices = ["rock","paper","scissor"]

user_choice = input("enter your choice among rock paper and scissor: ").lower()
comp_choice = random.choice(choices)

print(f"Your choice = {user_choice} and computer choice = {comp_choice}")

if(comp_choice == user_choice):
    print("Tie")

elif(comp_choice == "rock" and user_choice == "scissor" ) or (comp_choice == "paper" and user_choice == "rock"):
    print("Computer won")
    
elif(user_choice == "rock" and comp_choice == "scissor" ) or (user_choice == "paper" and comp_choice == "rock"):
    print("You won")
else:
    print("invalid request try again")