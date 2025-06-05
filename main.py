# choice= input("what do you like? (espresso/latte/cappuccino): ")
# print(choice)

from resources_db import machine_resources as resources

def get_resources_report():
    print(f"water: {resources.get('water', ' ')}ml")
    print(f"milk: {resources.get('milk', ' ')}ml")
    print(f"water: {resources.get('water', ' ')}ml")
    print(f"water: {resources.get('water', ' ')}ml")

is_machine_on= True

while is_machine_on:
    choice= input("what do you like? (espresso/latte/cappuccino): ")
    if choice.lower() == "off":
        is_machine_on = False
    elif choice.lower() == "report":
        get_resources_report()