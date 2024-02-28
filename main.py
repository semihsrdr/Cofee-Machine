import time


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_on=True

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()



while turn_on:
    ordered_cofee=input("What would you like? (espresso/latte/cappuccino/):")

    if ordered_cofee.lower()=="off":
        turn_on=False
        print("The machine turning off. Please wait.")
        time.sleep(1)
        print("The machine turned off!")
        break
    elif ordered_cofee.lower()=="report":
        coffee_maker.report()
        money_machine.report()
    elif ordered_cofee.lower()=="refill":
        coffee_maker.refill_resources()
    else:
        drink=menu.find_drink(ordered_cofee.lower())
        if coffee_maker.is_resource_sufficient(drink):
            cost=drink.cost
            if money_machine.make_payment(cost):
                coffee_maker.make_coffee(drink)
