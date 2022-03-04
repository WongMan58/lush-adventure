import os

class Inventory():
    inventory = [""] * 8

    def addItem(item): # Add amount
        for space, space_pos in zip(Inventory.inventory, range(len(Inventory.inventory))):
            print(Inventory.inventory)
                
    def display():
        os.system('cls||clear')
        print("Inventory: ")
        for item in Inventory.inventory:
            print(item)