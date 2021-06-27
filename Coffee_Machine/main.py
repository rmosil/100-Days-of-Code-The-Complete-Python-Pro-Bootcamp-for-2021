from art import logo
from data import MENU


def payment():
    """Calculates the payment"""
    print("")
    print("Please insert coins")
    quarter = int(input("How many quarters: "))
    total_quarter = quarter * 0.25
    sub_total = total_quarter
    if sub_total == MENU[order]["cost"] or sub_total >= MENU[order]["cost"]:
        return sub_total

    elif sub_total <= MENU[order]["cost"]:
        dime = int(input("How many dimes: "))
        total_dimes = dime * 0.1
        sub_total = sub_total + total_dimes

        if sub_total == MENU[order]["cost"] or sub_total >= MENU[order]["cost"]:
            return sub_total

        elif sub_total <= MENU[order]["cost"]:
            nickel = int(input("How many nickles: "))
            total_nickles = nickel * 0.05
            sub_total = sub_total + total_nickles

            if sub_total == MENU[order]["cost"] or sub_total >= MENU[order]["cost"]:
                return sub_total

            elif sub_total <= MENU[order]["cost"]:
                penny = int(input("How many pennies: "))
                total_pennies = penny * 0.01
                sub_total = sub_total + total_pennies
                return sub_total


def report_update():
    """Updates the ingredients and money report"""
    resources["water"] = resources["water"] - MENU[order]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[order]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[order]["ingredients"]["coffee"]
    resources["money"] = resources["money"] + total


print(logo)
turn_on = True

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0.00}

while turn_on:

    print("")
    order = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

    while order != "espresso" and order != "latte" and order != "cappuccino" and order != "report":
        print("Invalid option! Try again")
        order = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

    if order == "report":
        print("")
        print("Water: {}ml.".format(resources["water"]))
        print("Milk: {}ml.".format(resources["milk"]))
        print("Coffee: {}g.".format(resources["coffee"]))
        print("Money: ${:.2f}.".format(resources["money"]))

    else:

        if resources["water"] >= MENU[order]["ingredients"]["water"] \
                and resources["milk"] >= MENU[order]["ingredients"]["milk"] \
                and resources["coffee"] >= MENU[order]["ingredients"]["coffee"]:

            print("The {} costs ${:.2f}.".format(order, MENU[order]["cost"]))
            total = payment()

            if total == MENU[order]["cost"]:
                print("Here is your {}. Enjoy!".format(order))
                report_update()

            elif total >= MENU[order]["cost"]:
                change = total - MENU[order]["cost"]
                total -= change
                print("Here is ${:.2f} in change.".format(change))
                print("Here is your {}. Enjoy!".format(order))
                report_update()

            elif total < MENU[order]["cost"]:
                print(total)
                print("Sorry! That is not enough money. Payment refunded")

        else:
            print("Sorry! Not enough ingredients.")
            break

    power = input("Turn off the coffee machine? Type \"yes\" or \"no\": ").lower().strip()
    if power == "yes":
        turn_on = False
