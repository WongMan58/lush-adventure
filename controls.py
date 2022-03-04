import keyboard, time
from player import Player
from inventory import Inventory

global inventoryShown
inventoryShown = False

def checkKeyboardInput():
    Player.checkInput()

    if keyboard.is_pressed('e'):
        global inventoryShown
        if not inventoryShown:
            Inventory.display()
            inventoryShown = True
        elif inventoryShown:
            Inventory.hide()
            inventoryShown = False
        time.sleep(0.1)