import keyboard
from player import Player
from inventory import Inventory

def checkKeyboardInput():
    Player.checkMovement()

    if keyboard.is_pressed('e'):
        Inventory.display()
    if keyboard.is_pressed('f'):
        Inventory.addItem('hi')