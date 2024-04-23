'''
You are going to write a program that will mark a spot on a map with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what it looks like, notice the nesting:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']
Now it looks a bit more like the coordinates of a real map:

Your job is to write a program that allows you to mark a square on the map using a letter-number system.
First, your program must take the user input and convert it to a usable format.

Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
Example Input 1
B3
Example Output 1
Hiding your treasure! X marks the spot.
['⬜️', '️⬜️', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', 'X', '⬜️️']
'''

line1 = ["⬜️","⬜️","⬜️"]
line2 = ["⬜️","⬜️","⬜️"]
line3 = ["⬜️","⬜️","⬜️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
print(position[0])
index_row= int(position[1])-1
'''
tmp_index_col= position[0]
if tmp_index_col == "A":
    index_col=0
elif tmp_index_col == "B":
    index_col=1
elif tmp_index_col == "C":
    index_col=2
else:
    print("Invalid format entered")
'''
tmp_list=['A','B','C']
try:
    index_col= tmp_list.index(position[0])
    map[index_row][index_col]='X'
except ValueError:
    print("Only A, B, C are allowed")

print(f"{line1}\n{line2}\n{line3}\n")