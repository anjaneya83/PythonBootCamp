#Write a program that works out whether if a given number is an odd or even number.
number = int(input("enter any number: "))
if number%2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")