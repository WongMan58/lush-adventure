import os, time

from map import *

class Inventory():
    inventory = [["", 0]] * 12

    def addItem(item, amount):
        for space, space_pos in zip(Inventory.inventory, range(len(Inventory.inventory))):
            if space[0] == item:
                Inventory.inventory[space_pos][1] += amount
                break
            elif space[0] == "":
                Inventory.inventory[space_pos] = [item, amount]
                break
        time.sleep(0.1) # NOTE: FOR NOW
        
    def display():
        os.system('cls||clear')
        print("---------------------------------------")
        print("Inventory:                     Money:")
        print("---------------------------------------")
        filled_count = 0
        for item in Inventory.inventory:
            if item[0] == "":
                print("- Empty")
            if item[0] != "":
                print("- %s x%s " % (item[0], item[1]))
                filled_count += 1
        if filled_count == len(Inventory.inventory):
            print("\nInventory is full!")
    
    def hide():
        os.system('cls||clear')
        Map.display()
