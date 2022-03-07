import os, time

from map import *

class Inventory():
    inventory = [["", 0]] * 20
    inventory[0] = ["Money", 0]

    def addItem(item, amount):
        for space, space_pos in zip(Inventory.inventory, range(len(Inventory.inventory))):
            if space[0] == item:
                Inventory.inventory[space_pos][1] += amount
                break
            elif space[0] == "":
                Inventory.inventory[space_pos] = [item, amount]
                break
    
    def display():
        os.system('cls||clear')
        print("-------------------------------")
        print("          Inventory:")
        print("-------------------------------\n")
        for item, item_pos in zip(Inventory.inventory, range(len(Inventory.inventory))):
            if item_pos == 0:
                if Inventory.inventory[0][1] == 0:
                    print("- Money: None")
                elif Inventory.inventory[0][1] > 0:
                    print("- Money x%s " % Inventory.inventory[0][1])
            elif item_pos != 0:
                if item[0] != "":
                    print("- %s: x%s" % (item[0], item[1]))
                elif item[0] == "":
                    print("- Empty")
    
    def hide():
        os.system('cls||clear')
        Map.display()