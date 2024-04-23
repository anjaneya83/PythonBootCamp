#Write a program that calculates and outputs the number of characters in any name.
#The automated tests will try out lots of different names as the input. Your code should work for any name

name1= input("What is your name? ")
count_char=0
for char in name1:
    count_char=count_char+1
    print(char)
print(count_char)

num_char=len(name1)
print(num_char)