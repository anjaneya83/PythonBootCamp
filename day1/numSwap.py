#This program takes two inputs. The first input is stored in a variable called a. The second input is stored in a variable called b.
#Write a program that switches the values stored in the variables a and b.
a = int(input("Enter first number:" ))
b = int(input("Enter second number:" ))
temp_num = a
a = b
b= temp_num
print("a= "+str(a)+" b= "+str(b))