"""
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2

Add pepperoni for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1
"""
print("Thank you for choosing Python pizza deliveries!")
size = input("What size of pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N :")

cost = 0
if size == "S" :
    cost= 15
    if add_pepperoni == "Y":
        cost += 2
    if extra_cheese == "Y":
        cost += 1
elif size == "M" :
    cost = 20
    if add_pepperoni == "Y":
        cost += 3
    if extra_cheese == "Y":
        cost += 1
elif size == "L" :
    cost = 25
    if add_pepperoni == "Y":
        cost += 3
    if extra_cheese == "Y":
        cost += 1
else:
    print("invalid choice")

print(f"Your final bill is: ${cost}.")