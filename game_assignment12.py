from gamefunctions import *
from wanderingMonster import WanderingMonster
import random
import json
import pygame

# Constants
MAX_HEALTH = 100
current_hp = MAX_HEALTH
current_gold = 10   
inventory = {}
filename = "game.json"

# Initialize Pygame
pygame.init()

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

# Window setup
window = pygame.display.set_mode((320, 320))

# Player setup
x, y = 295, 145
width, height = 10, 10
gameExit = False

# Monster setup
grid_size = (10, 10)

# Load or start a new game
save_or_resume = input("Pick one, Start new game or load previous game: ")
if save_or_resume == "load previous game":
    with open(filename, 'r') as file:
        game_data = json.load(file)
        current_hp = game_data.get("current_hp", MAX_HEALTH)
        current_gold = game_data.get("current_gold", 10)
        inventory = game_data.get("inventory", {})
        print("Game data loaded successfully.")

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
    print("me: health = {}".format(current_hp))
    print("monster: health = {}".format(monster.health))

def pick_item():
    global current_gold
    shop_items = [
        {"price": 5, "name": "sword", "type": "weapon", "maxDurability": 10, "currentDurability": 10},
        {"price": 1, "name": "Armour", "type": "shield", "maxDurability": 5, "currentDurability": 5}
    ]
    
    selection = input("Enter a choice, weapon or shield: ")
    if selection == "weapon":
        item = shop_items[0]
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
    if current_hp <= 0:
        print("Not enough health to fight")
        return

    # Create a new monster for the fight
    monster = WanderingMonster.new_random_monster(grid_size)
     # Check if the monster is None
    if monster is None:
        print("Failed to create a monster!")
        return
    print("You are fighting a {}!".format(monster.name))
    monster = WanderingMonster.new_random_monster(grid_size)
    print(f"Monster created: {monster}")  # Debugging line
    
    if current_gold >= 0:
        pick_item()
    
    while True:
        if "weapon" in inventory:
            weapondamage = inventory["weapon"]["currentDurability"]
            if weapondamage > 0:
                monster.health -= weapondamage
                inventory["weapon"]["currentDurability"] -= 1  # Decrease weapon durability
            else:
                print(f'Not enough Durability to use weapon')
                break
        else:
            print("You have no weapon to fight with!")
            break
        
        if monster.health <= 0:
            print("You killed a {}!".format(monster.name))
            return
        
        current_hp -= monster.power  # Assuming monster has a power attribute
        if current_hp <= 0:
            print("You died fighting a {}!".format(monster.name))
            return
        
        displayFightStatistics(monster)
        choice = getUserFightOptions()
        if choice == '2':
            break
# Initialize the monsters list
monsters = []

# Populate the monsters list with random monsters
for _ in range(5):  # Adjust the number of monsters as needed
    monster = WanderingMonster.new_random_monster(grid_size)
    monsters.append(monster)

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

# Main game loop
while True:
    pick_game()
    
    # Save game state
    game = {
        "current_hp": current_hp,
        "current_gold": current_gold,
        "inventory": inventory
    }
    with open(filename, 'w') as file:
        json.dump(game, file)
    print(f'Data saved to {filename}')

    # Initialize Pygame for graphical interface
    window = pygame.display.set_mode((320, 320))
    gameExit = False

    # Game loop for graphical interface
    while not gameExit:
        window.fill((0, 0, 0))  # Clear the screen
        pygame.draw.circle(window, green, (300, 150), 10, width=0)  # Example monster position
        pygame.draw.circle(window, red, (110, 150), 10, width=0)  # Example monster position
        pygame.draw.rect(window, white, (x, y, width, height))  # Draw player
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                new_x, new_y = x, y  # Reset new position to current position
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

                # Check boundaries
                if 0 <= new_x <= 320 - width and 0 <= new_y <= 320 - height:
                    x, y = new_x, new_y  # Update player position

                # Check for collisions with monsters
                player_rect = pygame.Rect(x, y, width, height)
                for monster in monsters:
                    monster_rect = pygame.Rect(monster.position[0], monster.position[1], 10, 10)  # Assuming monster size
                    if player_rect.colliderect(monster_rect):
                        print(f"You encountered a {monster.name}!")
                        fight_monster()  # Call your fight function here
                        break  # Exit the loop after encountering a monster

        # Move monsters every other frame (or as needed)
        for monster in monsters:
            monster.move(grid_size)  # Move each monster

pygame.quit()
