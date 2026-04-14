import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_images = [rock, paper, scissors]

my_choice= int(input("0 for Rock, 1 for Paper, 2 for Scissors: "))
if my_choice >=0 and my_choice<=2:
    print(game_images[my_choice])

computer_choice = random.randint(0,2)
print(f"computer choice {computer_choice}")
print(game_images[computer_choice])

if my_choice>=3 or my_choice<0:
    print("Invalid choice,You lose")
elif my_choice == 0 and computer_choice == 1:
    print("computer wins")
elif my_choice ==0 and computer_choice == 2:
    print("I win")
elif my_choice ==1 and computer_choice == 0:
    print("I win")
elif my_choice ==1 and computer_choice ==2:
    print("Computer wins")
elif my_choice ==2 and computer_choice == 0:
    print("Computer wins")
elif my_choice ==2 and computer_choice==1:
    print("I win")
elif my_choice == computer_choice:
    print("Draw")


