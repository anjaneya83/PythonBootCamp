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
game_options_print = [rock,paper,scissors]
game_choice_list= ["rock","paper","scissors"]
print("Welcome to the classic game of rock, paper and scissors")
user_choice = input("Type in your pick, in response the program will generate its  own pick at random:\n")
program_choice_index=random.randint(0,2)
program_choice = game_choice_list[program_choice_index]
try:
    get_user_index = game_choice_list.index(user_choice)
    print(f"You picked:\n {game_options_print[get_user_index]}")
    print(f"The program picked:\n{game_options_print[program_choice_index]}")
    if user_choice == program_choice:
        print("Its a Tie")
    else:
        if user_choice == "rock" and program_choice == "scissors":
            print("You Win")
        elif user_choice == "paper" and program_choice == "rock":
            print("You Win")
        elif user_choice == "scissors" and program_choice == "paper":
            print("You Win")
        else:
            print("You Loose. Better luck next time")
except ValueError:
    print(" Allowed values are rock, paper, scissors and they are case sensitive")

