from gamefunctions import *
import random

'''
leftovermoney = purchase_item(round((random.random() * 10), 3),
                                  round((random.random() * 10), 3),
                                  round((random.randint(1, 10)), 3))
print(leftovermoney)   
my_monster = new_random_monster()
print(my_monster)
print_welcome("John")
print_shop_menu("Egg", .23, "Pear", 12.34)
'''
    
MAX_HEALTH = 100
current_hp = MAX_HEALTH
current_gold = 10   


def getUserFightOptions():
    
    while True:
        print("Keep fighting or run away?")
        print("What would you like to do?")
        print("1) Keeo fighting")
        print("2) Run away")
        
        selection = input("Enter your choice (1 or 2): ")
        if selection == '1'or selection == '2':
            return selection  
        else:
            print('Not a valid input, please try again from selection 1 or 2')

def displayFightStatistics(monster):
    global current_hp
    print("me: health = {}".format(current_hp))
    print("monster: health = {}".format(monster["health"]))
          

def fight_monster():

    global current_hp
    global current_gold

    if current_hp <= 0:
        print("not enough health to fight")
        return

    monster = new_random_monster()
    mydamage = monster["power"]
    
    print("you are fighting a {}!".format(monster["name"]))

    while True:

        monsterdamage = random.randint(5,30)

        monster["health"] -= monsterdamage
        if monster["health"] <= 0:
            print("you killed a {}!".format(monster["name"]))
            return
        current_hp -= mydamage
        if current_hp <=0:
            print("you died fighting a {}!".format(monster["name"]))
            return
        displayFightStatistics(monster)
        choice = getUserFightOption()
        if choice == '2':
            break

def pick_game():

    global current_hp
    global current_gold

    while True:
        print("You are in town.")
        print(f"Current HP: {current_hp}, Current Gold: {current_gold}")
        print("What would you like to do?")
        print("1) Leave town (Fight Monster)")
        print("2) Sleep (Restore HP for 5 Gold)")
        print("3) Quit")
        
        selection = input("Enter your choice (1, 2, or 3): ")
        if selection == '1':
            fight_monster()
        elif selection == '2':
            if current_gold >= 5:
                current_gold -= 5
                current_hp += 10
                if current_hp > MAX_HEALTH:
                    current_hp = MAX_HEALTH
            else:
                print("You do not have enough gold to sleep")
                    

        elif selection == '3':
            break
            
        else:
            print('Not a valid input, please try again from selections 1, 2 and 3')

pick_game()

        
    





