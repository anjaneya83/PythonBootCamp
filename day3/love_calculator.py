"""
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

These functions will help you:
lower() count()
"""
print("Welcome to Love calculator. It shall predict how much love is their between you and you partner")
name1 = input("Write your full name: ").lower()
name2 = input("Write your partner's name: ").lower()
print(f" You have entered {name1} and {name2}")
score1 = 0
combined_name= name1+name2
score1= combined_name.count("t")
score1+= combined_name.count("r")
score1+= combined_name.count("u")
score1+= combined_name.count("e")

score2 = combined_name.count("l")
score2 += combined_name.count("o")
score2 += combined_name.count("v")
score2 += combined_name.count("e")
love_score=score1*10+score2
if love_score <10 or love_score >90:
    print(f"You go together like coke and mentos.")
elif love_score >39 and love_score <51:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}.")