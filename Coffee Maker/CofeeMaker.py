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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    'money' : 0
}





# The user will Input their cash here
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
# The Report is a special command for the owner that shows what left and how much money is made
def report():
    for item in resources:
        print(item, ':', resources[item])
# This check first if there is enough resources
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'There Is not enough {item}')
            return True
            

# This checks if they have enough
def price_check(price, drink_name):    
        
    change = total - price
    if change < 0:
        print(f' Sorry thats not enough money. Money refunded. You would of owed ${round(change, 3)} more')
    else:
        print('Your change is $', round(change, 3))
        print(f"Here is your {drink_name} ☕️. Enjoy!")
        resources['money'] += price
        usage(drink['ingredients'])        


#This Subtracts the Reources that was used from the Oringnal
def usage(item_used):
    for cost in item_used:
        resources[cost] -= item_used[cost]
        print(f'{cost} : {resources[cost]} ')



while True:
    choice = input('Would you like espresso/latte/cappuccino)')
    

    if choice == "off":
        break  
    elif choice == 'report':
        report()
    else:
        drink = MENU[choice] 
        if is_resource_sufficient(drink['ingredients']): # This check first if there is enough resources
            break
        else:
            total = process_coins() # The user will Input their cash here
            price_check(drink['cost'], choice) # This checks if the user have enough cash












