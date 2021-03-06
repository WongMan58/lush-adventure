import keyboard, time

from map import *
from inventory import Inventory

class Player():
    x = 0
    y = 0
    direction = "UP"
    costume = "@"

    def spawn(pos_x, pos_y):
        Map.generate()
        Player.x = pos_x
        Player.y = pos_y
        Map.replaceObject(Player.x, Player.y, Player.costume, True)
    
    def move(change_x, change_y):
        Map.replaceObject(Player.x, Player.y, Map.old_obj, True)
        if change_x != None:
            Player.y += change_x
            Map.replaceObject(Player.x, Player.y, Player.costume, True)
        if change_y != None:
            Player.x -= change_y
            Map.replaceObject(Player.x, Player.y, Player.costume, True)
        
        time.sleep(0.12)
    
    def checksides():
        up = False
        right = False
        down = False
        left = False
        stone = "█"

        if Player.x > 0:
            x_row_info = Map.map[Player.x - 1]
            if x_row_info[Player.y] != stone:
                up = True
        if Player.y < (Map.width - 1):
            x_row_info = Map.map[Player.x]
            if x_row_info[Player.y + 1] != stone:
                right = True
        if Player.x < (Map.height - 1):
            x_row_info = Map.map[Player.x + 1]
            if x_row_info[Player.y] != stone:
                down = True
        if Player.y > 0:
            x_row_info = Map.map[Player.x]
            if x_row_info[Player.y - 1] != stone:
                left = True

        return up, right, down, left
    
    def collectitem():
        flower = "F"
        daisy = "D"

        if Player.direction == "UP" and Player.x > 0:
            x_row_info = Map.map[Player.x - 1]
            if x_row_info[Player.y] == flower:
                Inventory.addItem("Flower", 1)
                Map.replaceObject(Player.x - 1, Player.y, "G", False)
            elif x_row_info[Player.y] == daisy:
                Inventory.addItem("Daisy", 1)
                Map.replaceObject(Player.x - 1, Player.y, "G", False)
        elif Player.direction == "RIGHT" and Player.y < (Map.width - 1):
            x_row_info = Map.map[Player.x]
            if x_row_info[Player.y + 1] == flower:
                Inventory.addItem("Flower", 1)
                Map.replaceObject(Player.x, Player.y + 1, "G", False)
            elif x_row_info[Player.y + 1] == daisy:
                Inventory.addItem("Daisy", 1)
                Map.replaceObject(Player.x, Player.y + 1, "G", False)
        elif Player.direction == "DOWN" and Player.x < (Map.height - 1):
            x_row_info = Map.map[Player.x + 1]
            if x_row_info[Player.y] == flower:
                Inventory.addItem("Flower", 1)
                Map.replaceObject(Player.x + 1, Player.y, "G", False)
            elif x_row_info[Player.y] == daisy:
                Inventory.addItem("Daisy", 1)
                Map.replaceObject(Player.x + 1, Player.y, "G", False)
        elif Player.direction == "LEFT" and Player.y > 0:
            x_row_info = Map.map[Player.x]
            if x_row_info[Player.y - 1] == flower:
                Inventory.addItem("Flower", 1)
                Map.replaceObject(Player.x, Player.y - 1, "G", False)
            elif x_row_info[Player.y - 1] == daisy:
                Inventory.addItem("Daisy", 1)
                Map.replaceObject(Player.x, Player.y - 1, "G", False)

    def checkForKeyboardInput():
        can_go_up, can_go_right, can_go_down, can_go_left = Player.checksides()
        stone = "█"

        # Player movement
        if keyboard.is_pressed("up") and can_go_up:
            Player.move(None, 1)
            Player.direction = "UP"
        elif keyboard.is_pressed("right") and can_go_right:
            Player.move(1, None)
            Player.direction = "RIGHT"
        elif keyboard.is_pressed("down") and can_go_down:
            Player.move(None, -1)
            Player.direction = "DOWN"
        elif keyboard.is_pressed("left") and can_go_left:
            Player.move(-1, None)
            Player.direction = "LEFT"

        # Other player input
        if keyboard.is_pressed('c'):
            Player.collectitem()