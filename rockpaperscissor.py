import random

choices = ["rock","paper","scissor"]

user_choice = input("enter your choice among rock paper and scissor: ")
comp_choice = random.choice(choices)

print(f"user choice = {user_choice} and compuer choice = {comp_choice}")

if(comp_choice == user_choice):
    print("Tie")

elif(comp_choice == rock && user_choice == scissor )||(comp_choice == paper && user_choice ==rock):
    print("Computer won")
