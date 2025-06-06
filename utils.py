from resources_db import machine_resources as resources
from resources_db import COFFEE_MENU

def get_resources_report():
    print(f"water: {resources.get('water', ' ')}ml")
    print(f"milk: {resources.get('milk', ' ')}ml")
    print(f"water: {resources.get('water', ' ')}ml")
    print(f"water: {resources.get('water', ' ')}ml")

def is_resources_sufficient(choice):
    is_resources_suff = True
    for ingred, qty in COFFEE_MENU.get(choice, {}).get("ingredients", {}).items():
        if resources.get(ingred, 0) < qty:
            print(f"we dont have enough {ingred}!!! Try another coffee.")
            is_resources_sufficient = False

    return is_resources_suff