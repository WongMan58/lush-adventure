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

    def removeItem(item, amount):
        for space, space_pos in zip(Inventory.inventory, range(len(Inventory.inventory))):
            if space[0] == item:
                Inventory.inventory[space_pos][1] -= amount
                break

    def display():
        os.system('cls||clear')
        print("-------------------------------")
        print("          Inventory:")
        print("-------------------------------\n")
        print("- %s: %s" % (Inventory.inventory[0][0], Inventory.inventory[0][1]))
        for item, item_pos in zip(Inventory.inventory, range(len(Inventory.inventory))):
            if item_pos > 0:
                if item[0] == "":
                    print("- Empty")
                elif item[0] != "":
                    print("- %s: x%s" % (item[0], item[1]))
    
    def hide():
        os.system('cls||clear')
        Map.display()