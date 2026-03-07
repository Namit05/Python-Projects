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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coins():
    print("Please insert coins")
    quarters = float(input("Enter the total quarters: "))
    dimes = float(input("Enter the total dimes: "))
    nickles = float(input("Enter the total nickles: "))
    pennies = float(input("Enter the total pennies: "))
    money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return money


def check_resources(user_choice):
    ingredients = MENU[user_choice]["ingredients"]

    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def update_resources(user_choice):
    ingredients = MENU[user_choice]["ingredients"]

    for item in ingredients:
        resources[item] -= ingredients[item]


run_machine = True

while run_machine:

    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        run_machine = False

    elif user_choice == "report":
        for key, value in resources.items():
            print(f"{key}: {value}")

    else:

        if check_resources(user_choice):

            Money = coins()

            if Money >= MENU[user_choice]["cost"]:
                change = round(Money - MENU[user_choice]["cost"], 2)
                if change>0 :
                    print(f"Here is ${change} in change.")
                update_resources(user_choice)
                print("Here you go! Enjoy ☕")
            else:
                print("Insufficient Amount!")
