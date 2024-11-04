from menu import resources, MENU

def show_report():
    """Shows all available resources."""
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def process_coins():
    """Asks user type all the coins and returns full total"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes  + nickels + pennies
    return total


def get_info_drink(drink_name):
    """Takes drink name and returns all info about it"""
    coffee = MENU[drink_name]["ingredients"]["coffee"]
    water = MENU[drink_name]["ingredients"]["water"]
    milk = MENU[drink_name]["ingredients"]["milk"]
    price_drink = MENU[drink_name]["cost"]
    return coffee, water, milk, price_drink


def get_change(user_money, drink_price):
    """Takes user's money, checks if it is enough to buy a coffee"""
    if user_money >= drink_price:
        change = user_money - drink_price
        return f"${change:.2f}"
    return 0

def is_enough_ingredients(coffee, water, milk):
    """Checks whether enough ingredients in the coffee machine to make. Returns True or False"""
    res_coffee = resources["coffee"]
    res_water = resources["water"]
    res_milk = resources["milk"]

    if res_coffee >= coffee and res_water >= water and res_milk >= milk:
        return True

    return False


def subtract_ingredients(coffee, water, milk):
    """Subtracts available ingredients for making a coffee"""
    resources["coffee"] = resources.get("coffee") - coffee
    resources["water"] = resources.get("water") - water
    resources["milk"] = resources.get("milk") - milk


def take_money(user_money):
    """Takes user's money and sum it up."""
    resources['money'] += user_money