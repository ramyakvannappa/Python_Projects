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
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
if user_input >= 3 or user_input < 0:
    print("You provided an invalid input,you lose!")
else:
    print(game_images[user_input])

    computer_input = random.randint(0,2)
    print("Computer's choice : ")
    print(game_images[computer_input])

    #how to compare the two choice?
    #paper beats rock
    #scissors beats paper
    #rock beats scissors

    if user_input == 0 and computer_input == 2: # rock beats scissors
        print("You win!")
    elif computer_input == 0 and user_input == 2: # rock beats scissors
        print("You lose")
    elif computer_input > user_input: # scissors beats paper
        print("You lose")
    elif user_input > computer_input: # scissors beats paper
         print("You win")
    elif user_input == computer_input:
         print("It's a draw")
