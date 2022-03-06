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
        Map.replace(Player.x, Player.y, Player.costume, True)
    
    def move(change_x, change_y):
        Map.replace(Player.x, Player.y, Map.old_obj, True)
        if change_x != None:
            Player.y += change_x
            Map.replace(Player.x, Player.y, Player.costume, True)
        if change_y != None:
            Player.x -= change_y
            Map.replace(Player.x, Player.y, Player.costume, True)
        time.sleep(0.12)
    
    def checksides():
        up = False
        right = False
        down = False
        left = False

        stone = "█"

        if Player.x > 0 and Map.map[Player.x - 1][Player.y] != stone:
            up = True
        if Player.y < (Map.width - 1) and Map.map[Player.x][Player.y + 1] != stone:
            right = True
        if Player.x < (Map.height - 1) and Map.map[Player.x + 1][Player.y] != stone:
            down = True
        if Player.y > 0 and Map.map[Player.x][Player.y - 1] != stone:
            left = True

        return up, right, down, left
    
    def collectitem():
        if Player.direction == "UP" and Map.map[Player.x - 1][Player.y] == "F":
            Inventory.addItem("Flower", 1)
            Map.replace(Player.x - 1, Player.y, "G", False)
        elif Player.direction == "RIGHT" and Map.map[Player.x][Player.y + 1] == "F":
            Inventory.addItem("Flower", 1)
            Map.replace(Player.x, Player.y + 1, "G", False)
        elif Player.direction == "DOWN" and Map.map[Player.x + 1][Player.y] == "F":
            Inventory.addItem("Flower", 1)
            Map.replace(Player.x + 1, Player.y, "G", False)
        elif Player.direction == "LEFT" and Map.map[Player.x][Player.y - 1]:
            Inventory.addItem("Flower", 1)
            Map.replace(Player.x, Player.y - 1, "G", False)

    def checkForKeyboardInput():
        can_go_up, can_go_right, can_go_down, can_go_left = Player.checksides()

        if keyboard.is_pressed("up") and can_go_up:
            Player.move(None, 1)
            Player.direction = "UP"
        if keyboard.is_pressed("right") and can_go_right:
            Player.move(1, None)
            Player.direction = "RIGHT"
        if keyboard.is_pressed("down") and can_go_down:
            Player.move(None, -1)
            Player.direction = "DOWN"
        if keyboard.is_pressed("left") and can_go_left:
            Player.move(-1, None)
            Player.direction = "LEFT"
        
        if keyboard.is_pressed('g'):
            Player.collectitem()