MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

report = {
    "water": 1000,
    "milk": 500,
    "coffee": 200,
    "money": 25
}


def show_report():
    print(f"""
    Water: {report['water']}ml
    Milk: {report['milk']}ml
    Coffee: {report['coffee']}g
    Money: ${report['money']}
    """)


def check_resources(order):
    """Checks if there are sufficient resources in the machine.
    Continues to process coins if so."""
    for ingredient in MENU[order]['ingredients']:
        if MENU[order]['ingredients'][ingredient] > report[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
        else:
            process_coins(order)


def process_coins(order):
    """Checks if sufficient amount is paid. Refunds change if any.
    Continues to make coffee when order is paid"""
    cost = MENU[order]['cost']
    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    paid = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if paid < cost:
        print("Sorry that's not enough money. Money refunded.")
        coffee_machine()
    elif paid > cost:
        report["money"] += cost
        refund = "%.2f" % (paid - cost)
        print(f"Thank you! Here is ${refund} in change.")
        make_coffee(order)
    else:
        report["money"] += cost
        make_coffee(order)


def make_coffee(order):
    """Subtracts ingredients from the machine. Serves the order.
    Then restarts the process."""
    for ingredient in MENU[order]['ingredients']:
        report[ingredient] -= MENU[order]['ingredients'][ingredient]
    print(f"Here is your {order}. Enjoy! ☕")
    coffee_machine()


def coffee_machine():
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "espresso":
        check_resources(order)
    elif order == "latte":
        check_resources(order)
    elif order == "cappuccino":
        check_resources(order)
    elif order == "report":
        show_report()
        coffee_machine()
    elif order == "off":
        exit()
    else:
        print("Invalid input.")
        coffee_machine()


coffee_machine()
