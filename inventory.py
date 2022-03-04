import os, time

from map import *

class Inventory():
    inventory = [["", ""]] * 8

    def addItem(item, amount): # Add amount
        for space, space_pos in zip(Inventory.inventory, range(len(Inventory.inventory))):
            if space[0] == item:
                Inventory.inventory[space_pos][1] += amount
                break
            elif space[0] == "":
                Inventory.inventory[space_pos] = [item, amount]
                break
        time.sleep(0.1) # NOTE FOR NOW
        
    def display():
        os.system('cls||clear')
        print("Inventory: \n")
        empty_count = 0
        for item in Inventory.inventory:
            if item[0] != "":
                print("%s x%s" % (item[0], item[1]))
            elif item[0] == "":
                empty_count += 1
        if empty_count == 8:
            print("Empty")
    
    def hide():
        os.system('cls||clear')
        Map.display()