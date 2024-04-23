#Write a program that calculates the Body Mass Index (BMI)
#from a user's weight and height.The BMI is calculated by dividing
#a person's weight (in kg) by the square of their height (in m):
height=float(input("Enter your height in meters"))
weight=float(input("Enter your weight in KG"))
bmi=weight/(height**2)
#print(int(bmi))
print(round(bmi,2)  #round to two decimal places