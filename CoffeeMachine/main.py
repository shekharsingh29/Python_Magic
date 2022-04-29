# 1. Print report.
# 2. Check resources sufficient.
# 3. Process Coins.
# 4. Check Transaction Successful.
# 5. Make Coffee.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money_in_machine = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

want_coffee = True


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money_in_machine}")


def process_coins():
    print("Please insert coins. ")
    quarters = int(input("how many quarters?:"))
    pennies = int(input("how many pennies?:"))
    dimes = int(input("how many dimes?:"))
    nickels = int(input("how many nickels?:"))

    return 0.25*quarters + 0.05*nickels + 0.1*dimes + 0.01*pennies

def make_transaction(coffee_input, money_inserted):
    global money_in_machine
    if money_inserted >= MENU[coffee_input]["cost"]:
        money_in_machine = MENU[coffee_input]["cost"]
        print(f"Here is ${money_inserted - money_in_machine} in change.")
        return True
    else:
        return False

def make_coffee(cofee_input):
    resources["water"] = resources["water"]-MENU[coffee_input]["ingredients"]["water"]
    resources["milk"] = resources["milk"]-MENU[coffee_input]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"]-MENU[coffee_input]["ingredients"]["coffee"]
    print(f"Here is your {cofee_input} ☕️. Enjoy!")
    

while want_coffee:
    coffee_input = input("What would you like? (espresso/latte/cappuccino):")
    if coffee_input == 'off':
        want_coffee = False
    elif coffee_input == 'report':
        print_report()
    else:
        # Checking resources
        if MENU[coffee_input]["ingredients"]['milk'] <= resources["milk"]:
            if MENU[coffee_input]["ingredients"]['water'] <= resources["water"]:
                if MENU[coffee_input]["ingredients"]['coffee'] <= resources["coffee"]:
                    money_inserted = process_coins()

                    if make_transaction(coffee_input, money_inserted):
                        make_coffee(coffee_input)
                    else:
                        print("Sorry that's not enough money. Money refunded.​")
                else:
                    print(f"Sorry there is not enough coffee")
            else:   
                print(f"Sorry there is not enough water")
        else:
            print(f"Sorry there is not enough milk")
