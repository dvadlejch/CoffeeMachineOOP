from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from sys import exit

# espresso = MenuItem("espresso", 50, 0, 18, 1.5)
# latte = MenuItem("latte", 200, 250, 24, 2.5)
# cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)
Machine = CoffeeMaker()
Menu_inst = Menu()
Money = MoneyMachine()

def main_func():
    try:
        choice = str(input("What would you like? ")).lower()
    except ValueError:
        print("Unknown command, try again!")
        main_func()

    if choice == "off":
        print("Turning off!")
        exit()

    if choice == "report":
        Machine.report()
        main_func()

    if choice == "money":
        Money.report()
        main_func()

    if choice not in [Menu_inst.menu[i].name for i in range(len(Menu_inst.menu))]:
        print("Unknown command, try again!")
        main_func()

    else:
        drink = Menu_inst.find_drink(choice)
        if Machine.is_resource_sufficient(drink):
            if Money.make_payment(drink.cost):
                Machine.make_coffee(drink)

            main_func()
        else:
            main_func()


main_func()
