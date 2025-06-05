# choice= input("what do you like? (espresso/latte/cappuccino): ")
# print(choice)

is_machine_on= True

while is_machine_on:
    choice= input("what do you like? (espresso/latte/cappuccino): ")
    if choice.lower() == "off":
        is_machine_on = False