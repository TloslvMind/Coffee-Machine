from functions import *

is_on = True

while is_on:
    drink = input("“What would you like? (espresso/latte/cappuccino): ")

    if drink == 'off':
        is_on = False
    elif drink == "report":
        show_report()
    else:
        coffee, water, milk, price_drink = get_info_drink(drink)
        if is_enough_ingredients(coffee, water, milk):
            user_money = process_coins()
            change = get_change(user_money, price_drink)
            if change:
                subtract_ingredients(coffee, water, milk)
                take_money(price_drink)
                print(f"Here is your change: {change}")
                print(f"Here is your {drink} ☕ Enjoy!")
            else:
                print("Not enough money! Money refunded! Try again!")
        else:
            print(f"Not enough ingredients!")


