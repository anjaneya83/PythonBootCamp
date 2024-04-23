from menu import MENU, resources
print("This is a coffee machine simulation")


# TODO 2. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
def print_report():
    for key in resources:
        if key == "water" or key == "milk":
            print(f" {key}: {resources[key]}ml")

        elif key == "coffee":
            print(f" {key}: {resources[key]}g")
        else:
            print(f"{key}: ${resources[key]}")


# TODO 3. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
def enough_milk(ch):
    if resources["milk"] - MENU[ch]["ingredients"]["milk"] > 0:
        return True
    else:
        return False


def enough_water(ch):
    if resources["water"] - MENU[ch]["ingredients"]["water"] > 0:
        return True
    else:
        return False


def enough_coffee(ch):
    if resources["coffee"] - MENU[ch]["ingredients"]["coffee"] > 0:
        return True
    else:
        return False


def check_resources(ch):

    if not enough_water(ch):
        print("Sorry there is not enough water left in the coffee machine to prepare {ch} for you")
        return False
    if not enough_coffee(ch):
        print("Sorry there is not enough coffee left in the coffee machine to prepare {choice} for you")
        return False
    if ch != "espresso":
        if not enough_milk(ch):
            print("Sorry there is not enough milk left in the coffee machine to prepare {ch} for you")
            return False
    print(f"All resources are in enough quantity to prepare {ch}")
    return True


# TODO 4. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
def collect_money():
    print("Please insert coins.")
    qu = int(input("how many quarters?: "))
    di = int(input("how many dimes?: "))
    ni = int(input("how many nickles?: "))
    pe = int(input("how many pennies?: "))
    total_money = qu*0.25+di*.1+ni*.05+pe*.01
    return total_money


# TODO 5. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places
def check_balance(am, ch):
    balance = am-MENU[ch]["cost"]
    if balance < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${balance} in change")
        resources["money"] += MENU[ch]["cost"]
        return True


# TODO 6. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink
def make_coffee(ch):
    resources["water"] -= MENU[ch]["ingredients"]["water"]
    resources["coffee"] -= MENU[ch]["ingredients"]["coffee"]
    if ch != "espresso":
        resources["milk"] -= MENU[ch]["ingredients"]["milk"]
    print_report()


# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):
# Check the user’s input to decide what to do next.
# The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
#  . Turn off the Coffee Machine by entering “off” to the prompt
valid_option = ["espresso", "latte", "cappuccino", "off", "report"]
choice = ""
money = 0
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice not in valid_option:
        print("Please enter a valid option")
    elif choice == "off":
        print("Saayo Naara!!!")
        is_on = False
    elif choice == "report":
        print_report()
    else:
        if check_resources(choice):
            amount_paid = collect_money()
            if check_balance(amount_paid, choice):
                make_coffee(choice)
