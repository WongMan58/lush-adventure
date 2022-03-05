import keyboard, time

from player import *
from inventory import Inventory

class Controls():
    inventoryShown = False

    def checkForUserKeyboardInput():
        if not Controls.inventoryShown:
            Player.checkForKeyboardInput()
        if keyboard.is_pressed('e'):
            if not Controls.inventoryShown:
                Inventory.display()
                Controls.inventoryShown = True
            elif Controls.inventoryShown:
                Inventory.hide()
                Controls.inventoryShown = False
            time.sleep(0.1)
