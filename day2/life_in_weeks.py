#Create a program using maths and f-Strings that tells us how many weeks
#we have left, if we live until 90 years old. It will take your current age
#as the input and output a message with our time left in this format:
#You have x weeks left.
#Where x is replaced with the actual calculated number of weeks the input
#age has left until age 90.
current_age= int(input("Enter your age in years: "))
expected_age=90
age_left=expected_age-current_age
no_of_weeks=age_left*52
print(f"You have {no_of_weeks} weeks left.")