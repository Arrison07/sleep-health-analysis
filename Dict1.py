# 1. WAP to create following structure
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
#Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, 
# {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}

color_name= ["Black", "Red", "Maroon", "Yellow"]
color_code= ["#000000", "#FF0000", "#800000", "#FFFF00"]

structure = []

for name, code in zip(color_name, color_code):
    structure.append({"color_name": name, "color_code": code})

print(structure)

# 2 Make a rock paper scissor game with score counter
#winning cases
# rock wins scissor
# paper wins rock
# scissor wins paper

import random

player = 0
computer = 0

while True:
    user_choice = input("rock, paper, scissor or exit: ").lower()
    if user_choice == "exit":
        break
    if user_choice not in ["rock", "paper", "scissor"]:
        print("Invalid option")
        continue

    comp_choice = random.choice(["rock", "paper", "scissor"])

    if user_choice == comp_choice:
        print("Tie!\n")
    elif (user_choice == "rock" and comp_choice == "scissor") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissor" and comp_choice == "paper"):
        print("You win")
        player += 1
    elif(comp_choice == "rock" and user_choice == "scissor") or \
         (comp_choice == "paper" and user_choice == "rock") or \
         (comp_choice == "scissor" and user_choice == "paper"):
        print("Computer wins")
        computer += 1
    else:
        print("Try  again")

    print("Computer chose:", comp_choice)
    print("Score → Player:", player, "| Computer:", computer, "\n")

