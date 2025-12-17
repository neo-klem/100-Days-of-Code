import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

the_list = [rock,paper,scissors]

player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for scissors. \n"))
player_choice = the_list[player_input]

computer_input = random.randint(0, 2)
computer_choice = the_list[computer_input]
                           
if player_input == computer_input:
    print(f"{player_choice}\nComputer choose:\n{computer_choice}\n DRAW!")
elif player_input == 0 and computer_input == 2:
    print(f"{player_choice}\nComputer choose:\n{computer_choice}\n YOU WIN!")
elif player_input == 2 and computer_input == 1:
    print(f"{player_choice}\nComputer choose:\n{computer_choice}\n YOU WIN!")
elif player_input == 1 and computer_input == 0:
    print(f"{player_choice}\nComputer choose:\n{computer_choice}\n YOU WIN!")
else:
    print(f"{player_choice}\nComputer choose:\n{computer_choice}\n YOU LOOSE!")


