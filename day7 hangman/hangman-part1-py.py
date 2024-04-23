#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random
#now we pick an index using random funciton
chosen_word = random.choice(word_list)
print(type(chosen_word))
guess =input("Guess a letter: ").lower()
for ch in chosen_word:
    if guess == ch:
        print("right")
    else:
        print("wrong")