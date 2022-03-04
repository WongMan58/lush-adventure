import keyboard, time
from player import Player
from inventory import Inventory

global inventoryShown
inventoryShown = False

def checkKeyboardInput():
    Player.checkMovement()

    if keyboard.is_pressed('e'):
        global inventoryShown
        if not inventoryShown:
            Inventory.display()
            inventoryShown = True
        elif inventoryShown:
            Inventory.hide()
            inventoryShown = False
        time.sleep(0.1)
    if keyboard.is_pressed('f'):
        Inventory.addItem('hi', 2)
        Inventory.addItem("hi2", 2)
        print(Inventory.inventory)