from pip._internal.index import sources

from menu import resources, MENU
# from main import money

def show_report():
    """Shows all available resources."""
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: {money}")


def ask_coins_and_give_amount_coins():
    """Asks user type all the coins and returns full amount coins"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_coins = (quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01) * 100
    return total_coins


def get_info_drink(drink_name):
    """Takes drink name and returns all info about it"""
    coffee = MENU[drink_name]["ingredients"]["coffee"]
    water = MENU[drink_name]["ingredients"]["water"]
    milk = MENU[drink_name]["ingredients"]["milk"]
    price_in_coins = MENU[drink_name]["cost"] * 100
    return coffee, water, milk, price_in_coins


def get_change(user_coins, price_in_coins):
    """Takes total coins, converts it into dollars and coin amounts and return a readable string"""
    if user_coins >= price_in_coins:
        change = user_coins - price_in_coins
        dollars_change = int(change // 100)
        coins_change = int(change % 100)
        return f"${dollars_change}.{coins_change}"
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


def change_money(new_coins):
    """Takes new amount of coins. Calculates them and changes the value in the resource's dictionary ."""
    money = resources["money"]
    money = money.lstrip('$')
    dollars, coins = map(int, money.split('.'))
    new_dollars = int(new_coins // 100) + dollars
    new_coins = int(new_coins % 100) + coins
    resources['money'] = f"${new_dollars}.{new_coins}"