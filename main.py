from resource_data import *
from art import logo

coffee_again = True

while coffee_again:
    print(logo)
    print("Espresso - $1.5")
    print("Latte - $2.5")
    print("Cappuccino - $3")

    order = input("What would you like?\n")

    if order == "report":
        print(resources)
        break
    if order == "off":
        print("Coffee Machine Turned off")
        break
        
    if resources["water"] == 0 or resources["milk"] == 0 or resources["coffee"] == 0:
        print("Not working, since no resources found.")
        exit()

    amount = 0
    print("Please insert coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))
    total = round(((quarters*0.25) + (dimes*0.1) + (nickels*0.05) + (pennies*0.01)),2)

    if order == "espresso":
        if total < 1.5:
            print("That's not enough for Espresso")
        else:
            amount += 1.5
            if resources["water"] >= 50:
                if resources["coffee"] >= 18:
                        resources["water"] -= 50
                        resources["coffee"] -= 18
                        resources["money"] += 1.5
                        if total-amount > 0:
                            print(f"That is your change {round(total-amount)}")
                        print("Here is your espresso. Enjoy!  ☕")
                        print(resources)
            else:
                print("Not enough resources")            
        
    elif order == "latte":
        if total < 2.5:
            print("That's not enough for Latte")
        else:
            amount += 2.5
            if resources["water"] >= 200:
                if resources["milk"] >= 150:
                    if resources["coffee"] >= 24:
                        resources["water"] -= 200
                        resources["milk"] -= 150
                        resources["coffee"] -= 24
                        resources["money"] += 2.5
                        if total-amount > 0:
                            print(f"That is your change {round(total-amount)}")
                        print("Here is your latte. Enjoy! ☕")
                        print(resources)
            else:
                print("Not enough resources")
                
    elif order == "cappuccino":
        if total < 3:
            print("That's not enough for Cappuccino")
        else:
            amount += 3
            if resources["water"] >= 250: 
                if resources["milk"] >= 100:
                    if resources["coffee"] >= 24:
                        resources["water"] -= 250
                        resources["milk"] -= 100
                        resources["coffee"] -= 24
                        resources["money"] += 3
                        if total-amount > 0:
                            print(f"That is your change {round(total-amount)}")
                        print("Here is your cappuccino. Enjoy! ☕")
                        print(resources)
            else:
                print("Not enough resources")
               
    else:
        print("Sorry, we don't have that.'")
        break
        
