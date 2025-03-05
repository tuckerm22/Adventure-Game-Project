from gamefunctions import *
import random
leftovermoney = purchase_item(round((random.random() * 10), 3),
                                  round((random.random() * 10), 3),
                                  round((random.randint(1, 10)), 3))
print(leftovermoney)
    
my_monster = new_random_monster()
print(my_monster)


print_welcome("John")


print_shop_menu("Egg", .23, "Pear", 12.34)


