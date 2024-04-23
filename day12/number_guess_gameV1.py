#Number Guessing game
import random
from art import logo

def check_match(n,g):
    if g==n:
        print(f"You got it Dude!! The answer was {g}")
        return True
    elif g > n:
        print("It is higher than the number")
    else:
        print("It is lower than the number")
    return False

def play_game(num):
    
    guess=int(input("Make a Guess: "))
    outcome = check_match(num,guess)
    if outcome== True:
        return True
    else:     
        return False
print(logo)
number = random.randint(1,101)
print("Welcome to a number guessing game!!\nI'm thinking of a number between 1 and 100.")
level=input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == "easy":
    no_of_try = 10
else:
    no_of_try = 5
print(f"You have {no_of_try} attempts remaining to guess the number")
is_over = False
while is_over == False:
    
    is_matched = play_game(number)
    no_of_try-=1
    if is_matched == True:
        is_over = True
    elif no_of_try == 0:
        print(f"Pssst, the correct answer is {number}.\nYou've run out of guesses, you lose.")
        is_over = True
    else:
        print("Guess Again")
        print(f"You have {no_of_try} attempts remaining to guess the number")
 