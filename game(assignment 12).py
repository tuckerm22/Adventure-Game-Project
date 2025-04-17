from gamefunctions import *
import random
import json
import pygame
import math
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
inventory = {}
filename = "game.json"
save_or_resume = input("Pick one, Start new game or load previous game: ")

def getUserFightOptions():
    while True:
        print("Keep fighting or run away?")
        print("What would you like to do?")
        print("1) Keep fighting")
        print("2) Run away")
        
        selection = input("Enter your choice (1 or 2): ")
        if selection in ['1', '2']:
            return selection  
        else:
            print('Not a valid input, please try again from selection 1 or 2')

def displayFightStatistics(monster):
    global current_hp
    print("me: health = {}".format(current_hp))
    print("monster: health = {}".format(monster["health"]))

def pick_item():
    global current_gold
    shop_items = [
        {"price": 5, "name": "sword", "type": "weapon", "maxDurability": 10, "currentDurability": 10},
        {"price": 1, "name": "Armour", "type": "shield", "maxDurability": 5, "currentDurability": 5}
    ]
    
    selection = input("Enter a choice, weapon or shield: ")
    if selection == "weapon":
        item = shop_items[0]
        print(f"Item details: {item}") 
        if current_gold >= item["price"]:
            inventory["weapon"] = item
            current_gold -= item["price"]
            print(f"You have bought: {inventory['weapon']['name']}")
            print(f"Remaining gold: {current_gold}")
        else:
            print("You do not have enough gold to buy this item.")
    elif selection == "shield":
        item = shop_items[1]
        if current_gold >= item["price"]:
            inventory["shield"] = item
            current_gold -= item["price"]
            print(f"You have bought: {inventory['shield']['name']}")
            print(f"Remaining gold: {current_gold}")
        else:
            print("You do not have enough gold to buy this item.")
    else:
        print("Invalid selection. Please choose either 'weapon' or 'shield'.")

def fight_monster():
    global current_hp
    global current_gold
    if current_hp <= 0:
        print("Not enough health to fight")
        return
    monster = new_random_monster()
    mydamage = monster["power"]
    print("You are fighting a {}!".format(monster["name"]))
    
    if current_gold >= 0:
        pick_item()
    
    while True:
        if "weapon" in inventory:
            weapondamage = inventory["weapon"]["currentDurability"]
            if weapondamage > 0:
                monster["health"] -= weapondamage
                inventory["weapon"]["currentDurability"] -= 1  # Decrease weapon durability
            else:
                print(f'Not enough Durability to use weapon')
                break
        else:
            print("You have no weapon to fight with!")
            break
        
        if monster["health"] <= 0:
            print("You killed a {}!".format(monster["name"]))
            return
        
        current_hp -= mydamage
        if current_hp <= 0:
            print("You died fighting a {}!".format(monster["name"]))
            return
        
        displayFightStatistics(monster)
        choice = getUserFightOptions()
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
                print(f"Restored 10 HP. Current HP: {current_hp}")
            else:
                print("You do not have enough gold to sleep")
        elif selection == '3':
            break
        else:
            print('Not a valid input, please try again from selections 1, 2 and 3')
if save_or_resume == "load previous game":
    with open(filename, 'r') as file:
        game_data = json.load(file)
        current_hp = game_data.get("current_hp", MAX_HEALTH)
        current_gold = game_data.get("current_gold", 10)
        inventory = game_data.get("inventory", {})
        print("Game data loaded successfully:")
        pick_game()
    
pick_game()
game = {
    "current_hp": current_hp,
    "current_gold": current_gold,
    "inventory": inventory
}
with open(filename, 'w') as file:
    json.dump(game,file)
print(f'Data saved to {filename}')
def circle_rect_collision(circle, rect):
    """
    Checks if a circle and a rectangle are colliding.

    Args:
        circle: A tuple (x, y, radius) representing the circle.
        rect: A pygame.Rect object representing the rectangle.

    Returns:
        True if the circle and rectangle are colliding, False otherwise.
    """
    circle_x, circle_y, circle_radius = circle

    # Find the closest point on the rectangle to the circle's center
    closest_x = max(rect.left, min(circle_x, rect.right))
    closest_y = max(rect.top, min(circle_y, rect.bottom))

    # Calculate the distance between the closest point and the circle's center
    distance_x = circle_x - closest_x
    distance_y = circle_y - closest_y
    distance_squared = distance_x**2 + distance_y**2

    # Check if the distance is less than the circle's radius squared
    return distance_squared <= circle_radius**2


pygame.init()
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
window = pygame.display.set_mode(((320, 320)))

x, y = 295, 145
width, height = 10, 10
vel = 1
gameExit = False
window.fill((0, 0, 0))
pygame.draw.circle(window, green ,(300,150),10,width=0)
pygame.draw.circle(window, red ,(110,150),10,width=0) 
pygame.draw.rect(window, white , (x, y, width, height))
green_circle = (300,150,10)
red_circle = (105,150,10)
pygame.display.update()

while not gameExit:
    new_x = x
    new_y = y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
        if event.type == pygame.KEYDOWN:
            we_fight_monster = True
            if event.key == pygame.K_LEFT:
                new_x -= 32
            elif event.key == pygame.K_RIGHT:
                new_x += 32
            elif event.key == pygame.K_UP:
                new_y -= 32
            elif event.key == pygame.K_DOWN:
                new_y += 32
            elif event.key == pygame.K_SPACE:
                gameExit = True

            if new_x < 320 and new_x > 0 or new_y < 320 or new_y > 0:
                x = new_x
                y = new_y
                window.fill((0, 0, 0))
                pygame.draw.circle(window, green ,(300,150),10,width=0)
                pygame.draw.circle(window, red ,(110,150),10,width=0)
                pygame.draw.rect(window, white , (x, y, width, height))
                pygame.display.update()
                rect = pygame.Rect(x,y,width,height)

                if circle_rect_collision(green_circle, rect):
                    gameExit = True
                elif circle_rect_collision(red_circle, rect):
                    if we_fight_monster:
                        pygame.quit()
                        fight_monster()
                        if current_hp <= 0:
                            gameExit = True
                            break
                        pygame.init()
                        window = pygame.display.set_mode(((320, 320)))
                        window.fill((0, 0, 0))
                        pygame.draw.circle(window, green ,(300,150),10,width=0)
                        pygame.draw.circle(window, red ,(110,150),10,width=0) 
                        pygame.draw.rect(window, white , (x, y, width, height))
                        pygame.display.update()
                        we_fight_monster = False   
pygame.quit()









        
    





