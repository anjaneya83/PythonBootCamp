from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on = True
m = Menu()

cm = CoffeeMaker()
mm = MoneyMachine()
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    mi = m.find_drink(choice)
    print(choice, mi.name)
    if choice != mi.name:
        if choice == "off":
            print("Saayo Naara!!!")
            is_on = False
        else:
            print("Please enter a valid option")
    else:
        if cm.is_resource_sufficient(mi):
            amount_paid = mm.process_coins()
            if mm.make_payment(amount_paid):
                cm.make_coffee(mi)
