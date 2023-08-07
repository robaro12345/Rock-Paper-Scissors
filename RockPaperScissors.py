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



ser_input =int(input("What would you like to chose? For rock type 0,Paper type 1 and Scissors type 2 "))
if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
elif user_input == 2:
    print(scissors)

print("Computers Choise")

computer_input = random.randint(0,2)
if computer_input == 0:
    print(rock)u
elif computer_input == 1:
    print(paper)
elif computer_input == 2:
    print(scissors)

if user_input == 0 and computer_input == 1:
    print("Computer Wins!")
elif user_input == 1 and computer_input == 2:
    print("Computer Wins")
elif user_input == 2 and computer_input == 0:
    print("Computer Wins")
elif computer_input == 0 and user_input == 1:
    print("User Wins")
elif computer_input == 1 and user_input == 2:
    print("User Wins")
elif computer_input == 2 and user_input == 0:
    print("User Wins")
else:
    print("Its a Draw")