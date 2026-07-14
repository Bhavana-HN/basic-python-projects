MENU={
    "tea":{
        "ingredients":{
            "water": 100,
            "tea_powder": 5,
            "milk": 50,
            "sugar": 8,
        },
        "cost": 30,
    },
    "coffee":{
        "ingredients":{
            "water": 50,
            "coffee_powder": 5,
            "milk": 100,
            "sugar": 8,
        },
        "cost": 20,
    },
    "masala_tea":{
        "ingredients":{
            "water": 80,
            "tea_powder": 5,
            "milk": 70,
            "sugar": 10,
            "spices": 5,
        },
        "cost": 40,
    },
    "filter_coffee":{
        "ingredients":{
            "water": 50,
            "coffee_powder": 5,
            "milk": 100,
            "sugar": 8,
        },
        "cost": 25
    }
}
profit=0
resources={
    "water": 500,
    "milk": 300,
    "tea_powder": 250,
    "coffee_powder": 200,
    "sugar": 400,
    "spices": 80
}
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many 10 rupee coins?: ")) * 10
    total += int(input("How many 5 rupee coins?: ")) * 5
    total += int(input("How many 2 rupee coins?: ")) * 2
    total += int(input("How many 1 rupee coins?: ")) * 1
    return total
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change} rupees in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

is_on=True
while is_on:
    choice=input("What would you like? (tea/coffee/masala_tea/filter_coffee): ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Tea Powder: {resources['tea_powder']}g")
        print(f"Coffee Powder: {resources['coffee_powder']}g")
        print(f"Sugar: {resources['sugar']}g")
        print(f"Spices: {resources['spices']}g")
        print(f"Money: {profit} rupees")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                for item in drink["ingredients"]:
                    resources[item]-=drink["ingredients"][item]
                print(f"Here is your {choice}. Enjoy!")