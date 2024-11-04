from functions import *

is_on = True

while is_on:
    drink = input("“What would you like? (espresso/latte/cappuccino): ")

    if drink == 'off':
        is_on = False

    if drink == "report":
        show_report()
        continue

    coffee, water, milk, price_in_coins = get_info_drink(drink)
    if is_enough_ingredients(coffee, water, milk):
        subtract_ingredients(coffee, water, milk)

        amount_user_coins = ask_coins_and_give_amount_coins()
        change = get_change(amount_user_coins, price_in_coins)
        if change:
            money = change_money(price_in_coins)
            print(f"Here is your change: {change}")
            print(f"Here is your {drink} ☕ Enjoy!")
        else:
            print("Not enough money! Try again!")
    else:
        print(f"Not enough ingredients!")


