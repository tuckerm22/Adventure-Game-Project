'''This module contains 4 programs.

    Each program is executed three times with various random inputs
'''
#gamefunctions.py
#Mercedes Tucker
#03/4/25

#This code creates four functions, purchase_item, new_random_monster,
#print_welcome and print_shop_menu
#and calls them 3 times with 3 different inputs
# first defining and running purchase_item

import random

def purchase_item(itemPrice, startingMoney, quantityToPurchase):
    """"outputs money leftover given price and quanitiy of item as well as a starting amount
    paramters; itemPrice, starttng Money and quanitity to Purchase
    returns quanitity purchased and money leftover"""
    money_leftover = startingMoney - (quantityToPurchase * itemPrice)
    if money_leftover < 0:
        quantityToPurchase = 0 # Not enough money, return nothing
       
        return quantityToPurchase, startingMoney
    else:
        return quantityToPurchase, money_leftover # Enough money, return the remaining amount

#Now defining and running new_random_monster
import random

def new_random_monster():
    """"outputs a random monster based on random inputs from a given
    set of values
    returns: random monster with description, health, power and money"""
    monster_names = ["Goblin", "Dragon", "Vampire"]
    name = random.choice(monster_names)
    if name == "Goblin":
        health = random.randint(30, 50)
        power = random.randint(10, 20)
        money = random.randint(5, 15)
    elif name == "Dragon":
        health = random.randint(100, 200)
        power = random.randint(50, 80)
        money = random.randint(50, 100)
    elif name == "Vampire":
        health = random.randint(60, 100)
        power = random.randint(30, 50)
        money = random.randint(20, 40)
    monster = {
        "name": name,
        "description": f"A fearsome {name} lurking nearby.",
        "health": health,
        "power": power,
        "money": money
    }
    
    return monster

# Now defining and running print_welcome
def print_welcome(name, width = 20):
    """outputs a phrase Hello, name centered in a width of 20 given a name
    paramters; name, width= 20
    returns: phrase, Hello"""
    phrase = f' Hello, {name}!'
    phrase_aligned = f'{phrase:^{width}}'
    print(phrase_aligned)
# Lastly defining and running print_shop_menu
def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """outputs a shop menu given 2 items and their prices
    paramters: item1 name and Price, item2 name and price
    returns: menu with items and prices formatted in a 24 by 4 box """
    item1Price = f'${item1Price:.2f}' 
    item2Price = f'${item2Price:.2f}'
    first_item= f'| {item1Name:<12}{item1Price:>8} |'
    second_item= f'| {item2Name:<12}{item2Price:>8} |'
    first_item_centered = f'{first_item:^24}'
    second_item_centered = f'{second_item:^24}'
    print("/----------------------\\")
    print(first_item_centered)
    print(second_item_centered)
    print("\\----------------------/")
def test_functions():
    leftovermoney = purchase_item(round((random.random() * 10), 3),
                                  round((random.random() * 10), 3),
                                  round((random.randint(1, 10)), 3))
    leftovermoney2 = purchase_item(round((random.random() * 10), 3),
                                   round((random.random() * 10), 3),
                                   round((random.randint(1, 10)), 3))
    leftovermoney3 = purchase_item(round((random.random() * 10), 3),
                                   round((random.random() * 10), 3),
                                   round((random.randint(1, 10)), 3))
    print(leftovermoney)
    print(leftovermoney2)
    print(leftovermoney3)

    my_monster = new_random_monster()
    my_monster2 = new_random_monster()
    my_monster3 = new_random_monster()
    print(my_monster)
    print(my_monster2)
    print(my_monster3)

    print_welcome("John")
    print_welcome("Mercedes")
    print_welcome("Riley")

    print_shop_menu("Egg", .23, "Pear", 12.34)
    print_shop_menu("Bread", 5, "Apple", 1)
    print_shop_menu("Milk", 2, "Berries", 6)

if __name__ == "__main__":
    test_functions()

