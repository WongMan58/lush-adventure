import os, time

from map import *

class Inventory():
    inventory = [["", 0]] * 12

    def addItem(item, amount):
        for space, space_pos in zip(Inventory.inventory, range(len(Inventory.inventory))):
            if space[0] == item:
                Inventory.inventory[space_pos][1] += amount
                item_added = True
                break
            elif space[0] == "":
                Inventory.inventory[space_pos][0] = item
                Inventory.inventory[space_pos][1] = amount
    
    def display():
        os.system('cls||clear')
        print("------------------------------")
        print("Inventory:")
        print("------------------------------\n")
        for item in Inventory.inventory:
            if item[0] != "":
                print("- %s x%s" % (item[0], item[1]))
            elif item[0] == "":
                print("- Empty")
    
    def hide():
        os.system('cls||clear')
        Map.display()