'''
You are going to write a program that will select a random name from a list of names. The person selected will have to pay
for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 1 splits the string names_string into individual names and puts them inside a List called names. For this to work, you
must enter all the names as names followed by comma then space. e.g. name, name, name

NOTE: Don't worry about getting hold of the input(), we've done the work behind the scenes to import everything.

HINT: Assume that names looks like this: input: x, y, z, names = ["x", "y", "z"]

Example Input
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!

'''
import random
print("Enter multiple names in format: Angela, Ben, Jenny")
names_string =input()
names= names_string.split(", ")
len_list= len(names)
random_index =random.randint(0,len_list-1)  #Return a number between 0 and len_list (both included)
#print(random_index)
print(f"{names[random_index]} is going to pay the bill")